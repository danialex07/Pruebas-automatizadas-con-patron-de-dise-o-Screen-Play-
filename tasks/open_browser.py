class OpenBrowser:
    def __init__(self, url):
        self.url = url

    def perform_as(self, actor):
        actor.browser.visit(self.url)
