from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time


options = webdriver.ChromeOptions()
# options.add_argument("user-data-dir-"+ acc)
options.add_experimental_option('detach',True)
service = Service(executable_path="./chromedriver.exe")

f1 = open("C:\\Users\\MTQV\\Desktop\\Python Program\\tool_check_live_mail\\hotmail.txt","r")
accs = f1.read().split("\n")
f1.close()
print(accs)

for acc in accs:
    driver = webdriver.Chrome(options=options,service=service)
    driver.get("https://login.live.com/")
    time.sleep(5)
    info = acc.split("|")
    print(info)
    user = info[0]
    passw = info[1]
    
    driver.find_element(By.ID,value='i0116').send_keys(user)
    time.sleep(5)
    driver.find_element(By.ID,value='idSIButton9').click()
    time.sleep(5)

    driver.find_element(By.ID,value='i0118').send_keys(passw)
    time.sleep(5)
    driver.find_element(By.ID,value='idSIButton9').click()
    time.sleep(5)

    driver.quit()
    if driver.current_url.find("https://login.live.com/"):
        f2 = open("C:\\Users\\MTQV\\Desktop\\Python Program\\tool_check_live_mail\\mail_pass_check.txt","a")
        f2.write(acc)
        f2.close()
    
    
