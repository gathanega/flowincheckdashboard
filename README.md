# Dashboard ATCS — Flowincheck

Folder khusus untuk seluruh berkas UI dashboard. Tidak ada logika backend di sini;
server yang menyajikan halaman berada di `../atcs_unified/app.py`.

## Isi folder

| Berkas | Rute | Keterangan |
|--------|------|------------|
| `index.html` | `/` | Dashboard Flowincheck (tema terang, 6 CCTV Tier 1) |
| `3tier.html` | `/3tier` | Dashboard 3-tier (produksi, riset, analitik) |
| `assets/logo.png` | `/assets/logo.png` | Logo Flowincheck |

## Sumber data

Dashboard memanggil API di server yang sama:

- `/api/public-config`
- `/api/locations`
- `/api/logs`
- `/api/hourly`
- `/api/insight?location=...`
- `/api/devices`
- `/api/frame` dan `/api/detections` (opsional, 404 bila belum ada frame)

Data diambil dari SQLite `../atcs_unified/data/atcs.sqlite3`.

## Menjalankan

```powershell
$env:PYTHONPATH="C:\Users\Than\AppData\Local\Temp\opencode\fic\pylib"
cd "C:\Users\Than\Documents\Default Project\flowincheck\atcs_unified"
python -m uvicorn app:app --host 127.0.0.1 --port 8000
```

Buka:

- http://127.0.0.1:8000/ — dashboard Flowincheck
- http://127.0.0.1:8000/3tier — dashboard 3-tier

## Catatan

- Tema default terang; tombol tema di header tetap bisa mengubah ke gelap.
- Aset eksternal dimuat dari CDN: Google Fonts (Inter), Chart.js, Leaflet,
  hls.js, dan mqtt.js. Tanpa internet, chart/peta tidak akan tampil.
- MQTT dinonaktifkan pada server integrasi; data diperbarui lewat polling API.
- Untuk menghentikan data simulasi:
  ```sql
  DELETE FROM observations WHERE source='demo-seed';
  ```
