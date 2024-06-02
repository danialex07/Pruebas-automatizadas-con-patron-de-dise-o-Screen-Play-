class CatalogUi:
    def __init__(self):
        self.page_title = '//*[@id="header_container"]/div[1]/div[2]/div'  # Selector XPath para el título de la página del catálogo

    def get_product_by_name(self, product_name):
        return f'//*[@id="inventory_item_container"]//div[contains(text(), "{product_name}")]'
