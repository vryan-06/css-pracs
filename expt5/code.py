import hashlib
import timeit

text_inputs = ["12233344445555566666666666", "aaasssdddfffggggggggggghhhhhhhhhhh", "qwertyuiopasdfghjklzxcvbnmnbvcxzlkjhgfdsapoiuytrewq"]

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