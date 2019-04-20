from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException
import time
from django.test import LiveServerTestCase

Max_WAIT = 10

class FIrstTestCase(LiveServerTestCase):


    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        #Close Browser.
        self.browser.quit()

    def wait_for_row_table(self, row_text):
        start_time = time.time()
        while True:
            try:
                table = self.browser.find_element_by_id('Course_Table')
                rows = table.find_elements_by_tag_name('tr')
                self.assertIn(row_text, [row.text for row in rows])
                return
            except (AssertionError, WebDriverException) as e:
                if time.time() - start_time > Max_WAIT:
                    raise e
                time.sleep(0.5)

    def test_multi_user_list_diff_urls(self):
        self.browser.get(self.live_server_url)
     
     
    #Danny wants a list e manage the courses he requires for his major.
    #He goes to this website that he heard from his senior to help manage his course.

    #Danny saw the title of the website and knows he is on the right site.

    #1) He saw a textbox for him to enter his course.
        #submitBox = self.browser.find_element_by_xpath('//button[contains(text(), "Submit")]').click
        inputbox = self.browser.find_element_by_id('Course_Id')
        inputbox.send_keys('History 101')

        #submitBox()
        #time.sleep(5)
        inputbox.send_keys(Keys.ENTER)
        #CourseAttribute = inputbox.get_attribute()
        self.wait_for_row_table('1: History 101')



    #2) He enters a course as a test and press es the enter key and saw the list updated. Adding his course to the list
        #Still need to work on how to get user input Sprint 2
        

        #Testing phase allow time to enter info

        """
        Gets text from input box used for formating currently useless
        CourseAdding = inputbox.text
        """

        """
        Sprint 2: Make it not Hardcoded 
        Sample: Currently Gives AssertionError from home.html
        self.check_for_row_in_table('1: {0}'.format(CourseAdding))
        """


    #2a)     

    #3) Sprint 2: He noticed that there is options next to his course list that sets it to done or in-progress. 

    #4) When Danny selected done, a green text that says "Done" pops up next to the course.

    #5) If he select "In-Progress" a yellow text pops up that says "In-Progress"

    #6) Excited he wonders if the list will save and be used later on.


    #7) Danny notices the Unqiue URL
        danny_list_url = self.browser.current_url
        self.assertRegex(danny_list_url, '/lists/.+')

        time.sleep(5)
    #8) His friend Josh decided to give the site a try
    ##New browser session to avoid having another user info display
        self.browser.quit()
        self.browser = webdriver.Firefox()

    #9)Josh vists homepage
        self.browser.get(self.live_server_url)
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('History 101', page_text)

        inputbox = self.browser.find_element_by_id('Course_Id')
        inputbox.send_keys('Art 101')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_table('1: Art 101')
    #10) Josh noticed his own unique url tooss
        josh_list_url = self.browser.current_url
        self.assertRegex(josh_list_url, '/lists/.+')
        self.assertNotEqual(danny_list_url, josh_list_url)

        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('History 101', page_text)
        self.assertIn('Art 101', page_text)
	    
        time.sleep(5)
        #self.fail('Testing Version Intentional Fail')  
