#!/usr/bin/env python3
"""Fail-closed structural validation for TL-WR840N V6.2 TP-Link V2 images."""
import argparse
import struct
import sys
from pathlib import Path

FLASH_LIMIT = 0x3E0000
TFTP_FLASH_LIMIT = 0x3E0000
FW_LENGTH = 0x3D0000
TFTP_PAD = 0x10000
EXPECTED = {
    "sysupgrade.bin": {"hwid": 0x08400006, "hwrev": 0x1, "hwrevadd": 0x7},
    "tftp-recovery.bin": {"hwid": 0x08400006, "hwrev": 0x1, "hwrevadd": 0x7},
}

def u32(data, offset):
    return struct.unpack_from(">I", data, offset)[0]

def validate(path, kind):
    data = path.read_bytes()
    if len(data) < 0x200:
        raise ValueError(f"{path.name}: shorter than TP-Link V2 header")
    # Offsets come from struct fw_header in mktplinkfw2.c.
    version, hwid, hwrev, hwrevadd = (u32(data, o) for o in (0x00, 0x34, 0x38, 0x3c))
    fwlen, kernel_ofs, kernel_len, rootfs_ofs, rootfs_len, boot_ofs, boot_len = (
        u32(data, o) for o in (0x70, 0x74, 0x78, 0x7c, 0x80, 0x84, 0x88)
    )
    exp = EXPECTED[kind]
    for key, value in (("HWID", hwid), ("HWREV", hwrev), ("HWREVADD", hwrevadd)):
        want = exp[key.lower()]
        if value != want:
            raise ValueError(f"{path.name}: {key}=0x{value:x}, expected 0x{want:x}")
    if fwlen != FW_LENGTH:
        raise ValueError(f"{path.name}: header firmware length 0x{fwlen:x}, expected 0x{FW_LENGTH:x}")
    if kernel_ofs != 0x200 or kernel_len == 0 or rootfs_len == 0:
        raise ValueError(f"{path.name}: invalid kernel/rootfs offsets or lengths")
    if kernel_ofs + kernel_len > len(data) or rootfs_ofs + rootfs_len > len(data):
        raise ValueError(f"{path.name}: header payload range exceeds file")
    if rootfs_ofs < kernel_ofs + kernel_len:
        raise ValueError(f"{path.name}: rootfs overlaps kernel")
    if boot_ofs != 0 or boot_len != 0:
        raise ValueError(f"{path.name}: bootloader payload must be absent")
    if kind == "sysupgrade.bin" and len(data) > FLASH_LIMIT:
        raise ValueError(f"{path.name}: exceeds 3968 KiB firmware image limit")
    if kind == "tftp-recovery.bin":
        if len(data) > TFTP_FLASH_LIMIT:
            raise ValueError(f"{path.name}: exceeds 0x3e0000 firmware partition limit")
        if len(data) <= TFTP_PAD or data[-TFTP_PAD:] != bytes(TFTP_PAD):
            raise ValueError(f"{path.name}: expected trailing 64 KiB zero padding")
        if len(data) - TFTP_PAD > FW_LENGTH:
            raise ValueError(f"{path.name}: pre-padding image exceeds 0x3d0000 firmware payload limit")
    print(f"PASS {path.name}: size={len(data)} bytes, version-field=0x{version:08x}, "
          f"HWID=0x{hwid:08x}, HWREV=0x{hwrev:x}, HWREVADD=0x{hwrevadd:x}, "
          f"kernel=[0x{kernel_ofs:x},0x{kernel_ofs + kernel_len:x}), "
          f"rootfs=[0x{rootfs_ofs:x},0x{rootfs_ofs + rootfs_len:x}), "
          f"boot_len={boot_len}")

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("directory", type=Path)
    args = parser.parse_args()
    try:
        for name in EXPECTED:
            candidates = list(args.directory.glob(f"*{name}"))
            if len(candidates) != 1:
                raise ValueError(f"expected exactly one *{name}, found {len(candidates)}")
            validate(candidates[0], name)
    except (OSError, ValueError, struct.error) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1
    return 0

if __name__ == "__main__":
    sys.exit(main())
