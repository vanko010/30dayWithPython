import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys

# Specify the path to chromedriver.exe
driver = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver')

# Truy cập trang web
driver.get("https://support.pavietnam.vn")

email = driver.find_element(By.XPATH, "//input[@id='username']")
pw = driver.find_element(By.XPATH, "//input[@id='matkhau']")
login = driver.find_element(By.XPATH, "//body/div[1]/div[1]/div[2]/div[1]/div[5]/div[1]/form[1]/input[2]")

email.send_keys("vule@pavietnam.vn")
pw.send_keys("16112001@Aii")
login.click()

try:
    textlogin2 = driver.find_element(By.XPATH, "//div[contains(text(),'BẰNG TÀI KHOẢN 2')]")
    if textlogin2:
        email2 = driver.find_element(By.XPATH, "//input[@id='username']")
        pw2 = driver.find_element(By.XPATH, "//input[@id='matkhau']")
        login2 = driver.find_element(By.XPATH, "//body/div[1]/div[1]/div[2]/div[1]/div[5]/div[4]/form[1]/input[1]")
        email2.send_keys("2")
        pw2.send_keys("nvpacukhoi750suvanhanh")
        login2.click()
        print("Tôi là nhân viên")
except Exception as e:
    print("Tôi là khách hàng")

driver.close()
