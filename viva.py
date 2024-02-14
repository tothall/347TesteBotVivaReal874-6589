import random
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep


class ScrollRandomization:
    @staticmethod
    def human_scroll_down(driver, height_percentual=None):
        total_scroll_height = ScrollRandomization.get_scroll_height(driver)
        ref_scroll = ScrollRandomization.current_scroll(driver)

        if ref_scroll >= total_scroll_height:
            return

        if height_percentual:
            hgt_perc = (height_percentual / 100) * total_scroll_height
        else:
            random_perc = random.randint(10, 30)
            hgt_perc = (random_perc / 100) * total_scroll_height

        while ScrollRandomization.current_scroll(driver) < total_scroll_height and ScrollRandomization.current_scroll(driver) - ref_scroll < hgt_perc:
            ScrollRandomization.scroll_down(driver)
            sleep(0.1)  # Ajuste o tempo conforme necessário

    @staticmethod
    def scroll_down(driver):
        ActionChains(driver).key_down(Keys.ARROW_DOWN).perform()

    @staticmethod
    def get_scroll_height(driver):
        return driver.execute_script("return Math.max( document.body.scrollHeight, document.body.offsetHeight, document.documentElement.clientHeight, document.documentElement.scrollHeight, document.documentElement.offsetHeight );")

    @staticmethod
    def current_scroll(driver):
        return driver.execute_script("return window.scrollY;")

# Exemplo de uso:
# driver = ...  # Seu objeto WebDriver aqui
# ScrollRandomization.human_scroll_down(driver)
