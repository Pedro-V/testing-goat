from selenium import webdriver
import unittest

# Todo script que usa o webdriver deve ativar o server rodando, na linha de comando: 
# python manage.py runserver

class NewVisitorTest(unittest.TestCase):
    # setUp e tearDown rodam antes e após cada teste
    def setUp(self) -> None:
        self.browser = webdriver.Firefox()

    def tearDown(self) -> None:
        self.browser.quit()
    
    def test_can_start_a_list_and_retrieve_it_later(self):
        self.browser.get('http://localhost:8000')

        self.assertIn('To-Do', self.browser.title)


if __name__ == '__main__':
    unittest.main()


