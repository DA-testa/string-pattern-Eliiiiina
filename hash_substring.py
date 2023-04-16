# python3
import sys
import random

def read_input():
    choice = input().rstrip()
    if choice == "F":
        with open("/.tests", "r") as file:
            pattern = file.readline().rstrip()
            text = file.readline().rstrip()
    else:
        pattern = input().rstrip()
        text = input().rstrip()
    return (pattern, text)

def print_occurrences(output):
    print(' '.join(map(str, output)))

def poly_hash(s, prime, x):
    ans = 0
    for c in reversed(s):
        ans = (ans * x + ord(c)) % prime
    return ans

def precompute_hashes(text, pattern_len, prime, x):
    H = [0] * (len(text) - pattern_len + 1)
    s = text[-pattern_len:]
    H[-1] = poly_hash(s, prime, x)
    y = 1
    for _ in range(pattern_len):
        y = (y * x) % prime
    for i in reversed(range(len(text) - pattern_len)):
        H[i] = (x * H[i + 1] + ord(text[i]) - y * ord(text[i + pattern_len])) % prime
    return H

def rabin_karp(pattern, text):
    if len(pattern) > len(text):
        return []

    prime = 1000000007
    x = random.randint(1, prime - 1)
    pattern_hash = poly_hash(pattern, prime, x)
    H = precompute_hashes(text, len(pattern), prime, x)
    return [i for i in range(len(text) - len(pattern) + 1) if pattern_hash == H[i] and text[i:i + len(pattern)] == pattern]

def get_occurrences(pattern, text):
    return rabin_karp(pattern, text)

if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))
