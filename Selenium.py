from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time



PATH ="/Users/shawn/Desktop/chrome/chromedriver"
driver = webdriver.Chrome(PATH)

driver.get("https://techwithtim.net")

search = driver.find_elements_by_name("s")
search[0].send_keys("test") #put text in the search bar
search[0].send_keys(Keys.RETURN) #to ENTER


try:
    # waot until it search for test and do all the rest

    main = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.ID, "main"))
    )

    articles = main[0].find_elements_by_tag_name("article")
    print(articles)
    for article in articles:
        header = article.find_element_by_class_name("entry-summary")
        print(header.text)
finally:
    driver.quit()







#driver.close()
driver.quit()
