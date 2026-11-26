# Proyek Codex — TL-WR840N V6.20 + XMC XM25QH32DHIG

Paket ini disiapkan untuk audit source OpenWrt 19.07.10 dan penyelidikan boot failure XMC. Firmware yang ada sebelumnya belum terbukti bisa boot pada chip XMC.

## Isi
- `AGENTS.md`: aturan kerja dan konteks teknis yang wajib dibaca Codex.
- `CODEX-FIRST-TASK-ID.txt`: prompt pertama untuk Codex (audit read-only).
- `.github/workflows/build-wr840n-xmc.yml`: workflow build terakhir yang akan diaudit, bukan dianggap benar.
- `source/openwrt-19.07-tl-wr840n-v6.x-main.zip`: source OpenWrt yang sedang digunakan.
- `reference/previous-build-SHA256SUMS.txt`: checksum artefak build sebelumnya.

## Penting
Jangan flash image yang lama atau image hasil build baru hanya karena proses kompilasi berhasil. Tahap pertama hanya audit kode dan workflow. Simpan firmware stock dan recovery TFTP yang sudah pernah berhasil.

## Memulai
1. Ekstrak paket ini ke folder lokal.
2. Buka terminal di folder proyek.
3. Jalankan Codex di folder tersebut.
4. Kirim isi `CODEX-FIRST-TASK-ID.txt` sebagai tugas pertama.
5. Minta Codex hanya melaporkan audit; jangan mengizinkan perubahan sampai hasilnya ditinjau.
