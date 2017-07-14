#!/usr/bin/env python3

# Script to decompress GMod Lua cache folder

import lzma
import sys
import os

if len(sys.argv) < 2:
	print("Usage: gluacache.py <lua cache folder path>")
	sys.exit()

folder = sys.argv[1]
outputdir = os.path.join(folder, "decompressed")

if not os.path.exists(outputdir):
	os.makedirs(outputdir)

print("[*] Beginning writing of decompressed files")

for f in os.listdir(folder):
	if os.path.splitext(f)[1] == ".lua":
		with open(os.path.join(folder, f), "rb") as compressed:
			compressed.seek(4) # Take out the trash
			with lzma.open(compressed) as decompressed:
				lua = decompressed.read()
				lua = lua.decode("ascii", "ignore")
				with open(os.path.join(outputdir, f), "w+") as out:
					out.write(lua[:-1]) # Remove null byte
					
print("[*] Wrote files to cache/lua/decompressed!")