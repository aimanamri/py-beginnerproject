from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

driver_PATH = r'C:\Users\User\Desktop\py_project\chromedriver.exe'  #change ur chrome driver PATH here
driver = webdriver.Chrome(executable_path = driver_PATH)

driver.maximize_window()
driver.delete_all_cookies()

urls = ["https://www.bbc.com/news",
        "https://www3.nhk.or.jp/news/special/coronavirus/data/",
        "http://covid-19.moh.gov.my/terkini-negeri"]


for posts in range(len(urls)):
    print(posts)
    driver.get(urls[posts])    
    if(posts!=len(urls)-1):
       driver.execute_script("window.open('');")
       chwd = driver.window_handles
       driver.switch_to.window(chwd[-1])

time.sleep(2)
hour = 0.5
refresh_time_in_seconds = hour  * 3600

# ---------uncomment this line if want to switch between tabs every xx seconds---
# while True:
#     Windows = driver.window_handles
#     for window in Windows:
#         driver.switch_to.window(window)
#         time.sleep(refresh_time_in_seconds)
    
 # -----------------------------------------------------------------------------   
# (p/s : only run one while True loop at at time. You cant run both)
# ---------uncomment this line if want to refresh every xx seconds--------------
while True:
    time.sleep(refresh_time_in_seconds)  
    Windows = driver.window_handles
    for window in Windows:
        driver.switch_to.window(window)
        driver.refresh()
# -----------------------------------------------------------------------------

# ---------to prevent program from stop running----------------maybe not working because while true loop still running
hour = 1.5  # <--- set time in hour here
time.sleep(hour*3600)

#  you can move to specific handle    
chwd = driver.window_handles
print(chwd)