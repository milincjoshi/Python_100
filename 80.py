'''
Question:
Please write a program to compress and 
decompress the string "hello world!hello world!hello world!hello world!".
Hints:
Use zlib.compress() and zlib.decompress() to compress and decompress a string.
'''

import zlib
x = "hello world!hello world!hello world!hello world!"
compressed = zlib.compress(x)
decompressed = zlib.decompress(compressed)
print compressed
print decompressed