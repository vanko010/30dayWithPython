from selenium import webdriver

# Khởi tạo WebDriver Chrome
driver = webdriver.Chrome('C:/Users/doanv/Downloads/chrome-win64/chrome.exe')

# Hoặc có thể dùng forward slash
# driver = webdriver.Chrome('C:/Users/doanv/Downloads/chrome-win64/chromedriver.exe')

# Truy cập trang web
driver.get('https://www.example.com')

# Đóng trình duyệt sau khi hoàn thành
driver.quit()
