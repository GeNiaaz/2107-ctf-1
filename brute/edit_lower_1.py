if __name__ == '__main__':

    with open('1-word.txt') as file:
        text = file.readlines()

    with open('lower_1.txt', 'w') as f:
        for line in text:
            f.write(line.lower())
        

