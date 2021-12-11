import hashlib
import itertools
key = "iwrupvqb"

def find_hash(num_zeroes):
    zeroes = "0" * num_zeroes
    for c in itertools.count():
        attempt = f"{key}{c}".encode()
        if hashlib.md5(attempt).hexdigest()[:num_zeroes] == zeroes:
            return c

print("Part 1:", find_hash(5))
print("Part 2:", find_hash(6))