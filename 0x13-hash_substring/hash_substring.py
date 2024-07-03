def poly_hash(s, prime, multiplier):
    hash_value = 0
    for char in reversed(s):
        hash_value = (hash_value * multiplier + ord(char)) % prime
    return hash_value

def precompute_hashes(text, pattern_len, prime, multiplier):
    text_len = len(text)
    last_substring = text[-pattern_len:]
    H = [0] * (text_len - pattern_len + 1)
    H[-1] = poly_hash(last_substring, prime, multiplier)
    y = pow(multiplier, pattern_len, prime)
    for i in range(text_len - pattern_len - 1, -1, -1):
        H[i] = (multiplier * H[i + 1] + ord(text[i]) - y * ord(text[i + pattern_len])) % prime
        if H[i] < 0:
            H[i] += prime
    return H

def rabin_karp(text, pattern):
    text_len = len(text)
    pattern_len = len(pattern)
    prime = 1000000007
    multiplier = 236
    result = []
    pattern_hash = poly_hash(pattern, prime, multiplier)
    hash_substrings = precompute_hashes(text, pattern_len, prime, multiplier)
    for i in range(text_len - pattern_len + 1):
        if pattern_hash == hash_substrings[i]:
            if text[i:i + pattern_len] == pattern:
                result.append(i) 
    return result

if __name__ == '__main__':
    pattern = input()
    text = input()
    positions = rabin_karp(text, pattern)
    for pos in positions:
        print(pos, end=' ')