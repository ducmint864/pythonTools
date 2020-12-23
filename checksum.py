import hashlib
import sys

md5_hash = hashlib.md5()
addr = input("Full address to file in system: ")
sample = input("Sample to compare to: ")
file = open(addr, "rb")
content = file.read()
md5_hash.update(content)

result = md5_hash.hexdigest()
print("Your file:\t "+result)
print("Source sample:\t "+sample)
if result == sample:
	print("Match! Your file is safe")
	exit()
print("\n>>>Unmatched! Your file is corrupted!")

