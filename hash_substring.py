import os

def read_input():
    input_type = input().strip().upper()
    if input_type == 'I':
        pattern = input().strip()
        text = input().strip()
    elif input_type == 'F':
        filename = input("Enter the file name: ")
        file_path = os.path.join('./tests', filename)
        with open(file_path, 'r') as f:
            pattern = f.readline().strip()
            text = f.readline().strip()
    return pattern, text

def print_occurrences(output):
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    p = 1000000007
    x = 263
    m = len(pattern)
    n = len(text)
    h = pow(x, m-1, p)
    p_hash = 0
    t_hash = 0
    occurrences = []
    for i in range(m):
        p_hash = (p_hash*x + ord(pattern[i])) % p
        t_hash = (t_hash*x + ord(text[i])) % p
    if p_hash == t_hash and pattern == text[:m]:
        occurrences.append(0)
    for i in range(1, n-m+1):
        t_hash = (t_hash - h*ord(text[i-1])) % p
        t_hash = (t_hash*x + ord(text[i+m-1])) % p
        if p_hash == t_hash and pattern == text[i:i+m]:
            occurrences.append(i)
    return occurrences

if __name__ == '__main__':
    print_occurrences(get_occurrences(*read_input()))
