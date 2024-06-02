class VerifyCartButton:
    def __init__(self, item_id):
        self.item_id = item_id

    def perform_as(self, actor):
        button = actor.browser.find_by_id(f'remove-{self.item_id}')
        assert button.text == "Remove"
