from framework import struct
from framework import lib


class MainPage(lib.Pages.PageWithTitle):
    def __init__(self, book):
        super().__init__(book, '演示应用')
        self.add_element(lib.Elements.TextElement(self, (40, 40), '演示应用, 可以在这里添加一些文字'))


class MainBook(struct.Book):
    def __init__(self, app):
        super().__init__(app)
        self.add_page("main", MainPage(self))


class Application(lib.AppBase):
    def __init__(self, env):
        super().__init__(env)
        self.name = '演示应用'
        self.add_book("main", MainBook(self))
