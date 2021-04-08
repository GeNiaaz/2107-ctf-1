import random


alphabet = r"abcdefghijklmnopqrstuvwxyz+-_0123456789{}"

def encrypt(message: str):
    random.seed(2107)
    acc = []
    for letter in message:
        shift = random.randint(0, len(alphabet))
        new_index = (alphabet.index(letter) + shift) % len(alphabet)
        acc.append(alphabet[new_index])

    return "".join(acc)

def decrypt(input: str):
    random.seed(2107)
    ans = ""
    length = len(alphabet)
    counter = 0
    for letter in input:
        ran = random.randint(0, length)
        result = alphabet.index(letter)

        for i in range(0, 100):
            temp = result + i * length - ran
            if - 1 < temp < length:
                ans += alphabet[temp]
                break
            else:
                ...
    return ans



if __name__ == "__main__":
    with open('flag.txt') as file:
        flag = file.read().strip()
    ct = decrypt(flag)
    print(ct)

