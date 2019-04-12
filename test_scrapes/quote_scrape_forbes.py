# forbes use JS to store their data
# Can use selenium to scrape JS
# below is the link that show how to use selenium and xpath to do that
# https://stackoverflow.com/questions/8049520/web-scraping-javascript-page-with-python

# Seleniunm docs:
# https://selenium-python.readthedocs.io/locating-elements.html

def forbes_scrape(filename):
    from selenium import webdriver
    from selenium.webdriver.common.by import By
    driver = webdriver.Chrome()
    driver.get(filename)
    t_element = driver.find_element_by_xpath(By.XPATH, '//script[@type="text/javascript"]')
    print(t_element.text)

forbes_scrape('https://www.forbes.com/sites/kevinkruse/2013/05/28/inspirational-quotes/#513d19c06c7a')