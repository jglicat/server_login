from selenium import webdriver
import time
import random
import pyotp


# 全局等待时间变量，网络或者电脑太卡就调大点
time1 = 0
time2 = 1


def click_botton(name, xpath, driver, times=1, j=0):
    for i in range(10):
        try:
            driver.find_elements_by_xpath(xpath)[j].click()
            print("第" + str(i + 1) + "次点击'" + name + "'成功")
            time.sleep(random.uniform(time1 + times + i, time2 + times + i))
            break
        except Exception as e:
            if (i == 9):
                print(name + "失败，结束运行")
                raise
            else:
                print("第" + str(i + 1) + "次点击'" + name + "'失败")
                time.sleep(random.uniform(
                    time1 + times + i, time2 + times + i))


def send_text(name, xpath, driver,  text, times=1, j=0):
    for i in range(10):
        try:
            driver.find_elements_by_xpath(xpath)[j].send_keys(
                text)
            print("第" + str(i + 1) + "次填写'" + name + "'成功")
            time.sleep(random.uniform(time1 + times + i, time2 + times + i))
            break
        except Exception as e:
            if (i == 9):
                print(name + "失败，结束运行")
                raise
            else:
                print("第" + str(i + 1) + "次填写'" + name + "'失败")
                time.sleep(random.uniform(
                    time1 + times + i, time2 + times + i))


if __name__ == '__main__':
    username = ''
    pwd = ''
    key = ''
    topt = pyotp.TOTP(key)
    driver = webdriver.Chrome()
    driver.get('http://10.128.202.17/')
    click_botton('高级', "//button[contains(text(),'%s')]" % ('高级'), driver)
    click_botton('继续前往', "//a[contains(text(),'%s')]" %
                 ('继续前往10.128.202.17（不安全）'), driver)
    send_text('userName', "//input[@id='userName']", driver,  username)
    send_text('pwd', "//input[@id='pwd']", driver,  pwd)
    click_botton('登录', "//input[@id='btn_log']", driver)
    send_text('otp', "//input[@id='dyncodetext']", driver, topt.now())
    click_botton('登录', "//input[@id='btn_log']", driver)
    input()
