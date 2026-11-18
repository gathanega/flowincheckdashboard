"""Bangun dashboard.html (satu file mandiri) dari index.html + assets/logo.png.

Jalankan setiap kali index.html atau logo berubah:
    python build_single_file.py
"""
from pathlib import Path
import base64

folder = Path(__file__).parent
index = (folder / "index.html").read_text(encoding="utf8")
logo_b64 = base64.b64encode((folder / "assets" / "logo.png").read_bytes()).decode("ascii")

count = index.count('src="assets/logo.png"')
out = index.replace('src="assets/logo.png"', 'data-logo="1"')

inject = (
    "<script>(function(){var L=\"data:image/png;base64," + logo_b64 + "\";"
    "var imgs=document.querySelectorAll('img[data-logo]');"
    "for(var i=0;i<imgs.length;i++){imgs[i].src=L;}})();</script>\n"
)
out = out.replace("</body>", inject + "</body>")
(folder / "dashboard.html").write_text(out, encoding="utf8")

print(f"logo di-embed sekali, dipakai di {count} <img>")
print(f"output: {(folder / 'dashboard.html').stat().st_size:,} bytes")
