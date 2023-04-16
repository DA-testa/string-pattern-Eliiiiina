import os

def read_input():
    input_choice = input().strip().upper()
    if input_choice == 'I':
        pattern = input().strip()
        text = input().strip()
    elif input_choice == 'F':
        filename = input("Enter the file name: ")
        file_path = os.path.join('./tests', filename)
        with open(file_path, 'r') as f:
            pattern = f.readline().strip()
            text = f.readline().strip()
    return pattern, text

def print_occurrences(output):
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    p = 10**9 + 7
    x = 263
    m = len(pattern)
    n = len(text)
    p_hash = sum(ord(pattern[i]) * pow(x, i, p) for i in range(m)) % p
    t_hash = sum(ord(text[i]) * pow(x, i, p) for i in range(m)) % p
    h = pow(x, m-1, p)
    occurrences = []
    if p_hash == t_hash and pattern == text[:m]:
        occurrences.append(0)
    for i in range(1, n-m+1):
        t_hash = ((t_hash - ord(text[i-1]) * h) * x + ord(text[i+m-1])) % p
        if p_hash == t_hash and pattern == text[i:i+m]:
            occurrences.append(i)
    return occurrences

if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))
