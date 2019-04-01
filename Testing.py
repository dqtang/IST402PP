from selenium import webdriver


browser = webdriver.Firefox()
#Danny wants a list to manage the courses he requires for his major.
#He goes to this website that he heard from his senior to help manage his course.
browser.get('http://localhost:8000')

#Danny saw the title of the website and knows he is on the right site.
assert 'Course Management List' in browser.title


#1) He saw a textbox for him to enter his course.

#2) He press the enter key and saw the list updated. Adding his course to the list

#3) He noticed that there is options next to his course list that sets it to done or in-progress. 

#4) When Danny selected done, a green text that says "Done" pops up next to the course.

#5) If he select "In-Progress" a yellow text pops up that says "In-Progress"

#6) Excited he wonders if the list will save and be used later on.


#Close Browser.
browser.quit()

