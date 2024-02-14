import random
import time
from itertools import permutations

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC

from TimeRandomization import TimeRandomization
import secrets
from MouseRandomization import Mouse


class ScrollRandomization:

    @staticmethod
    def get_scroll_height(driver):
        return driver.execute_script("return Math.max(document.body.scrollHeight - window.innerHeight);")

    @staticmethod
    def get_scrollbar_height(driver):
        return driver.execute_script("return window.innerHeight;")

    @staticmethod
    def scroll_bar_height_discount(driver, height_in_pixels):
        scroll_bar_height = driver.execute_script("return window.innerHeight;")
        height_correction = height_in_pixels - scroll_bar_height
        return height_correction

    @staticmethod
    def current_scroll(driver):
        return driver.execute_script("return window.scrollY;")
        #return driver.execute_script("return window.pageYOffset")
        # return driver.execute_script("return window.pageYOffset + window.innerHeight")

    @staticmethod
    def get_viewport_height(driver):
        js_code = """
                var totalPageHeight = window.innerHeight; 
                return totalPageHeight;
            """
        height = driver.execute_script(js_code)
        return height

    @staticmethod
    def get_element_scroll_height(driver, xpath):
        js_code = """
           var element_xpath = '%s';
           var element = document.evaluate(element_xpath, document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
           if (element) 
           {
               var rectangle = element.getBoundingClientRect();
               var element_scroll_height = rectangle.top + window.scrollY;
               return element_scroll_height;
               } 
           else 
           {
               return null;
           }
           """ % xpath
        element_scroll_height = driver.execute_script(js_code)
        return element_scroll_height

    @staticmethod
    def human_scroll_down(driver, random_perc_start, random_perc_stop, dy_start, dy_stop, short_wait_start,
                          short_wait_stop, medium_wait_start, medium_wait_stop, long_wait_start, long_wait_stop,
                          height_percentual=None):

        ref_scroll = ScrollRandomization.current_scroll(driver)  # Salva a altura inicial(pixels) quando a função é chamada
        total_scroll_height = ScrollRandomization.get_scroll_height(driver)  # Altura total do scroll em pixels

        if ref_scroll >= total_scroll_height:  # Impede a rolagem quando a página está no final
            return

        delta_h = ScrollRandomization.current_scroll(driver) - ref_scroll  # Altura percorrida inicial(zero)
        #print(ref_scroll)
        #print(total_scroll_height)

        if height_percentual:  # função no modo não randômico percentual de altura
            target_height = (height_percentual / 100) * total_scroll_height
        else:  # função no modo randômico de percentual da altura
            random_perc = secrets.SystemRandom().randrange(random_perc_start, random_perc_stop)
            delta_h_hgt_perc = (random_perc / 100) * total_scroll_height
            target_height = abs(ScrollRandomization.scroll_bar_height_discount(driver, delta_h_hgt_perc))

        while delta_h <= target_height:
            # Randomização das pausas
            time_choice = secrets.SystemRandom().randrange(1, 11)
            if short_wait_start <= time_choice <= short_wait_stop:  # Randomiza pausas aleatórias curtas
                TimeRandomization.secrets_short_wait()
            elif medium_wait_start <= time_choice <= medium_wait_stop:  # Randomiza pausas aleatórias médias
                TimeRandomization.secrets_medium_wait()
            elif long_wait_start <= time_choice <= long_wait_stop:  # Randomiza pausas aleatórias longas
                TimeRandomization.secrets_long_wait()

            dy = secrets.SystemRandom().randrange(dy_start, dy_stop)  # Randomiza o quanto é rolado de uma única vez
            for j in range(dy):
                delta_h = ScrollRandomization.current_scroll(driver) - ref_scroll
                if ScrollRandomization.current_scroll(driver) >= total_scroll_height:
                    return
                if delta_h >= target_height:
                    return

                #  Pressiona a seta para baixo
                ActionChains(driver) \
                    .key_down(Keys.ARROW_DOWN) \
                    .perform()

            # Altura percorrida no término do for(Define a continuidade do while)
            delta_h = ScrollRandomization.current_scroll(driver) - ref_scroll
            #print("rolagem")

    @staticmethod
    def human_scroll_down_long_pattern(driver, height_percentual=None):
        #print("short")
        return ScrollRandomization.human_scroll_down(driver, 5, 10, 13, 25,
                                                   3, 6, 7, 10,
                                                   7, 10, height_percentual)

    @staticmethod
    def human_scroll_down_medium_pattern(driver, height_percentual=None):
        #print("medium")
        return ScrollRandomization.human_scroll_down(driver, 5, 10, 6, 10,
                                                   1, 3, 4, 8,
                                                   9, 10, height_percentual)

    @staticmethod
    def human_scroll_down_short_pattern(driver, height_percentual=None):
        #print("long")
        return ScrollRandomization.human_scroll_down(driver, 1, 5, 2, 5,
                                                   1, 8, 9, 9,
                                                   10, 10, height_percentual)

    @staticmethod
    def human_scroll_down_precision_short_pattern(driver, height_percentual=None):
        return ScrollRandomization.human_scroll_down(driver, 1, 3, 2, 5,
                                                     1, 8, 9, 9,
                                                     10, 10, height_percentual)

    @staticmethod
    def scroll_down(driver, height_percentual=None, height_in_pixels=None):
        ref_scroll = ScrollRandomization.current_scroll(driver)  # Salva a altura inicial quando a função é chamada
        total_scroll_height = ScrollRandomization.get_scroll_height(driver)  # Altura total do scroll
        viewport_height = ScrollRandomization.get_viewport_height(driver)
        # Impede a rolagem quando a página está no final
        if ref_scroll >= total_scroll_height:
            return
        delta_h = ScrollRandomization.current_scroll(driver) - ref_scroll
        # Altura percorrida inicial(zero)

        print(f"delta_h inicial = {delta_h}")
        #print(ref_scroll)
        #print(total_scroll_height)

        if height_percentual:
            #target_height = (height_percentual / 100) * total_scroll_height
            target_height = abs(ScrollRandomization.scroll_bar_height_discount(driver, height_percentual))
        elif height_in_pixels:
            #target_height = height_in_pixels
            target_height = abs(ScrollRandomization.scroll_bar_height_discount(driver, height_in_pixels))

        else:
            random_perc = secrets.SystemRandom().randrange(10, 30)
            target_height = (random_perc / 100) * total_scroll_height

        while delta_h <= target:
            delta_h = ScrollRandomization.current_scroll(driver) - ref_scroll
            if ScrollRandomization.current_scroll(driver) >= total_scroll_height:
                return
            if delta_h >= target_height:
                return
            pattern_choice = secrets.SystemRandom().randrange(1, 4)
            if pattern_choice == 1:
                print("escolheu 1")
                ScrollRandomization.human_scroll_down_long_pattern(driver)
            elif pattern_choice == 2:
                print("escolheu 2")
                ScrollRandomization.human_scroll_down_medium_pattern(driver)
            elif pattern_choice == 3:
                print("escolheu 3")
                ScrollRandomization.human_scroll_down_short_pattern(driver)

    @staticmethod
    def viewport_scroll_down(driver, height_in_pixels=None):
        ref_scroll = ScrollRandomization.current_scroll(driver)  # Salva a altura inicial quando a função é chamada
        total_scroll_height = ScrollRandomization.get_scroll_height(driver)  # Altura total do scroll
        viewport_height = ScrollRandomization.get_viewport_height(driver)  # Altura total da viewport
        delta_h = ScrollRandomization.current_scroll(driver) - ref_scroll  # Altura percorrida inicial(zero)

        # Impede a rolagem quando a página está no final
        if ref_scroll >= total_scroll_height:
            return

        # print(ref_scroll)
        #print(total_scroll_height)


        viewport_target_height = 0
        # Subtrai a altura do scroll da altura de input
        target_height = abs(ScrollRandomization.scroll_bar_height_discount(driver, height_in_pixels))
        print(f"target height={target_height}")
        print(f"viewport={viewport_height}")
        if target_height > viewport_height:
            number = target_height / viewport_height
            print(f"number={number}")
            viewport_target_height = (number - 0.5) * viewport_height
        else:
            print("ERRO")
            pass

        print(f"target={viewport_target_height}")
        while delta_h <= viewport_target_height:
            delta_h = ScrollRandomization.current_scroll(driver) - ref_scroll
            if ScrollRandomization.current_scroll(driver) >= total_scroll_height:
                return
            if delta_h >= target_height:
                return
            pattern_choice = secrets.SystemRandom().randrange(1, 4)
            if pattern_choice == 1:
                #print("escolheu 1")
                ScrollRandomization.human_scroll_down_long_pattern(driver)
            elif pattern_choice == 2:
                #print("escolheu 2")
                ScrollRandomization.human_scroll_down_medium_pattern(driver)
            elif pattern_choice == 3:
                #print("escolheu 3")
                ScrollRandomization.human_scroll_down_short_pattern(driver)
        return print("Fim scroll")

    @staticmethod
    def scroll_to_element_by_xpath(wait, driver, xpath):
        wait.until(EC.presence_of_all_elements_located((By.XPATH, xpath)))  # Realiza a espera do carregamento do elemento web
        ref_scroll = ScrollRandomization.current_scroll(driver)
        element_height = ScrollRandomization.get_element_scroll_height(driver, xpath)
        if ref_scroll < element_height:
            ScrollRandomization.viewport_scroll_down(driver, element_height)

        elif ref_scroll > element_height:
            print("subida")
            while ScrollRandomization.current_scroll(driver) > element_height:
                ScrollRandomization.scroll_up(driver, False, element_height)

        elif ref_scroll == element_height:
            return

    @staticmethod
    def random_updown_scroll_by_time(driver):

        scroll_height = ScrollRandomization.get_scroll_height(driver)  # Altura total do scroll
        ref_scroll = ScrollRandomization.current_scroll(driver)  # Salva a altura inicial quando a função é chamada
        start_time = time.time()  # Inicia o cronômetro
        random_amount = random.randint(20, 35) / 100
        amount = 100 / 100 * ScrollRandomization.get_scroll_height(driver)
        permutation_range = [1, 2, 3, 4, 5, 6]
        permuta = list(permutations(permutation_range))
        delta_time = time.time() - start_time
        random_time = random.randint(10, 30)

        while delta_time <= 80:  # Define o tempo(segundos) que os movimentos randômicos vão durar
            delta_time = time.time() - start_time
            permuta_choice = random.randint(0, 719)
            print(permuta[permuta_choice])
            for i in permuta[permuta_choice]:
                delta_time = time.time() - start_time
                if 1 <= i <= 2:  # 50%
                    choice = random.randint(1, 3)
                    if choice == 1 or choice == 2:
                        ScrollRandomization.short_delta_y_down(driver, amount)
                    elif choice == 3:
                        ScrollRandomization.short_delta_y_up(driver, amount)
                elif 3 <= i <= 4:  # 33%
                    choice = random.randint(1, 3)
                    if choice == 1 or choice == 2:
                        ScrollRandomization.medium_delta_y_down(driver, amount)
                    elif choice == 3:
                        ScrollRandomization.medium_delta_y_up(driver, amount)
                elif 5 <= i <= 6:  # 16%
                    choice = random.randint(1, 3)
                    if choice == 1 or choice == 2:
                        ScrollRandomization.long_delta_y_down(driver, amount)
                    elif choice == 3:
                        ScrollRandomization.long_delta_y_up(driver, amount)

    @staticmethod
    def human_scroll_up(driver, random_perc_start, random_perc_stop, dy_start, dy_stop, short_wait_start,
                        short_wait_stop, medium_wait_start, medium_wait_stop, long_wait_start, long_wait_stop,
                        height_percentual=None):

        ref_scroll = ScrollRandomization.current_scroll(
            driver)  # Salva a altura inicial(pixels) quando a função é chamada
        total_scroll_height = ScrollRandomization.get_scroll_height(driver)  # Altura total do scroll em pixels

        if ref_scroll <= 0:  # Impede a rolagem quando a página está no final
            return

        delta_h = ref_scroll - ScrollRandomization.current_scroll(driver)  # Altura percorrida inicial(zero)
        # print(ref_scroll)
        # print(total_scroll_height)

        if height_percentual:  # função no modo não randômico percentual de altura
            target_height = (height_percentual / 100) * total_scroll_height
        else:  # função no modo randômico de percentual da altura
            random_perc = secrets.SystemRandom().randrange(random_perc_start, random_perc_stop)
            delta_h_hgt_perc = (random_perc / 100) * total_scroll_height
            target_height = ScrollRandomization.scroll_bar_height_discount(driver, delta_h_hgt_perc)

        while delta_h <= target_height:
            # Randomização das pausas
            time_choice = secrets.SystemRandom().randrange(1, 11)
            if short_wait_start <= time_choice <= short_wait_stop:  # Randomiza pausas aleatórias curtas
                TimeRandomization.secrets_short_wait()
            elif medium_wait_start <= time_choice <= medium_wait_stop:  # Randomiza pausas aleatórias médias
                TimeRandomization.secrets_medium_wait()
            elif long_wait_start <= time_choice <= long_wait_stop:  # Randomiza pausas aleatórias longas
                TimeRandomization.secrets_long_wait()

            dy = secrets.SystemRandom().randrange(dy_start, dy_stop)  # Randomiza o quanto é rolado de uma única vez
            for j in range(dy):
                delta_h = ScrollRandomization.current_scroll(driver) - ref_scroll
                if ScrollRandomization.current_scroll(driver) <= 0:
                    return
                if delta_h >= target_height:
                    return

                #  Pressiona a seta para cima
                ActionChains(driver) \
                    .key_down(Keys.ARROW_UP) \
                    .perform()

            # Altura percorrida no término do for(Define a continuidade do while)
            delta_h = ref_scroll - ScrollRandomization.current_scroll(driver)
            # print(delta_h)

    @staticmethod
    def human_scroll_up_long_pattern(driver, height_percentual=None):
        return ScrollRandomization.human_scroll_up(driver, 10, 20, 13, 25,
                                                   3, 6, 7, 10,
                                                   7, 10, height_percentual)

    @staticmethod
    def human_scroll_up_medium_pattern(driver, height_percentual=None):
        return ScrollRandomization.human_scroll_up(driver, 5, 10, 6, 10,
                                                   1, 3, 4, 8,
                                                   9, 10, height_percentual)

    @staticmethod
    def human_scroll_up_short_pattern(driver, height_percentual=None):
        return ScrollRandomization.human_scroll_up(driver, 1, 5, 2, 5,
                                                   1, 8, 9, 9,
                                                   10, 10, height_percentual)

    @staticmethod
    def scroll_up(driver, height_percentual=None, height_in_pixels=None):
        ref_scroll = ScrollRandomization.current_scroll(driver)  # Salva a altura inicial quando a função é chamada
        total_scroll_height = ScrollRandomization.get_scroll_height(driver)  # Altura total do scroll
        # Impede a rolagem quando a página está no final
        if ref_scroll <= 0:
            return

        delta_h = ref_scroll - ScrollRandomization.current_scroll(driver)  # Altura percorrida inicial(zero)
        # print(ref_scroll)
        # print(total_scroll_height)

        if height_percentual:
            target_height = (height_percentual / 100) * total_scroll_height
        elif height_in_pixels:
            target_height = height_in_pixels
        else:
            random_perc = secrets.SystemRandom().randrange(10, 30)
            target_height = (random_perc / 100) * total_scroll_height

        while delta_h <= target_height:
            delta_h = ScrollRandomization.current_scroll(driver) - ref_scroll
            if ScrollRandomization.current_scroll(driver) <= 0:
                return
            if delta_h >= target_height:
                return

            pattern_choice = secrets.SystemRandom().randrange(1, 4)
            if pattern_choice == 1:
                ScrollRandomization.human_scroll_up_short_pattern(driver)
            elif pattern_choice == 2:
                ScrollRandomization.human_scroll_up_medium_pattern(driver)
            elif pattern_choice == 3:
                ScrollRandomization.human_scroll_up_long_pattern(driver)
        # Altura percorrida no término do for(Define a continuidade do while)
        delta_h = ref_scroll - ScrollRandomization.current_scroll(driver)
        print(delta_h)
