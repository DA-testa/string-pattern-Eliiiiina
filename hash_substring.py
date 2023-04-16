import sys
import os
import random

def read_input():
    choice = sys.stdin.readline().rstrip()
    if choice == "F":
        fails = sys.stdin.readline().rstrip()
        atrasanas = './tests/'
        faila_vieta = os.path.join(atrasanas, fails)
        try:
            with open(faila_vieta, mode="r") as file:
                n = int(file.readline())
                data = list(map(int, file.readline().split()))
        except FileNotFoundError:
            print("File not found.")
            sys.exit()
        except ValueError:
            print("Invalid input format.")
            sys.exit()
        return (data[0], data[1])
    else:
        pattern = sys.stdin.readline().rstrip()
        text = sys.stdin.readline().rstrip()
        return (pattern, text)

def print_occurrences(output):
    print(' '.join(map(str, output)))

def poly_hash(s, prime, x):
    ans = 0
    for c in reversed(s):
        ans = (ans * x + ord(c)) % prime
    return ans

def precompute_hashes(text, pattern_len, prime, x):
    hashes = [0] * (len(text) - pattern_len + 1)
    substring = text[-pattern_len:]
    hashes[-1] = poly_hash(substring, prime, x)
    y = 1
    for _ in range(pattern_len):
        y = (y * x) % prime
    for i in reversed(range(len(text) - pattern_len)):
        hashes[i] = (x * hashes[i + 1] + (text[i] - y * text[i + pattern_len])) % prime
    return hashes

def rabin_karp(pattern, text):
    prime = 1000000007
    x = random.randint(1, prime - 1)
    pattern_hash = poly_hash(pattern, prime, x)
    hashes = precompute_hashes(text, len(pattern), prime, x)
    return [i for i in range(len(text) - len(pattern) + 1) if pattern_hash == hashes[i] and text[i:i + len(pattern)] == pattern]

def get_occurrences(pattern, text):
    return rabin_karp(pattern, text)

if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))
