from time import sleep

from humancursor import WebCursor
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

from BrowserConfig import Config
from ScrollRandomization import ScrollRandomization
from MouseRandomization import Mouse
from Navigation import Navigation
from Data_Extraction import Extraction, MetaData


# Main Function
sleep(5)
# Configurações
configurations = Config()
wait = configurations.wait
driver = configurations.driver
cursor = WebCursor(driver)

#Mouse.mouse_passing_to_random_elements(driver, cursor)

time_start =
last_page = 5
current_page = Navigation.current_page(wait, driver)
while current_page <= last_page:
    Mouse.init_mouse(driver, cursor, wait)
    wait.until(EC.presence_of_all_elements_located((By.XPATH, '//div[@class="results-main__panel js-list"]')))
    page_ads = Extraction.all_page_houses_extraction(wait, driver)
    total_page_ads = 0
    total_page_ads += page_ads
    ScrollRandomization.scroll_to_element_by_xpath(wait, driver, '//ul[@class="pagination__wrapper"]')
    Navigation.next_page(wait, driver, cursor)
    current_page = Navigation.current_page(wait, driver)

driver.quit()
MetaData.get_extraction_info(wait, driver, time_start, time_stop, last_page)











