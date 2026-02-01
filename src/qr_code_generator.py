import qrcode
from urllib.parse import urlparse

def is_valid_url(text: str) -> bool:
    # Return True if text is a valid http/https URL
    parsed = urlparse(text)
    return parsed.scheme in ("http", "https") and bool(parsed.netloc)

def looks_like_domain(text: str) -> bool:
    # Check if input looks like a domain without scheme
    return "." in text and " " not in text and not text.startswith(("http://", "https://"))

def normalize_url(text: str) -> str:
    # Prepend https:// if input looks like a domain without scheme
    return "https://" + text if looks_like_domain(text) else text

def normalize_file_extension(ext: str) -> str:
    # Normalize file extension input to png/jpg
    ext = ext.strip().lower().replace(".","")
    if ext == "jpeg":
        ext = "jpg"
    return ext

def generate_qr(data: str, filename: str, fill_color: str, back_color: str) -> None:
    # Generate and save a QR code image from the given data
    qr = qrcode.QRCode(box_size=10, border=4)
    qr.add_data(data)
    qr.make(fit=True)

    image = qr.make_image(fill_color = fill_color, back_color = back_color)
    image.save(filename)

def main() -> None:
    print("QR Code Generator")

    # Choose QR colors
    fill_color = input("Enter QR color (default: black): ").strip().lower() or "black"
    back_color = input("Enter background color (default: white): ").strip().lower() or "white"

    # Input file extension
    file_ext = input("Enter file type (png/jpg) [default: png]: ").strip().lower() or "png"
    file_ext = normalize_file_extension(file_ext)

    if file_ext not in ("png", "jpg"):
        print("Invalid file type. Only PNG and JPG are supported")
        raise SystemExit

    # Multiple QR codes input
    print("\nEnter multiple URL(s)/text(s) separated by commas")
    data_list_input = input("Enter URL(s)/text(s): ").strip()
    data_list = [item.strip() for item in data_list_input.split(",") if item.strip()]

    if not data_list:
        print("No valid URL/text input provided")
        raise SystemExit

    base_filename = input("Enter base filename (example: qr_code): ").strip() or "qr_code"

    # Generate QR codes
    for i, raw_data in enumerate(data_list, start=1):
        filename = f"{base_filename}_{i}.{file_ext}"
        data = normalize_url(raw_data)

        if data.startswith(("http://", "https://")):
            if not is_valid_url(data):
                print("Skipping invalid URL: {raw_data}")
                continue

            if raw_data != data:
                print("Autocorrected URL: {raw_data} -> {data}")

        generate_qr(data, filename, fill_color, back_color)
        print(f"QR code saved: {filename} | Data: {data}")

    print(f"All QR codes generated successfully!")

if __name__ == "__main__":
    main()