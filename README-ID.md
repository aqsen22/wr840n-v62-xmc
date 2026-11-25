# Paket final build — TL-WR840N V6.2 + XMC XM25QH32D

Upload seluruh isi folder ini ke root repository GitHub Anda. Jangan mengunggah folder induk sebagai satu direktori; unggah isi di dalamnya. Pastikan `.github` ikut terunggah.

Struktur:
- `.github/workflows/build-wr840n-xmc.yml`
- `source/openwrt-19.07-tl-wr840n-v6.x-main.zip` (source WR840N V6.2 dengan patch XMC)
- `config.seed`

Buka Actions → Build WR840N V6.2 XMC → Run workflow. Jika berhasil, ambil BIN dari Artifacts.

Peringatan: ini adalah paket build, bukan firmware BIN. Patch harus berhasil diterapkan dan hasil build harus diperiksa. Keberhasilan kompilasi tidak menjamin router akan boot. Simpan firmware stock dan metode recovery sebelum uji.
