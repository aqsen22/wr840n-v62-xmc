# Paket build otomatis — TP-Link TL-WR840N V6.2 + XMC XM25QH32D

Paket ini menjalankan kompilasi di GitHub Actions. Komputer pengguna tidak perlu memasang Ubuntu/WSL.

## Isi paket

- `source/openwrt-19.07-tl-wr840n-v6.x-main.zip` — source fork OpenWrt 19.07 yang menyertakan profil TL-WR840N V6.2.
- `patches/303-mtd-spi-nor-add-xmc-xm25qh32d.patch` — patch awal untuk JEDEC ID XMC `20 40 16`.
- `config.seed` — pemilihan target MediaTek MT76x8 dan profil WR840N V6.2.
- `.github/workflows/build-wr840n-xmc.yml` — workflow build otomatis.

## Cara menjalankan

1. Masuk ke https://github.com dan buat repository baru, misalnya `wr840n-v62-xmc`.
2. Upload seluruh isi folder paket ini ke root repository. Pastikan folder `.github/workflows/` ikut terunggah (di Windows, aktifkan **View > Show > Hidden items** jika folder tidak terlihat).
3. Buka tab **Actions** pada repository.
4. Pilih workflow **Build OpenWrt 19.07.10 - WR840N V6.2 XMC**.
5. Klik **Run workflow** dan tunggu sampai selesai. Kompilasi dapat memerlukan waktu cukup lama.
6. Jika status workflow hijau, buka hasil run tersebut, cari bagian **Artifacts**, lalu unduh `WR840N-V6.2-XMC-OpenWrt-19.07.10`.
7. Di dalam ZIP artifact akan ada file BIN yang dibuat. Prioritaskan `sysupgrade.bin` hanya jika router sedang menjalankan OpenWrt yang kompatibel. Jangan gunakan file recovery/factory melalui antarmuka web stock kecuali image itu memang telah dibuat dan divalidasi untuk metode tersebut.

## Catatan penting

- Workflow akan berhenti jika profil WR840N V6.2 tidak terpilih atau proses patch/build gagal.
- Patch XMC ini merupakan patch awal yang perlu dibuktikan oleh proses `target/linux/prepare` dan build. Keberhasilan kompilasi tidak membuktikan router pasti boot; tetap uji dengan kabel LAN dan siapkan firmware stock serta metode TFTP recovery.
- Chip yang ditargetkan: XMC XM25QH32D, kapasitas 32 Mbit (4 MiB), JEDEC ID `20 40 16`.
- Perangkat harus benar-benar TL-WR840N V6.2 dengan chip flash yang sama. Jangan gunakan untuk varian hardware lain.
- OpenWrt 19.07.10 sudah EOL. Paket ini khusus untuk pengujian kompatibilitas, bukan rekomendasi penggunaan jangka panjang.
