class BasePage():   #class
    def __init__(self, browser, url):   #конструктор — метод, который вызывается, когда мы создаем объект в него в качестве параметра передаем экземпляр драйвера и урл
        self.browser = browser  #сохраняем как атрибуты класса
        self.url = url
    def open(self):   # открываet нужную страницу в браузере, используя метод get().
        self.browser.get(self.url)  #реализация метода
