# 🛰️ Traceroute Analyzer: Deteksi Jalur Jaringan & Titik Kemacetan

Proyek ini dirancang untuk menganalisis jalur jaringan menggunakan perintah `traceroute`, lalu memvisualisasikan titik-titik kemacetan dan jalur yang lancar. Cocok untuk pembelajaran troubleshooting jaringan, terutama di lingkungan virtual seperti VirtualBox.

---

## 🎯 Tujuan Proyek

- Menjalankan traceroute ke host tujuan
- Mengidentifikasi setiap hop (lompatan) dalam jalur jaringan
- Menandai hop yang lambat (macet) dan cepat (lancar)
- Menyajikan grafik latency per hop secara visual

---

## 🛠️ Teknologi yang Digunakan

- Python 3
- Modul: `subprocess`, `re`, `matplotlib`
- Sistem operasi: Linux (Ubuntu/Debian)
- Terminal dengan akses ke perintah `traceroute`

---

## 🚀 Cara Menjalankan

1. Pastikan Python dan traceroute sudah terinstal:
   ```bash
   sudo apt update
   sudo apt install traceroute python3 python3-pip
   pip install matplotlib
