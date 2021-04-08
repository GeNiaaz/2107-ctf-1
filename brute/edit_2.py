if __name__ == '__main__':

    with open('1_word_combi.txt') as file:
        text = file.readlines()

    with open('2_word_combi.txt', 'w') as f:
        for line1 in text:
            for line2 in text:
                f.write(line1[:-1] + line2)
                f.write(line1[:-1] + "-" + line2)
                f.write(line1[:-1] + "_" + line2)

        

