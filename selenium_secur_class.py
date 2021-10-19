from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import antigravity


driver = webdriver.Chrome(executable_path='/home/vladyslav/IT_Step/lesson_25-26/chromedriver')


def decorator_checking_site(checking_site):
    def checking_main_page(*args, **kwargs):
        try:
            result = checking_site(*args, **kwargs)
            return result
            
        except:
            print('A site that does not exist or is incorrectly specified.')
            exit()
    
    return checking_main_page

def decorator_checking_id(checking_id):
    def checking_element_id(*args, **kwargs):

        try:
            result = checking_id(*args, **kwargs)
            return result

        except:
            print('Element with the specified "ID" was not found.')
            exit()

    return checking_element_id

def decorator_checking_class_name(checking_class_name):
    def checking_element_class_name(*args, **kwargs):

        try:
            result = checking_class_name(*args, **kwargs)
            return result

        except:
            print('Element with the specified "CLASS_NAME" was not found.')
            exit()

    return checking_element_class_name

def decorator_cheking_link_text(cheking_link_text):
    def cheking_element_link_text(*args, **kwargs):

        try:
            result = cheking_link_text(*args, **kwargs)
            return result

        except:
            print('Element with the specified "LINK_TEXT" was not found.')
            exit()

    return cheking_element_link_text


class MainPage_ChoosingProduct:

    def __init__(self, driver):
        self.driver = driver

    @decorator_checking_site
    def main_page(self):
            
        self.driver.implicitly_wait(10)
        self.driver.get('https://secur.ua/')
    
    @decorator_checking_id
    def element_search(self):

        self.driver.implicitly_wait(10)
        element_search = self.driver.find_element(By.ID, 'search')
            
        element_search.clear()
        element_search.send_keys('Видеокамера AHD купольная Tecsar AHDD-20V5M-in')
        element_search.send_keys(Keys.ENTER)

    @decorator_checking_class_name
    def choosing_product(self):

        self.driver.implicitly_wait(10)
        self.driver.find_element(By.CLASS_NAME, 'product-wrap').click()


class SearchElementReview_WritingReview:

    def __init__(self, driver):
        self.driver = driver

    @decorator_cheking_link_text
    def search_element_review(self):

        self.driver.implicitly_wait(10)
        tabs_manu = driver.find_element(By.LINK_TEXT, 'Отзывы')
        tabs_manu.send_keys(Keys.RETURN)

    @decorator_checking_id
    def writing_review(self):

        self.driver.implicitly_wait(10)
        name = driver.find_element(By.ID, 'nickname_field')

        name.clear()
        name.send_keys('Vlad')

        self.driver.implicitly_wait(10)
        email = driver.find_element(By.ID, 'summary_field')

        email.clear()
        email.send_keys('@')

        self.driver.implicitly_wait(10)
        detail = driver.find_element(By.ID, 'review_field')

        detail.clear()
        detail.send_keys('Very good')

        self.driver.implicitly_wait(10)
        pluses_product = driver.find_element(By.ID, 'pluses_product')

        pluses_product.clear()
        pluses_product.send_keys('Very-very good')

        self.driver.implicitly_wait(10)
        lows_product = driver.find_element(By.ID, 'lows_product')

        lows_product.clear()
        lows_product.send_keys('Nope')

    @decorator_checking_class_name
    def button_send(self):

        self.driver.implicitly_wait(10)
        driver.find_element(By.CLASS_NAME, 'btn.btn-silver.btn-review-post.button').click()

        time.sleep(10)
        driver.close()
        driver.quit()


first_class = MainPage_ChoosingProduct(driver)
first_class.main_page()
first_class.element_search()
first_class.choosing_product()

second_class = SearchElementReview_WritingReview(driver)
second_class.search_element_review()
second_class.writing_review()
second_class.button_send()


