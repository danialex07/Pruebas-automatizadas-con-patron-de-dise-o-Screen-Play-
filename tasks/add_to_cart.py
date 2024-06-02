class AddToCart:
    def __init__(self, item_id):
        self.item_id = item_id

    def perform_as(self, actor):
        button = actor.browser.find_by_id(f'add-to-cart-{self.item_id}')
        button.click()
