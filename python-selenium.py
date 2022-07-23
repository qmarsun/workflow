
def firefix_driver():
    driver = webdriver.Firefox()
    driver.get("http://www.python.org")
    assert "Python" in driver.title
    elem = driver.find_element(By.NAME, "q")
    elem.clear()
    elem.send_keys("pycon")
    elem.send_keys(Keys.RETURN)
    assert "No results found." not in driver.page_source
    driver.close()


def using_svc():
    import time
    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service
    sel_driver=r'C:\\workarea\\chromedriver'
    service = Service(sel_driver)
    service.start()
    driver = webdriver.Remote(service.service_url)
    driver.get('http://www.google.com/');
    time.sleep(5) # Let the user actually see something!
    driver.quit()

def using_zoho():
    import time
    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service
    sel_driver=r'C:\\workarea\\chromedriver'
    service = Service(sel_driver)
    service.start()
    driver = webdriver.Remote(service.service_url)
    time.sleep(2)
    driver.get('https://api-console.zoho.com/');
    time.sleep(5) # Let the user actually see something!
    #adriver.quit()


def setup_driver():
    sel_driver=r'C:\\workarea\\geckodriver'
    driver = webdriver.Chrome(sel_driver)  
    print(driver)
    # Optional argument, if not specified will search path.
    driver.get('http://www.google.com/');

    time.sleep(5) # Let the user actually see something!
    search_box = driver.find_element_by_name('q')

    search_box.send_keys('ChromeDriver')

    search_box.submit()

    time.sleep(5) # Let the user actually see something!

    driver.quit()

using_zoho  ()
