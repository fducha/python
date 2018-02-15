main_abc, code_abc = input(), input()
str_to_encode, str_to_decode = list(input()), list(input())

# encode_dict = {}
# for i in range(len(main_abc)):
#     encode_dict[main_abc[i]] = code_abc[i]
#
# decode_dict = {}
# for i in range(len(code_abc)):
#     decode_dict[code_abc[i]] = main_abc[i]

for i in range(len(str_to_encode)):
    # str_to_encode[i] = encode_dict[str_to_encode[i]]
    str_to_encode[i] = code_abc[main_abc.index(str_to_encode[i])]

for i in range(len(str_to_decode)):
    # str_to_decode[i] = decode_dict[str_to_decode[i]]
    str_to_decode[i] = main_abc[code_abc.index(str_to_decode[i])]

print(''.join(str_to_encode))
print(''.join(str_to_decode))
