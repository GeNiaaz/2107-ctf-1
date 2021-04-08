import requests
from bs4 import BeautifulSoup
from string import printable

# 14 yields 928

url = "http://ctf.nus-cs2107.com:2772/"

s = requests.session()

block_size = 16


def get_blocks(token):
    new = []
    for i in range(0, len(token), block_size):
        new.append(token[i:i+block_size])
    return new


def determine_block_length():
    token_length = 896
    while token_length == 896:
        for i in range(1, 20):
            content = "a" * i
            content_length = len(content)

            info = {
                "creds": content,
            }

            r = s.get(url)
            r = s.post(url, data=info)
            soup = BeautifulSoup(r.content, 'html.parser')
            token = soup.find('p', id="new-creds").text
            token_length = len(token)
            print("content length:", content_length, "|| Token length:", token_length)
            print("\n".join(get_blocks(token)))
            print("=" * 34)
            if token_length != 896:
                break

counter = 12
known_data = list("coursemology:cs2107:")
str_so_far = ""
original_data_list = []
original_data = "0528f8f97e1a90807bc8d39d84a0aafdfae15b56c7d251d603c7e942e7a80f14f898d26d4a030254b4d508f00d8943cde30c96709a89d83d45386ca0e0c9eead703736bc1c2625ba3ef6ce58b8aa96838a63a327e3f8c791235d667d3119d19b24da867b5e7498c95ad64efe9b767097fae15b56c7d251d603c7e942e7a80f14f898d26d4a030254b4d508f00d8943cd0dc4f8594153840f5eed493c72322d87304aa63778e0a4239a8e5d06c39a866d469c1f0fd3faf1cd99037b28fbcdd76759d6ac6619405c3fcb3acff245f7648efae15b56c7d251d603c7e942e7a80f14f898d26d4a030254b4d508f00d8943cdc82069716293acca8d0d492bb0233af0fae15b56c7d251d603c7e942e7a80f14f898d26d4a030254b4d508f00d8943cd6b03f98d316e26cb12f1d27b8c24dd80dd79ca5cff4f0f565d71c801cf330997a957443c67e85cf1da714f0047158fbf18b4582046d80d503229b09442895f47c575f32951eeaba0c863376fbe0bb6b5bbf7e9fb447b1b6a695a0261ac2f737c7115678f949cc97e8bc86b42a72946bec575f32951eeaba0c863376fbe0bb6b5bbf7e9fb447b1b6a695a0261ac2f737c52c8dbe96db2e34817d5c75ccff41572"
for i in range(0, len(original_data), 16):
    original_data_list.append(original_data[i:i+16])

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

while True:
    prev_char = "1"
    for c in (chr(i) for i in range(33, 127)):
        print("trying character", "".join(known_data), c)
        info = {
            # "creds": "a" * start_block_gap + c + "\n",
            "creds": "".join(known_data) + c,
        }
        r = s.get(url)
        r = s.post(url, data=info)
        soup = BeautifulSoup(r.content, 'html.parser')
        token = soup.find('p', id="new-creds").text
        token_length = len(token)
        blocks = get_blocks(token)
        print("block:", blocks[1])
        # print("\n".join(blocks))
        if blocks[1] == original_data_list[1]:
            print("WE GOT A HIT!!!")
            print("CHARACTER WINNER:", c)
            known_data.append(prev_char)
            break
        prev_char = c

# determine_block_length()

s.close()
