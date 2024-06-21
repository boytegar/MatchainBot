import base64
import zlib
import json

def decode_file(encoded_content):
    # Balik urutan string dan decode dari base64
    compressed_content = base64.b64decode(encoded_content[::-1])

    # Dekompresi data
    original_content = zlib.decompress(compressed_content).decode()

    return original_content

# Baca file terenkripsi dari file
with open('encoded_files.json', 'r') as file:
    encoded_files = json.load(file)

# Dekripsi dan eksekusi setiap file
for file_path, encoded_content in encoded_files.items():
    original_content = decode_file(encoded_content)
    exec(original_content)