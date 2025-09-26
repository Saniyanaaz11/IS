def create_matrix(key):
    key = key.lower().replace('j', 'i')
    alphabet = "abcdefghiklmnopqrstuvwxyz"
    seen, matrix = {}, []
    for ch in key + alphabet:
        if ch.isalpha() and ch not in seen:
            seen[ch] = divmod(len(matrix), 5)
            matrix.append(ch)
    return [matrix[i:i+5] for i in range(0, 25, 5)], seen

def prepare_text(text):
    text = text.lower().replace('j', 'i').replace(' ', '')
    result, i = [], 0
    while i < len(text):
        a = text[i]
        b = text[i+1] if i+1 < len(text) else 'x'
        if a == b:
            result += [a, 'x']
            i += 1
        else:
            result += [a, b]
            i += 2
    if len(result) % 2: 
        result.append('x')
    return ''.join(result)

def process_pair(matrix, pos, a, b, shift):
    r1, c1 = pos[a]; r2, c2 = pos[b]
    if r1 == r2:  # same row
        return matrix[r1][(c1+shift)%5] + matrix[r2][(c2+shift)%5]
    if c1 == c2:  # same col
        return matrix[(r1+shift)%5][c1] + matrix[(r2+shift)%5][c2]
    return matrix[r1][c2] + matrix[r2][c1]

def clean_decrypted(text):
    cleaned, i = [], 0
    while i < len(text)-2:
        a, b, c = text[i], text[i+1], text[i+2]
        if b == 'x' and a == c:
            cleaned.append(a); i += 2
        else:
            cleaned.append(a); i += 1
    cleaned.extend(text[i:])
    return ''.join(cleaned).rstrip('x')

# main
text = input("Enter the plain text: ")
key  = input("Enter Key value: ")

matrix, pos = create_matrix(key)
prepared    = prepare_text(text)

encrypted = ''.join(process_pair(matrix, pos, prepared[i], prepared[i+1], 1) 
                    for i in range(0, len(prepared), 2))
decrypted = ''.join(process_pair(matrix, pos, encrypted[i], encrypted[i+1], -1) 
                    for i in range(0, len(encrypted), 2))
cleaned   = clean_decrypted(decrypted)

print("Encrypted Text:", encrypted)
print("Decrypted Text:", cleaned)
