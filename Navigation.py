from time import sleep
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException, NoSuchElementException
import secrets


class Navigation:
    """Todas as funções dessa classe recebem como argumento o wait e/ou o argumento driver.
    Isso acontece pelo fato das funções dependerem do objeto driver e do objeto wait da classe
    Configurations"""

    @staticmethod
    def next_page(wait, driver, cursor):
        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="js-site-main"]/div[2]/div[1]/section/div[2]/div[2]/div/ul/li[9]/button')))
        next_button = driver.find_element(By.XPATH, '//*[@id="js-site-main"]/div[2]/div[1]/section/div[2]/div[2]/div/ul/li[9]/button')
        random_x = (secrets.SystemRandom().randrange(1, 9))/10
        random_y = (secrets.SystemRandom().randrange(1, 9))/10
        cursor.click_on(next_button, relative_position=[random_x, random_y])
        return print("Página passada com sucesso")

    @staticmethod
    def current_page(wait, driver):
        wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="js-site-main"]/div[2]/div[1]/section/div[2]/div[2]/div/ul/li[9]/button')))
        next_button = driver.find_element(By.XPATH, '//*[@id="js-site-main"]/div[2]/div[1]/section/div[2]/div[2]/div/ul/li[9]/button')
        current_page = next_button.get_attribute('data-page')
        if current_page > 1:
            _current_page = current_page - 1
            return _current_page
        else:
            return current_page

    @staticmethod
    def main_page_wait(wait):

        # Esperar até que os elementos estejam presentes
        try:
            wait.until(
                EC.presence_of_all_elements_located((By.XPATH, "/html/body/div[1]/div[3]/div/div[1]/div/div/ul")))
        except TimeoutException:
            print(
                "Os elementos do elemento (tag ul e class=nav flex-colummn) não estão presentes. Verifique se há mudanças na página.")

    @staticmethod
    def all_next_pages(wait, driver):
        wait.until(EC.presence_of_all_elements_located((By.XPATH, "//ul[@class='pagination__wrapper']")))
        wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@title='Próxima página']")))
        button = driver.find_element(By.XPATH, "//button[@title='Próxima página']")
        while button.is_enabled():
            try:
                driver.execute_script("arguments[0].scrollIntoView();", button)
                driver.execute_script("arguments[0].click();", button)
                # ActionChains(driver)\
                #        .scroll_to_element(button)\
                #        .perform()
                wait.until(EC.presence_of_all_elements_located((By.XPATH, "//div[@class='property-card__content']")))
                sleep(2)
                wait.until(EC.presence_of_all_elements_located((By.XPATH, "//ul[@class='pagination__wrapper']")))
                wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@title='Próxima página']")))
                button = driver.find_element(By.XPATH, "//button[@title='Próxima página']")
            except (TimeoutException, StaleElementReferenceException):
                break

    @staticmethod
    def all_products_click_and_next_pages(wait, driver):
        """Essa função aceita como exceção páginas que não tem o botão de passar páginas"""
        cancel_while = None
        button = None
        try:
            wait.until(EC.presence_of_all_elements_located((By.XPATH, "//div[@class='pager']")))
            wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='pager']/button[2]")))
            button = driver.find_element(By.XPATH, "//div[@class='pager']/button[2]")
        except (TimeoutException, StaleElementReferenceException):
            Navigation.all_page_products_click(wait, driver)
            cancel_while = 1
        while cancel_while != 1 and button.is_enabled():
            try:
                driver.execute_script("arguments[0].scrollIntoView();", button)
                driver.execute_script("arguments[0].click();", button)
                # ActionChains(driver)\
                #        .scroll_to_element(button)\
                #        .perform()
                wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, "card-body")))
                Navigation.all_page_products_click(wait, driver)
                sleep(2)
                wait.until(EC.presence_of_all_elements_located((By.XPATH, "//div[@class='pager']")))
                wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='pager']/button[2]")))
                button = driver.find_element(By.XPATH, "//div[@class='pager']/button[2]")
            except TimeoutException:
                break
