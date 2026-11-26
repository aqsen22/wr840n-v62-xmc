# Verifikasi driver XMC XM25QH32D

Status: NOT VERIFIED

Model komponen:
Nama/marking persis yang tercetak pada chip:
Vendor datasheet lengkap, nomor dokumen, revisi, tanggal:
SHA256 datasheet:

| Fitur driver Linux 4.14 yang diklaim | Bukti halaman/tabel/register datasheet | Pemetaan source (file/baris/simbol) | Status |
|---|---|---|---|
| JEDEC ID 0x204016 | | spi-nor.c flash_info entry | UNKNOWN |
| Kapasitas 32 Mbit / 4 MiB | | size/sector count in INFO() | UNKNOWN |
| Erase 4 KiB dan opcode/parameter | | SECT_4K / erase map | UNKNOWN |
| Erase 64 KiB dan opcode/parameter | | sector geometry | UNKNOWN |
| Page program size dan batas halaman | | spi-nor core | UNKNOWN |
| Read command/mode yang dipilih | | spi-nor core/controller | UNKNOWN |
| Status/WIP/WEL/error/protection handling | | spi-nor core and flags | UNKNOWN |
| SFDP availability and fallback behavior | | datasheet and kernel implementation | UNKNOWN |
| Timing and voltage compatibility | | datasheet and board supply evidence | UNKNOWN |

Reviewer:
Tanggal:
Kesimpulan teknis dan batas bukti:

Ubah menjadi tepat Status: VERIFIED hanya setelah semua baris wajib ditelaah terhadap datasheet resmi yang cocok dengan exact part suffix. Status ini bukan bukti boot berhasil pada perangkat keras.
