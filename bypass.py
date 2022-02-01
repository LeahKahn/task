import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

s = Service('E:/SEM 6/neuron/chromedriver.exe')
op = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=s, options=op)


driver.get('https://safebrowsing.google.com/safebrowsing/report_phish/Captcha')

time.sleep(1)

datas = [['http://mediocre.com', 'It says mediocre and I do not like it']]

for data in datas:
    count = 0
    textboxes = driver.find_elements(By.XPATH, '//input[@id="url"]')
    textareaboxes = driver.find_elements(By.XPATH, '//textarea[@id="dq"]')

    for value in textboxes:
        value.send_keys(data[count])
        count += 1

    time.sleep(1)
    driver.minimize_window()
    time.sleep(1)
    driver.find_element(By.XPATH, '//div[@id="header"]')
    time.sleep(2)

    for value in textareaboxes:
        value.send_keys(data[count])
        count += 1
    driver.maximize_window()
    time.sleep(2)

    frames = driver.find_elements(By.XPATH, '//iframe')
    driver.minimize_window()
    time.sleep(6)
    driver.maximize_window()

    options = webdriver.ChromeOptions()
    options.add_argument("start-maximized")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it(
        (By.CSS_SELECTOR, "iframe[name^='a-'][src^='https://www.google.com/recaptcha/api2/anchor?']")))
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[@id='recaptcha-anchor']"))).click()

    # click on submit button
    # WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//input[@type='submit' and @value='Confirmar']"))).click()
    submit = driver.find_element(By.XPATH, '//*[@type="submit"]')
    submit.click()