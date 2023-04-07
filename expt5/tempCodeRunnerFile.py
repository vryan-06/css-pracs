import hashlib
import timeit

files = ["1kb_file.txt", "2kb_file.txt", "5kb_file.txt"]
text_inputs = []

for file in files:
    with open(file, "r") as f:
        text_inputs.append(f.read())

# print(text_inputs)
print("----MD5----")
for t in text_inputs:
    t1 = timeit.default_timer()
    hash_md5 = hashlib.md5(t.encode())
    t2 = timeit.default_timer()
    res = (t2 - t1) * 1000000
    print("Input: ",t)
    print("Hash: ",hash_md5.hexdigest())
    print("Time to Complete: ",res, "microseconds")
    print()

print("----SHA----")
for t in text_inputs:
    t1 = timeit.default_timer()
    hash_sha = hashlib.sha1(t.encode())
    t2 = timeit.default_timer()
    res = (t2 - t1) * 1000000
    print("Input: ",t)
    print("Hash: ",hash_sha.hexdigest())
    print("Time to Complete: ",res, "microseconds")
    print()