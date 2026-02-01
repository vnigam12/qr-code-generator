# 📌 QR Code Generator (Python)

A **QR Code Generator** built with Python that supports:

✅ Generate **multiple QR codes at once**  
✅ Custom **QR color + background color**  
✅ Supports **PNG / JPG** output formats  
✅ **URL validation** + auto-add `https://` for domains  

## 🚀 Features

- Generate QR codes from:
  - URLs (validated)
  - Plain text
- Auto-correct URLs:
  - `amazon.com` → `https://amazon.com`
- Saves each QR code with a unique filename:
  - `qr_1.png`, `qr_2.png`, etc.

## 📦 Installation

Clone the repo:

```bash
git clone https://github.com/<your-username>/qr-code-generator.git
cd qr-code-generator
Create and activate a virtual environment:

python3 -m venv .venv
source .venv/bin/activate
Install dependencies:

pip install -r requirements.txt
```

## ▶️ Run the program
```bash
python src/qr_generator.py
```

## 🧪 Run tests
```bash
pytest -v
```

## 📝 Example Input
```bash
Enter QR color (default: black): blue
Enter background color (default: white): white
Choose file type (png/jpg) [default: png]: png
Enter text/URL(s): amazon.com, https://aws.amazon.com, Hello World
Enter base filename (example: qr_code): my_qr
Output files:

my_qr_1.png

my_qr_2.png

my_qr_3.png
```

## 🛠 Tech Stack

- Python 3
- qrcode + Pillow
- pytest

## 📄 License
```bash
MIT License
```
