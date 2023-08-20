from time import sleep
from fake_useragent import UserAgent
from webdriver_manager.chrome import ChromeDriverManager


from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver



def turn_on_the_browser():

    service=Service(ChromeDriverManager().install())
    
    options=Options()
    #options.add_argument(f"user-agent={user_agent}")
    driver=webdriver.Chrome(service=service, options=options)
    driver.maximize_window()
    return driver



def scrollin(driver,scrolls=1,  script="window.scrollBy(0,1961)"):
    scrolls=range(scrolls)
    for scroll in scrolls:
        driver.execute_script(script)
        sleep(2)
        
        
        
