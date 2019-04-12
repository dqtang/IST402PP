from selenium import webdriver
import unittest
from selenium.webdriver.common.keys import Keys
import time


class FIrstTestCase(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        #Close Browser.
        self.browser.quit()

    def check_for_row_in_table(self, row_text):
        table = self.browser.find_element_by_id('Course_Table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

    def test_FirstList(self):
        #Danny wants a list e manage the courses he requires for his major.
        #He goes to this website that he heard from his senior to help manage his course.
        self.browser.get('http://localhost:8000')
        #Danny saw the title of the website and knows he is on the right site.
        self.assertIn ('Course Management', self.browser.title)
        header_text =  self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Your Course List', header_text)


    #1) He saw a textbox for him to enter his course.
        
        inputbox = self.browser.find_element_by_id('Course_Id')
        self.assertEqual(inputbox.get_attribute('placeholder'), 'Enter a Course') 

    #2) He enters a course as a test and press es the enter key and saw the list updated. Adding his course to the list
        #Still need to work on how to get user input Sprint 2
        
        inputbox.send_keys('History 101')

        #Testing phase allow time to enter info
        time.sleep(5)

        """
        Gets text from input box used for formating currently useless
        CourseAdding = inputbox.text
        """
        inputbox.send_keys(Keys.ENTER)
        
        time.sleep(5)

        """
        Sprint 2: Make it not Hardcoded 
        Sample: Currently Gives AssertionError from home.html
        self.check_for_row_in_table('1: {0}'.format(CourseAdding))
        """
                        
        # Will add Loop and Counter Later to enumerate itself
        self.check_for_row_in_table('1: History 101')
        
        inputbox = self.browser.find_element_by_id('Course_Id')
        inputbox.send_keys('English 101')
        inputbox.send_keys(Keys.ENTER)
        time.sleep(2)

        self.check_for_row_in_table('1: History 101')
        self.check_for_row_in_table('2: English 101')



    #2a)     

    #3) Sprint 2: He noticed that there is options next to his course list that sets it to done or in-progress. 

    #4) When Danny selected done, a green text that says "Done" pops up next to the course.

    #5) If he select "In-Progress" a yellow text pops up that says "In-Progress"

    #6) Excited he wonders if the list will save and be used later on.




        self.fail('Testing Version Intentional Fail')  

if __name__ == '__main__':  
    unittest.main(warnings='ignore') 