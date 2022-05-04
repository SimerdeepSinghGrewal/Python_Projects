from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver_path = "C:\chromedriver.exe"

driver = webdriver.Chrome(driver_path)
driver.get(
    "https://www.linkedin.com/jobs/search/?f_AL=true&f_E=2&f_WT=2&geoId=103644278&keywords=python%20developer&location=United%20States")
time.sleep(3)
sign_in = driver.find_element(by=By.XPATH, value="/html/body/div[1]/header/nav/div/a[2]")
sign_in.click()
time.sleep(2)
user = driver.find_element(by=By.CSS_SELECTOR, value="div #username")
user.send_keys("LinkedIN_username")
password = driver.find_element(by=By.CSS_SELECTOR, value="div #password")
password.send_keys("LinkedIN_password")
signin = driver.find_element(by=By.XPATH, value='//*[@id="organic-div"]/form/div[3]/button')
signin.click()
time.sleep(5)


all_listings = driver.find_elements_by_css_selector(".job-card-container--clickable")

for listing in all_listings:
    print("called")
    listing.click()
    time.sleep(2)
    try:
        apply_button = driver.find_element_by_css_selector(".jobs-s-apply button")
        apply_button.click()

        time.sleep(5)
        phone = driver.find_element_by_class_name("fb-single-line-text__input")
        if phone.text == "":
            phone.send_keys(PHONE)
        
        submit_button = driver.find_element_by_css_selector("footer button")
        if submit_button.get_attribute("data-control-name") == "continue_unify":
            close_button = driver.find_element_by_class_name("artdeco-modal__dismiss")
            close_button.click()
            
            time.sleep(2)
            discard_button = driver.find_elements_by_class_name("artdeco-modal__confirm-dialog-btn")[1]
            discard_button.click()
            print("Complex application, skipped.")
            continue
        else:
            submit_button.click()

        time.sleep(2)
        close_button = driver.find_element_by_class_name("artdeco-modal__dismiss")
        close_button.click()

    except NoSuchElementException:
        print("No application button, skipped.")
        continue

time.sleep(5)