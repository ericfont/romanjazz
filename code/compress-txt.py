import zlib
import base64

print("Begin compress-txt.py...")

# open utf-8 encoded file as bytes
with open('all-charts-tabs.txt', 'rb') as f:
    input_file_bytes = f.read()

print(f"input_file_bytes Length: {len(input_file_bytes)}")

# 2. Compress the bytes using zlib
compressed_data = zlib.compress(input_file_bytes)

print(f"compressed_data Length: {len(compressed_data)}")

# 3. Encode the compressed bytes as a Base64 string
b64_encoded = base64.b64encode(compressed_data)
print(f"b64_encoded: {b64_encoded}")      

print(f"b64_encoded Length: {len(b64_encoded)}")

# Verification: Convert the Base64 bytes back to a readable ASCII string

# 2. Decompress the bytes using zlib
decompressed_bytes = zlib.decompress(compressed_data)

# 3. Convert bytes back to the original string
print(f"decoded string: {decompressed_bytes.decode('utf-8')}")                         
