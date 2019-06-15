from selenium import webdriver
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
        self.fail('Finish the test')

#You want to enter a to-do item straight away

#You type "Buy peacock feathers" into a text box

#You hit enter the page updates and now the page lists
#1: "Buy peacock feathers" as an item on the to-do lists

#There is still a text box inviting you to add another item.
#You enter "Use peacock feathers to make a fly"

#The page updates and now shows both items on the list

#You wonder if the site will remember your list. You see
#that the site has generate a unique url for you, and
#there is some explanatory text to that effect

#you visit the URL and the to-do list is still there

#You are satisfied and close your browser

if __name__ == '__main__':
    unittest.main(warnings='ignore')
