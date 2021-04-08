if __name__ == '__main__':

    list = ["", "-", "_"]
    with open('1_word_combi.txt') as file:
        text = file.readlines()

    with open('3_word_combi.txt', 'w') as f:
        for line1 in text:
            for line2 in text:
                for line3 in text:
                    for x in list:
                        for y in list:
                            f.write(line1[:-1] + x + line2[:-1] + y + line3)

        

