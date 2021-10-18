from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


driver = webdriver.Chrome(executable_path='/home/vladyslav/IT_Step/lesson_25-26/chromedriver')


class MainPage_ChoosingProduct:

    def __init__(self, driver):
        self.driver = driver

    def main_page(self):
            
        try:
            self.driver.implicitly_wait(10)
            self.driver.get('https://secur.ua/')

        except:
            print('A site that does not exist or is incorrectly specified')
            exit()

    
    def element_search(self):

        try:
            
            self.driver.implicitly_wait(10)
            element_search = self.driver.find_element_by_id('search')
            
            element_search.clear()
            element_search.send_keys('Видеокамера AHD купольная Tecsar AHDD-20V5M-in')
            element_search.send_keys(Keys.ENTER)

        except:
            print('Element with the specified "id" was not found')
            exit()

    def choosing_product(self):

        try:
            
            self.driver.implicitly_wait(10)
            products_grid = self.driver.find_element_by_class_name('product-wrap').click()

        except:
            print('Element with the specified "class" was not found')
            exit()

class SearchElementReview_WritingReview:
    def __init__(self, driver):
        self.driver = driver

    def search_element_review(self):

        while True:
            try:

                self.driver.implicitly_wait(10)
                tabs_manu = driver.find_element_by_link_text('Отзывы')
                tabs_manu.send_keys(Keys.RETURN)
                break

            except:
                print('Element with the specified "link text" was not found')
                exit()

    def writing_review(self):
        try:

            name = driver.find_element_by_id('nickname_field')
            name.send_keys('Vlad')

            email = driver.find_element_by_id('summary_field')
            email.send_keys('@')

            detail = driver.find_element_by_id('review_field')
            detail.send_keys('Very good')

            pluses_product = driver.find_element_by_id('pluses_product')
            pluses_product.send_keys('Very-very good')

            lows_product = driver.find_element_by_id('lows_product')
            lows_product.send_keys('Nope')

            driver.find_element_by_class_name('btn.btn-silver.btn-review-post.button').click()

        except Exception as ex:
            print(ex)

        # finally:
        #     time.sleep(10)
        #     driver.close()
        #     driver.quit()




first_class = MainPage_ChoosingProduct(driver)
first_class.main_page()
first_class.element_search()
first_class.choosing_product()

second_class = SearchElementReview_WritingReview(driver)
second_class.search_element_review()
second_class.writing_review()


