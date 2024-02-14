import secrets
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class Mouse:

    @staticmethod
    def get_dimensions(driver):
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
    def init_mouse(driver, cursor, wait):
        #cursor.show_cursor()
        len_choice = secrets.SystemRandom().randrange(1, 10)
        for i in range(len_choice):
            x_perc_choice = secrets.SystemRandom().randrange(1, 100)
            y_perc_choice = secrets.SystemRandom().randrange(1, 100)
            page_dimensions = Mouse.get_dimensions(driver)
            p_width = page_dimensions["width"]
            p_height = page_dimensions["height"]
            random_x = p_width * (x_perc_choice/100)
            random_y = p_height * (y_perc_choice/100)
            cursor.move_to([random_x, random_y])

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
    def get_viewport_height(driver):
        js_code = """
                    var totalPageHeight = window.innerHeight; 
                    return totalPageHeight;
                """
        viewport_height = driver.execute_script(js_code)
        return viewport_height

    @staticmethod
    def is_element_visible(driver, element, wait):
        try:
            # Espera até que o elemento seja visível
            wait.until(EC.visibility_of(element))

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























