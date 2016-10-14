from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

	def setUp(self):
		self.browser = webdriver.Chrome()
		self.browser.implicitly_wait(3)

	def tearDown(self):
		self.browser.quit()

	def test_can_start_a_list_and_retrieve_it_later(self):
		#Mike heard about a sweet new to-do app. He headed to check out its homepage.
		self.browser.get('http://localhost:8000')

		#He mentioned the page title and header mention to-do lists
		self.assertIn('To-Do',self.browser.title)
		self.fail('Finish the test!')


	#MIke is inivited to enter a to-do item straight away

	#He types "buy rock climbing gear"(mike's hobby is rock-climbing)
	#When she hits enter, the page updates, and now the page lists
	#1: Buy rock climbing gear" as an item in the to-do list

	#There is still a text box inviting him to add another item. He
	#enters "Learn how to trad climb"(Mike is dead-set on trying to learn to trad climb)

	#The page updates again, and now shows both items on her list

	#Mike wonders if whether the site will remember his list. Then he sees
	#that the site has generated a unique URL for her -- there is some
	#explanatory text to that effect.

	#He visists that URL - His to-do list is stil here.

	#Satisified, he goes back to mindlessly browsing reddit.

if __name__ == '__main__':
	unittest.main(warnings='ignore')

browser.quit()
