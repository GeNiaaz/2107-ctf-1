# def generate_list_for_padding_check(n):
#     result_list = []
#     for i in range(2, n + 1):
#         num_hex = hex(i)
#         num_str = str(num_hex)
#         num_str = num_str.replace("0x", "")
#         if len(num_str) < 2:
#             num_str = "0" + num_str
#         result_list.append(num_str)
#     if len(result_list) < 1:
#         return ["00"]
#
#     return result_list
#
#
# print(generate_list_for_padding_check(2))

'''

# for i in range(0, 256):
#     guess = hex(i)
#     guess = guess.replace("0x", "")
#     if len(guess) < 2:
#         guess = "0" + guess
#     print(guess)


def xor_this(a_str, b_str):
    a_hex = int(a_str, 16)
    b_hex = int(b_str, 16)
    result = hex(a_hex ^ b_hex)
    result_str = str(result)
    result_str = result_str.replace("0x", "")

    if len(result_str) < 2:
        result_str = ("0" + result_str)
    print(result_str)
    return result_str


# print(generate_list_for_padding_check(5))

# xor_this("01", "04")

x = ['01', '02', '03']

# print(x[1])


l = ['\n', 'i', 'n', 's', 't', 'a', 'g', 'r', 'a', 'm', ':', 'c', 's', '2', '1', '0', '7', ':', 'n', 'o', 't', 't', 'h', 'e', 'f', 'l', '4', 'g', '\n', 'r', 'e', 'd', 'd', 'i', 't', ':', 'c', 's', '2', '1', '0', '7', ':', 'n', 'o', 't', 't', 'h', 'e', 'f', 'l', 'l', '4', 'g', '\n', 't', 'w', 'i', 't', 't', 'e', 'r', ':', 'c', 's', '2', '1', '0', '7', ':', 'n', 'o', 't', 't', 'h', 'e', 'f', 'l', '4', 'g']
l_hex = []

for a in l:
    print(int(a, 256))
    # l_hex.append(hex(a))
    # print(hex(a))

'''

hex_list = [['30', '37', '3a', '6e', '6f', '74', '74', '68', '65', '66', '6c', '34', '67', '01', '02', '03'],
            ['6c', '34', '67', '0a', '74', '77', '69', '74', '74', '65', '72', '3a', '63', '73', '32', '31'],
            ['74', '3a', '63', '73', '32', '31', '30', '37', '3a', '6e', '6f', '74', '74', '68', '65', '66'],
            ['6e', '6f', '74', '74', '68', '65', '66', '6c', '34', '67', '0a', '72', '65', '64', '64', '69'],
            ['6e', '73', '74', '61', '67', '72', '61', '6d', '3a', '63', '73', '32', '31', '30', '37', '3a'],
            ['53', '5f', '37', '30', '5f', '79', '30', '55', '72', '73', '33', '4c', '46', '7d', '0a', '69'],
            ['75', '52', '5f', '33', '72', '72', '30', '72', '5f', '6d', '33', '53', '73', '34', '47', '33'],
            ['37', '3a', '63', '73', '32', '31', '30', '37', '7b', '6b', '33', '33', '70', '5f', '59', '30']]
coun = 0
for l in hex_list:
    result = "block " + str(coun) + ": "
    for a in l:
        result += chr(int(a,16))
    print(result)
    print("")
    coun += 1