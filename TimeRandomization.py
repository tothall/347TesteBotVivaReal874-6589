import time
import random
import secrets


class TimeRandomization:

    @staticmethod
    def random_time_actions():
        return time.sleep(random.uniform(0.8, 1.7))

    @staticmethod
    def medium_wait():
        return time.sleep((random.uniform(1.9, 3.4)))

    @staticmethod
    def long_wait():
        return time.sleep((random.uniform(4.1, 5)))

    @staticmethod
    def very_long_wait():
        return time.sleep((random.uniform(9.7, 14.9)))

    @staticmethod
    def temp(start_time):
        return time.time() - start_time

    @staticmethod
    def secrets_random_wait(floor, ceiling):
        len_ = (ceiling - floor) + 1
        seq = [0] * len_
        seq[0] = floor
        #print(seq[0])
        for i in range(1, len_):
            seq[i] = seq[i - 1] + 1

        seconds = secrets.choice(seq) / 10
        return time.sleep(seconds)

    @staticmethod
    def secrets_short_wait():
        return TimeRandomization.secrets_random_wait(8, 17)

    @staticmethod
    def secrets_medium_wait():
        return TimeRandomization.secrets_random_wait(19, 34)

    @staticmethod
    def secrets_long_wait():
        return TimeRandomization.secrets_random_wait(41, 50)

    @staticmethod
    def secrets_very_long_wait():
        return TimeRandomization.secrets_random_wait(41, 78)












