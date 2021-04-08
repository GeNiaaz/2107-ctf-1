import requests
from bs4 import BeautifulSoup

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

determine_block_length()

s.close()

