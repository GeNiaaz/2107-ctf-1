import requests
from bs4 import BeautifulSoup
from string import printable

# 14 yields 928

url = "http://ctf.nus-cs2107.com:2772/"

s = requests.session()

block_size = 32


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


old_data = list("coursemology:c")
known_data = []
counter = 0
block_number = 1

start_block_gap = 14
info = {
    "creds": "A" * start_block_gap,
}
r = s.get(url)
r = s.post(url, data=info)
soup = BeautifulSoup(r.content, 'html.parser')
token = soup.find('p', id="new-creds").text
token_length = len(token)
blocks_original = get_blocks(token)

# block_should_be = blocks_original[block_number]
# print(block_should_be)

while True:
    while counter < 15:
        info = {
            "creds": "A" * start_block_gap,
        }
        r = s.get(url)
        r = s.post(url, data=info)
        soup = BeautifulSoup(r.content, 'html.parser')
        token = soup.find('p', id="new-creds").text
        token_length = len(token)
        blocks_original = get_blocks(token)
        block_should_be = blocks_original[block_number]
        counter += 1
        for c in (chr(i) for i in range(33, 127)):
            print("counter:", counter)
            print("block num:", block_number)
            print("trying character", "".join(known_data) + " " + c)
            print("data so far:", "".join(old_data))
            # print("\n")
            info = {
                "creds": "".join(old_data) + "A" * start_block_gap + "\n" + "".join(known_data) + c,
            }
            r = s.get(url)
            r = s.post(url, data=info)
            soup = BeautifulSoup(r.content, 'html.parser')
            token = soup.find('p', id="new-creds").text
            token_length = len(token)
            blocks = get_blocks(token)
            # print("\n".join(blocks))
            if blocks[block_number] == block_should_be:
                print("WE GOT A HIT!!!")
                print("CHARACTER WINNER:", c)
                known_data.append(c)
                old_data.append(c)
                print(blocks[block_number])
                start_block_gap -= 1
                break
    counter = 0
    start_block_gap = 14
    block_number += 1
    known_data = []

# determine_block_length()

s.close()
