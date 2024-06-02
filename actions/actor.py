from splinter import Browser

class Actor:
    def __init__(self, name):
        self.name = name
        self.browser = Browser()

    def can(self, task):
        task.perform_as(self)

    def quit(self):
        self.browser.quit()
