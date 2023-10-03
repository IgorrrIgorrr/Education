import random


class EmailValidator:
    ls = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_.@"

    def __new__(cls, *args, **kwargs):
        return None

    @classmethod
    def get_random_email(cls):
        em = "."
        # while len(em) < 100:
        for i in range(random.randint(5, 99)):
            ls = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_"
            a = random.randint(0, 63)
            em += ls[a]
        em += "@."
        for i in range(random.randint(1, 49)):
            ls = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_"
            b = random.randint(0, 62)
            em += ls[b]

    @classmethod
    def check_email(cls, email):
        if set(cls.em) < set(cls.ls) and cls.em.count("@") == 1:
            return True

    @staticmethod
    def __is_email_str(email):
        return type(email) is str
