if __name__ == '__main__':

    list = ["", "-", "_"]
    num = 0
    num2 = 0
    with open('1_word_combi.txt') as file:
        text = file.readlines()

    with open('4_word_combi.txt', 'w') as f:
        for line1 in text:
            num2 += 1
            for line2 in text:
                print(num2, "/86  ", num, "/ 86")
                num += 1
                for line3 in text:
                    for line4 in text:
                        for x in list:
                            for y in list:
                                for z in list:
                                    f.write(line1[:-1] + x + line2[:-1] + y + line3[:-1] + z + line4)

        

