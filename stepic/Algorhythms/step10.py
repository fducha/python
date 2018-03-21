count_letters, code_str_size = map(int, input().split())
alphabet = {}
for _ in range(count_letters):
    letter, letter_code = input().split(': ')
    alphabet[letter_code] = letter
code = input()

result = ''
while len(code) != 0:
    for lc in alphabet:
        if code.startswith(lc):
            result += alphabet[lc]
            code = code[len(lc):]
            break
print(result)
