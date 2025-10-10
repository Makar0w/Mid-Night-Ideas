#decompress
import zlib
import time
with open("Compressed.txt", "rb") as file:
    comp_data = file.read()
decompressed = zlib.decompress(comp_data).decode("utf-8")
print(decompressed)
time.sleep(10)