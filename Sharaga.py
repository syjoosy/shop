from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
# import re
import os.path
# import pyautogui
# import requests, bs4
import time

def write_settings():
    if os.path.exists("settings.txt") == False:
        # file = open('settings.txt', 'w', encoding="utf-8", errors='ignore')
        # name = input("Имя, которое будет отображаться в Mind(Настраивается 1 раз): ")
        # file.write(name)
        return 0

test = write_settings()

with open('settings.txt') as file:
    name = file.readlines()
    mind_name = name[0]
    if test != 0:
        mind_name = mind_name[0:-1]
    # print(name)
    # name[0] = name[0:-2]
    # print(name)

print("Имя, которое будет отображаться в Mind: ", mind_name)

driver = webdriver.Firefox()
driver.get('http://studydep.miigaik.ru/semestr/index.php')

# with open('text.txt') as file:
#     lines = file.readlines()



#Выбор факультета, курса, группы

# time.sleep(2)
select = Select(driver.find_element_by_xpath('/html/body/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr/td/form/table/tbody/tr[1]/td[2]/select'))
select.select_by_visible_text("факультет прикладной космонавтики и фотограмметрии")
# select.click()
# elem = driver.find_element_by_xpath('/html/body/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr/td/form/table/tbody/tr[1]/td[2]/select')
# elem.click()
# time.sleep(1)
# elem.select_by_visible_text('факультет прикладной космонавтики и фотограмметрии')
# for i in range(6):
#     elem.send_keys(Keys.DOWN)
# elem.send_keys(Keys.RETURN)
# dataset_drop_down_element = WebDriverWait(driver, 20).until(elem.element_to_be_clickable(('body > table > tbody > tr > td:nth-child(2) > table > tbody > tr:nth-child(4) > td > table > tbody > tr > td:nth-child(2) > table > tbody > tr > td > form > table > tbody > tr:nth-child(1) > td:nth-child(2) > select')))
# dataset_drop_down_element = Select(dataset_drop_down_element)
# elem.click()

# elem = driver.find_element_by_css_selector('body > table > tbody > tr > td:nth-child(2) > table > tbody > tr:nth-child(4) > td > table > tbody > tr > td:nth-child(2) > table > tbody > tr > td > form > table > tbody > tr:nth-child(2) > td:nth-child(2) > select')
# elem.click()
# for i in range(3):
#     elem.send_keys(Keys.ARROW_DOWN)
# elem.click()

select = Select(driver.find_element_by_xpath('/html/body/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr/td/form/table/tbody/tr[2]/td[2]/select'))
select.select_by_visible_text('3')

select = Select(driver.find_element_by_xpath('/html/body/table/tbody/tr/td[2]/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr/td/form/table/tbody/tr[3]/td[2]/select'))
select.select_by_visible_text("ИСиТ III-1б")



#Определение недели, дня, пары, взятие ссылки на вебинар

weekElem = driver.find_element_by_css_selector('body > table > tbody > tr > td:nth-child(2) > table > tbody > tr:nth-child(4) > td > table > tbody > tr > td:nth-child(1) > table > tbody > tr:nth-child(3) > td > p:nth-child(1) > strong').text  #взятие недели, даты, дня недели
DateInfo = weekElem.split('\n')
Date = DateInfo[0]
Day = DateInfo[1]
Week = DateInfo[2]

elem = driver.find_element_by_css_selector('body > table > tbody > tr > td:nth-child(2) > table > tbody > tr:nth-child(4) > td > table > tbody > tr > td:nth-child(2) > table > tbody > tr > td > table.t > tbody > tr:nth-child(3)')
#print(Date, Day, Week)


lesson = driver.find_element_by_class_name('t')   # выбор таблицы с расписанием
lesson.find_elements_by_xpath("//*[contains(text(), 'https://vcs.imind.ru')]")     # выбор строк, содержащих расписание
#print(lesson.text)

f = open('text.txt', 'w')
test = str(lesson.text)
test.split('\n')
f.write(test)
# print(test)
f.close()



# Убираем из файла всю лишнюю инфу, кроме ссылок

# with open('text.txt', 'r') as file:
#     for line in file:
#         for day in week:
#             if day in line == True:
#                 line = line.replace('\n','')


# with open('text.txt') as file:
#     lines = file.readlines()
#
# str = 'Понедельник'
# pattern = re.compile(re.escape(str))
# with open('text.txt', 'w') as file:
#     for line in lines:
#         result = pattern.search(line)
#         if result is None:
#             file.write(line)

file = open("text.txt", "r")
lines = file.readlines()
file.close()

# file = open("text.txt", "w")
# for line in lines:
#   if "Понедельник " in line == False:
#     file.write(line)
# file.close()

week = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота"]

# print(lines)
str = 'https://vcs.imind.ru/'
file = open("text.txt", "w")
# i = 1
sep = ' '
# for day in week:
for line in lines:
    if line.find(str) >= 0:
        # file.write(line)
        index = line.index("h")
        line = line[:0] + line[index:]
        line = line.split(sep, 1)[0]
        line = line + "\n"
        file.write(line)
        # print(str, ' найдено, на строке ', i)
    # i += 1
file.close()

#Берем ссылку из файла и открываем ее
with open('text.txt', 'r') as file:
    nums = file.read().splitlines()
link = nums[0]
driver.get(link)
# driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.TAB)
time.sleep(2)
input = driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/div[5]/div[3]/div/div[3]/div/div[2]/div[1]/div[3]/div[3]/div/div[2]/div/div/div[3]/div/div[2]/div/div/div[9]/div/div[1]/div/div/div[3]/div[1]/div/div/input")
# input = driver.find_element_by_class_name("mind-textbox-content")
input.click()
# input.clear()
# time.sleep(1)
# ok_button = driver.find_element_by_xpath("/html/body/div[8]/div/table/tbody/tr[2]/td[2]/div/div/div/div/div[3]/div/div/div/div/table/tbody/tr/td[1]/div/div/div/table/tbody/tr/td[2]/div")
# ok_button.click()
# print("Нажал кнопку")
# time.sleep(1)
# print("Подождал")
# fra = driver.find_element_by_tag_name('tbody')
# driver.switch_to.frame('c6bb9b57-8fa0-415d-92fb-668f81795675')
# ok_button.click()
# print("Нажал кнопку")
for i in range(4):
    input.send_keys(Keys.BACKSPACE)
input.send_keys(mind_name)
for i in range(len(mind_name)):
    input.send_keys(Keys.ARROW_LEFT)
input.send_keys(Keys.BACKSPACE)
# button = driver.find_element_by_class_name("mind-button-text")
button = driver.find_element_by_xpath("/html/body/div[4]/div[2]/div/div[5]/div[3]/div/div[3]/div/div[2]/div[1]/div[3]/div[3]/div/div[2]/div/div/div[2]/div/div/div/div/table/tbody/tr/td[2]/div")
button.click()