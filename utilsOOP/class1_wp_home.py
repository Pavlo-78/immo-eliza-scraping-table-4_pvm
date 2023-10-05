

# створюємо клас веб сторінки
class w_page():
        def __init__(self, desc, url):
            self.__desc=desc
            self.__url=url
        
        @property
        def desc(self): return self.__desc

        @property
        def url(self): return self.__url

        @property
        def info(self): return f'{self.__desc}, {self.__url}'

