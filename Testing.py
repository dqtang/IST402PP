from selenium import webdriver
import unittest

class FIrstTestCase(unittest.TestCase):

    def startUp(self):
        self.browser = webdriver.Firefox()

def CloseBrowser(self):
    #Close Browser.
    self.browser.quit()



def FirstList(self):
    #Danny wants a list e manage the courses he requires for his major.
    #He goes to this website that he heard from his senior to help manage his course.
    self.browser.get('http://localhost:8000')
    #Danny saw the title of the website and knows he is on the right site.
    self.assertIn ('Course Management List', self.browser.title)
    self.fail('Testing Version Fail')  

#1) He saw a textbox for him to enter his course.



#2) He press the enter key and saw the list updated. Adding his course to the list

#3) He noticed that there is options next to his course list that sets it to done or in-progress. 

#4) When Danny selected done, a green text that says "Done" pops up next to the course.

#5) If he select "In-Progress" a yellow text pops up that says "In-Progress"

#6) Excited he wonders if the list will save and be used later on.

if __name__ == '__main__':  
    unittest.main(warnings='ignore') 