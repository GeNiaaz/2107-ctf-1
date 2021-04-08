import requests
from bs4 import BeautifulSoup
from string import printable

# 14 yields 928

url = "http://178.128.91.141:8005"

s = requests.session()


list_of_possible_guesses = []
for i in range(0, 256):
    guess = hex(i)
    guess = guess.replace("0x", "")
    if len(guess) < 2:
        guess = "0" + guess
    list_of_possible_guesses.append(guess)


def xor_long_string(a, b):
    length = len(a)
    result = ""
    for i in range(0, length, 2):
        result += xor_this(a[i:i+2], b[i:i+2])
    return result


def xor_this(a_str, b_str):
    a_hex = int(a_str, 16)
    b_hex = int(b_str, 16)
    result = hex(a_hex ^ b_hex)
    result_str = str(result)
    result_str = result_str.replace("0x", "")

    if len(result_str) < 2:
        result_str = ("0" + result_str)
    return result_str


# generates list(01, 02, 03, 04...)
def generate_list_for_padding_check(n):
    result_list = []
    for i in range(2, n + 1):
        num_hex = hex(i)
        num_str = str(num_hex)
        num_str = num_str.replace("0x", "")
        if len(num_str) < 2:
            num_str = "0" + num_str
        result_list.append(num_str)

    return result_list


def get_blocks(token):
    new = []
    for i in range(0, len(token), block_size):
        new.append(token[i:i+block_size])
    return new


def check_result(iv, c):
    to_join = iv + c
    info = {
        "data": to_join,
    }
    r = s.get(url)
    r = s.post(url, data=info)
    soup = BeautifulSoup(r.content, 'html.parser')
    result_message = soup.find('p', id="result").text
    print("output:", result_message)
    if result_message == "Successful!":
        return True
    else:
        return False


# xor 2 lists to xor iv
def xor_lists(a, b):
    result = []
    for i in range(len(a)):
        elem = xor_this(a[i], b[i])
        result.append(elem)
    return result


def change_iv_n_character(iv, guess, n, block_list_padding):
    iv = iv[-(n * 2)]
    chars_to_add = "".join(block_list_padding)
    iv += guess + chars_to_add
    return iv


# ls = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']

block_size = 32
input_data = "ea437fdd5cc90c5b8c329188ee265bebb65ac04d86b81eb29459104dd893c396a10c1b8c336ffcb0277fa196a9bf69ccd4d665d12e2db5f15286d9fe8ab8d9f2c7a2d907f198a0de0ea8a42f967b3e964e47a5809f7de611f494ab00e51624f38e78844cd4377c6d36f209a5c4fb9a4c08177e94fe56c398586a9ecdcc05fdc4ef1a1e712f58ccbd51bd42c00bfcaa96dfb0a1d8559c6f8761c18c61999747a5c2f81e74fa320ee0aea1d4943d2224208a78bdeea66379ed7968cdd484bfe1bb48fe93e153fff5bf95315a2ebb44c218c29c723f85c6e8718a15fde76da89252f6b9344669e4a277a31c535b52649166f3b98867a7177a2aca7a59bc089ab42609e198047b4d80eb4b13731cb8ab6777"
input_data_list = []
for i in range(0, len(input_data), block_size):
    input_data_list.append(input_data[i:i+block_size])

# iv = input_data_list[-2]
# c = input_data_list[-1]

plain_text = ['01', '02', '03']
# temp_list_items = ['01', '02', '03', '04', '05']

# WRITE CODE HERE  >>>>>>>>>>>>>>>
iv = input_data_list[-2]
c =  input_data_list[-1]

counter = 4
while counter < 17:
    list_padding_check = generate_list_for_padding_check(counter)
    for g in list_of_possible_guesses:
        # if counter == 0:
        #     expected_padding = "00" * 15 + g
        # else:
        end_list_padding = xor_lists(plain_text, list_padding_check)
        expected_padding = "00" * (16 - counter) + g + "".join(end_list_padding)
        new_iv = xor_long_string(expected_padding, iv)
        print("  padd:", expected_padding)
        print("    iv:", iv)
        print("new iv:", new_iv)
        print("     c:", c)
        print("pt so far:", plain_text)
        if check_result(new_iv, c):
            t = xor_this("01", g)
            print("CORRECT!! guess", g)
            plain_text.insert(0, t)
            print(plain_text)
            break
        else:
            print("wrong guess", g)
    counter += 1
    # counter += 1


# list_to_xor_with_iv = ['00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00', '00']

    # create items to xor with iv
# to_xor_ = xor_lists(plain_text, temp_list_items)
# iv = change_iv_n_character(iv, g, 4, list_padding_check)
# check_result(iv, c)

# for i in range(0,14):

# xor_temp = xor_long_string(temp, iv)


# ls = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']
# for x in range(0, 16):
#     for y in range(0, 16):
#         last_blk = input_data_list[-2]
#         temp = last_blk[:-2]
#         temp += ls[x]
#         temp += ls[y]
#         input_data_list[-2] = temp
#         print(input_data_list[-2])
#
#         info = {
#             "data": "".join(input_data_list),
#         }
#         r = s.get(url)
#         r = s.post(url, data=info)
#         soup = BeautifulSoup(r.content, 'html.parser')
#         token = soup.find('p', id="result").text
#         token_length = len(token)
#         # print("content length:", content_length, "|| Token length:", token_length)
#         print("last chars:", ls[x], ls[y], "output:", token)


# known_data = []
#
# start_block_gap = 15
# info = {
#     "creds": "a" * (start_block_gap + 1),
# }
# r = s.get(url)
# r = s.post(url, data=info)
# soup = BeautifulSoup(r.content, 'html.parser')
# token = soup.find('p', id="new-creds").text
# token_length = len(token)
# blocks = get_blocks(token)
#
# block_should_be = blocks[0]
# print(block_should_be)
#
# for c in printable:
#     print("trying character", c)
#     info = {
#         "creds": "a" * start_block_gap + c + "\n",
#     }
#     r = s.get(url)
#     r = s.post(url, data=info)
#     soup = BeautifulSoup(r.content, 'html.parser')
#     token = soup.find('p', id="new-creds").text
#     token_length = len(token)
#     blocks = get_blocks(token)
#     # print("\n".join(blocks))
#     if blocks[0] == block_should_be:
#         print("WE GOT A HIT!!!")
#         print("CHARACTER WINNER:", c)
#         known_data.append(c)
#         print(blocks[0])
# print("known data:", known_data)
# # determine_block_length()

s.close()
