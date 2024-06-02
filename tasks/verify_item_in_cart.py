class VerifyItemInCart:
    def perform_as(self, actor):
        cart_badge = actor.browser.find_by_css('.shopping_cart_badge')
        assert cart_badge and int(cart_badge.text) > 0
