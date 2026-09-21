import os
import requests
import zipfile

# تنظیمات لینک و نام فایل
url = "https://drive.google.com/drive/folders/0BxYys69jI14kU0I1YUQyY1ZDRUE?usp=sharing"
zip_target = "dataset.zip"
extract_path = "./data"

print("Downloading dataset...")
response = requests.get(url, stream=True)
with open(zip_target, "wb") as f:
    for chunk in response.iter_content(chunk_size=8192):
        if chunk:
            f.write(chunk)

print("Extracting files...")
with zipfile.ZipFile(zip_target, 'r') as zip_ref:
    zip_ref.extractall(extract_path)

os.remove(zip_target)
print(f"Dataset successfully downloaded and extracted to {extract_path}")

