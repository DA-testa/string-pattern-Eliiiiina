# python3

def read_input():
    # this function acquires input from both keyboard and file
    input_type = input().rstrip()
    if input_type == 'I':
        pattern = input().rstrip()
        text = input().rstrip()
    elif input_type == 'F':
        filename = input().rstrip()
        with open(filename, 'r') as f:
            pattern = f.readline().rstrip()
            text = f.readline().rstrip()
    return pattern, text

def print_occurrences(output):
    # this function controls output, it doesn't need any return
    print(' '.join(map(str, output)))

def get_occurrences(pattern, text):
    # Rabin Karp algorithm for finding the occurrences of the pattern in the text
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
