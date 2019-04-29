from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import WebDriverException
import time
from django.contrib.staticfiles.testing import StaticLiveServerTestCase

Max_WAIT = 10

class FIrstTestCase(StaticLiveServerTestCase):


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
     
     
    #Danny wants a list to manage the courses he requires for his major.
    #He goes to this website that he heard from his senior to help manage his course.

    #Danny saw the title of the website and knows he is on the right site.

    #1) He saw a textbox for him to enter his course.
        inputbox = self.browser.find_element_by_id('Course_Id')


    #2) He enters a course as a test and press es the enter key and saw the list updated. Adding his course to the list
        
        inputbox.send_keys('History 101')

        inputbox.send_keys(Keys.ENTER)
        
        #CourseAttribute = inputbox.get_attribute()
        self.wait_for_row_table('1: History 101')
        inputbox = self.browser.find_element_by_id('Course_Id')

        inputbox.send_keys('Language 101')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_table('2: Language 101')

    #3) His Course shows up and when he clicks on the checkbox it crossed out the selected course and 
    # the text turned green. 
        checkbox = self.browser.find_element_by_id('Completed')
        checkbox.click()
        time.sleep(5)



    #4) Danny notices the Unqiue URL
        danny_list_url = self.browser.current_url
        self.assertRegex(danny_list_url, '/lists/.+')

        time.sleep(5)

    #5) His friend Josh decided to give the site a try
    ##New browser session to avoid having another user info display
        self.browser.quit()
        self.browser = webdriver.Firefox()

    #6)Josh vists homepage
        self.browser.get(self.live_server_url)
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('History 101', page_text)

        inputbox = self.browser.find_element_by_id('Course_Id')
        inputbox.send_keys('Art 101')
        inputbox.send_keys(Keys.ENTER)
        self.wait_for_row_table('1: Art 101')

    #7) Josh noticed his own unique url tooss
        josh_list_url = self.browser.current_url
        self.assertRegex(josh_list_url, '/lists/.+')
        self.assertNotEqual(danny_list_url, josh_list_url)

        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('History 101', page_text)
        self.assertIn('Art 101', page_text)
	    
        time.sleep(5)
        #self.fail('Testing Version Intentional Fail')  
