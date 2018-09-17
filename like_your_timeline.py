import sys
import traceback
import codecs
import time
from selenium import webdriver
from getpass import getpass
from pyvirtualdisplay import Display
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

sys.stdout = codecs.getwriter('utf8')(sys.stdout)
sys.stderr = codecs.getwriter('utf8')(sys.stderr)

def execute_liking(username, password, driver):

    driver.implicitly_wait(1)
    
    username_field = driver.find_element_by_class_name("js-username-field")
    password_field = driver.find_element_by_class_name("js-password-field")

    username_field.send_keys(username)
    password_field.send_keys(password)

    driver.find_element_by_class_name("EdgeButtom--medium").click()

    driver.implicitly_wait(10)

    """
    Give some time for page to load
    """
    time.sleep(10)
    
    print("Login OK")
    
    """
    Find all 'Favorite' button on the current visible page    
    """
    elements = driver.find_elements_by_css_selector(".ProfileTweet-actionButton.js-actionButton.js-actionFavorite")
    
    print("Found " + str(len(elements)) + " clickable heart buttons")

    """
    Useful for debugging
    """
    driver.save_screenshot("t.png")

    num_success = 0

    for e in elements:
        try:
            WebDriverWait(driver, 10).until(EC.visibility_of(e))
            
            """
            element for the whole tweet 
            """
            content_element = e.find_element_by_xpath("../../../..")           
 
            driver.execute_script("arguments[0].scrollIntoView();", e)
            
            """
            Involving Javascript is hacky, but it is a workaround to get rid of unclickable errors
            """
            driver.execute_script("arguments[0].click();", e)
            
            fullname = content_element.find_element_by_css_selector(".fullname.show-popup-with-id.u-textTruncate")
            print("clicked like for " + fullname.text)

            num_success += 1
            time.sleep(1)
        except Exception as e:
            traceback.print_exc()

    print("Successfully clicks: " + str(num_success))

if __name__ == "__main__":

    with open('username', 'r') as myfile:
        username = myfile.read().replace('\n', '')

    print("Using username: " + username)

    with open('password', 'r') as myfile:
        password = myfile.read().replace('\n', '')

    display = Display(visible=0, size=(1024, 2048))
    display.start()

    driver = webdriver.Firefox()
    driver.set_window_position(0, 0)
    driver.set_window_size(1024, 768)
    driver.get("https://twitter.com/login")

    try:
        execute_liking(username, password, driver)
    except Exception as e:
        traceback.print_exc()
    finally:
        driver.quit()
        display.stop()
