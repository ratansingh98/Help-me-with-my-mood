# Install Guide
"""
Check you have installed latest version of chrome browser-> "chromium-browser --version"
If not, install latest version of chrome "sudo apt-get install chromium-browser"
get appropriate version of chrome driver from here(http://chromedriver.storage.googleapis.com/index.html)
Unzip the chromedriver.zip
Move the file to /usr/bin directory "sudo mv chromedriver /usr/bin"
Goto /usr/bin directory "cd /usr/bin"
Now, you would need to run something like "sudo chmod a+x chromedriver" to mark it executable.
finally you can execute the code.

from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://www.google.com")
print driver.page_source.encode('utf-8')
driver.quit()
display.stop()
"""

import time
from selenium import webdriver
import random


def playSong(mood):
    driver = webdriver.Chrome()
    driver.get("https://soundcloud.com/search/sets?q={}".format(mood))
    randomNum = random.randint(1, 10)
    print(randomNum)
    cookie = driver.find_element_by_xpath(
        '//*[@id="app"]/div[1]/div/div/div/button')
    cookie.click()
    play = driver.find_element_by_xpath(
        '//*[@id="content"]/div/div/div[3]/div/div/div/ul/li[{}]/div/div/div/div[2]/div[1]/div/div/div[1]/a'.format(randomNum))
    play.click()

    while True:
        quitkey = str(input("Press y to quit\n"))
        if quitkey is "y":
            driver.quit()
            quit()
