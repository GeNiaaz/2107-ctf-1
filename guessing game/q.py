from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('http://ctf.nus-cs2107.com:2774/')

searchbox = driver.find_element_by_xpath('//*[@id="guess"]')
seachButton = driver.find_element_by_xpath('//*[@id="submit"]')

def check_correct():
    live_score = driver.find_element_by_xpath('//*[@id="score"]').text[0]
    if int(live_score) > 0:
        return True 
    else:
        return False

def finished():
    live_score = driver.find_element_by_xpath('//*[@id="score"]').text[0]
    if int(live_score) == 1:
        second_num = driver.find_element_by_xpath('//*[@id="score"]').text[1]
        if second_num == "0":
            return True
        else:
            return False
    else:
        return False

input_nums = ['4','8','5','9','8','6','4','6','0','4']
guess_number = 0
not_finished = True
score_so_far = 0
highest_so_far = 0
while True:
    searchbox.send_keys(input_nums[score_so_far])
    seachButton.click()
    guess_number += 1
    time.sleep(0.05)
    print("Guess:", guess_number, "| Input:", input_nums[score_so_far], "| Score:", score_so_far, "/ 10", ">> highest:", highest_so_far)
    searchbox.clear()

    if score_so_far > highest_so_far:
        highest_so_far = score_so_far

    if check_correct():
        score_so_far += 1
        if finished():
            print("finished")
            break
        else:
            continue
    else:
        score_so_far = 0
        continue