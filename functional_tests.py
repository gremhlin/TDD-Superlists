from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest



class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()

    def test_start_and_retrieve_list(self):
        #You want to check out a new todo app, and go it its homepage
        self.browser.get('http://localhost:8000')

        #you notice the header and title mention to-do lists
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        #You're invited to enter a to-do item straight away
        inputbox =self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a To-Do item'
        )

        #You type "Buy peacock feathers" into a text box
        inputbox.send_keys('Buy peacock feathers')

        #You hit enter the page updates and now the page lists
        #1: "Buy peacock feathers" as an item on the to-do lists
        inputbox.send_keys(keys.ENTER)
        time.sleep(1)

        table = self.browers.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1: Buy peacock feathers' for row in rows)
        )
        #There is still a text box inviting you to add another item.
        #You enter "Use peacock feathers to make a fly"
        self.fail('Finish the test')
        #The page updates and now shows both items on the list

        #You wonder if the site will remember your list. You see
        #that the site has generate a unique url for you, and
        #there is some explanatory text to that effect

        #you visit the URL and the to-do list is still there

        #You are satisfied and close your browser

if __name__ == '__main__':
    unittest.main(warnings='ignore')
