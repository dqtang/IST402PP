from selenium import webdriver

browser = webdriver.Firefox()

#Set local host.
browser.get('http://localhost:8000')


#Set List title
assert 'Class Requirement List' in browser.title


#Close Browser.
browser.quit()

