import time
import secrets
import threading
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


class TimeRandomization:

    @staticmethod
    def chrono(start=None, stop=None):
        start_time = 0
        stop_time = 0
        if start == "start":
            start_time = time.time()  # Inicia o cronômetro
        elif stop == "stop"
            stop_time = time.time()
        delta_time = start_time - stop_time
        return delta_time

    @staticmethod
    def secrets_random_wait(floor, ceiling):
        len_ = (ceiling - floor) + 1
        seq = [0] * len_
        seq[0] = floor
        for i in range(1, len_):
            seq[i] = seq[i - 1] + 1

        choice_seconds = secrets.choice(seq) / 10
        time.sleep(choice_seconds)
        return choice_seconds

    @staticmethod
    def secrets_short_wait(driver=None, cursor=None, mouse_mode=None):

        if mouse_mode:
            return MouseAndScroll.mands(8, 17, driver, cursor)
        else:
            return TimeRandomization.secrets_random_wait(8, 17)

    @staticmethod
    def secrets_medium_wait(driver=None, cursor=None, mouse_mode=None):
        if mouse_mode:
            return MouseAndScroll.mands(19, 34, driver, cursor)
        else:
            return TimeRandomization.secrets_random_wait(19, 34)

    @staticmethod
    def secrets_long_wait(driver=None, cursor=None, mouse_mode=None):
        if mouse_mode:
            return MouseAndScroll.mands(41, 50, driver, cursor)
        else:
            return TimeRandomization.secrets_random_wait(41, 50)


class Mouse:

    @staticmethod
    def get_viewport_dimensions(driver):
        js_code = """
            var totalPageWidth = window.innerWidth;
            var totalPageHeight = window.innerHeight; 
            var dimensions = {
                width: totalPageWidth,
                height: totalPageHeight
            };
            return dimensions;
        """
        dimensions = driver.execute_script(js_code)
        return dimensions

    @staticmethod
    def init_mouse(driver, cursor):
        len_choice = secrets.SystemRandom().randrange(1, 6)
        for i in range(6):
            random_stop = secrets.randbelow(2)
            random_steady = secrets.SystemRandom().randrange(0, 1)
            if random_stop == 0:
                pass
            elif random_stop == 1:
                pass
            elif random_stop == 2:
                TimeRandomization.secrets_short_wait(driver, cursor)

            x_perc_choice = secrets.SystemRandom().randrange(1, 100)
            y_perc_choice = secrets.SystemRandom().randrange(1, 100)
            page_dimensions = Mouse.get_viewport_dimensions(driver)
            p_width = page_dimensions["width"]
            p_height = page_dimensions["height"]
            random_x = p_width * (x_perc_choice/100)
            random_y = p_height * (y_perc_choice/100)
            if random_steady == 0:
                cursor.move_to([random_x, random_y])
            else:
                cursor.move_to([random_x, random_y], steady=True)

    @staticmethod
    def is_element_visible(driver, element):
        try:
            # Espera até que o elemento seja visível
            WebDriverWait(driver, 10).until(EC.visibility_of(element))

            # Obtém as coordenadas e dimensões do elemento
            element_rect = element.rect

            # Verifica se o elemento está dentro do viewport
            return (
                    element_rect['x'] >= 0 and
                    element_rect['y'] >= 0 and
                    element_rect['x'] + element_rect['width'] <= driver.execute_script("return window.innerWidth") and
                    element_rect['y'] + element_rect['height'] <= driver.execute_script("return window.innerHeight")
            )
        except Exception as e:
            print(f"Erro ao verificar visibilidade: {str(e)}")
            return False

    @staticmethod
    def elementos_visiveis_no_viewport(driver, elementos):
        elementos_visiveis = list(set())

        for elemento in elementos:
            if Mouse.is_element_visible(driver, elemento):
                elementos_visiveis.append(elemento)

        return elementos_visiveis

    @staticmethod
    def mouse_passing_to_random_elements(driver, cursor):
        elementos = driver.find_elements(By.XPATH, "//div[@class='col-md-4 country']")
        conjunto_elementos_visiveis = Mouse.elementos_visiveis_no_viewport(driver, elementos)

        lent = len(conjunto_elementos_visiveis)
        random_len = secrets.randbelow(lent + 1)
        while random_len == 0:
            random_len = secrets.randbelow(lent + 1)
        print(random_len)
        for i in range(random_len):
            random_index = secrets.randbelow(random_len)
            print(random_index)
            cursor.move_to(conjunto_elementos_visiveis[random_index])

    @staticmethod
    def mouse_passing_to_random_elements_by_time(driver, cursor, delta_t):
        elementos = driver.find_elements(By.XPATH, "//div[@class='col-md-4 country']")
        conjunto_elementos_visiveis = Mouse.elementos_visiveis_no_viewport(driver, elementos)

        lent = len(conjunto_elementos_visiveis)
        random_len = secrets.randbelow(lent + 1)
        while random_len == 0:
            random_len = secrets.randbelow(lent + 1)
        print(random_len)
        for i in range(random_len):
            random_index = secrets.randbelow(random_len)
            print(random_index)
            cursor.move_to(conjunto_elementos_visiveis[random_index])












