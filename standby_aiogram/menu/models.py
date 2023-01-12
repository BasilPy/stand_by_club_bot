class MultiLangText:
    eng = None
    ru = None
    kz = None

    def __init__(self, eng, ru, kz):
        self.eng = eng
        self.ru = ru
        self.kz = kz

    def get_text_by_language(self, lang):
        match lang:
            case 'eng':
                return self.eng
            case 'ru':
                return self.ru
            case 'kz':
                return self.kz

class MenuItem:
    name: MultiLangText = None
    price: float = None
    item_id = None

    def __init__(self, name, price, item_id):
        self.name = name
        self.price = price
        self.item_id = item_id


class MenuCategory:
    category_name: str = None
    instruction: MultiLangText = None
    category_items: list[MenuItem] = None

    def __init__(self, category_name, instruction, category_items):
        self.category_name = category_name
        self.instruction = instruction
        self.category_items = category_items


class Menu:
    categories: list[MenuCategory] = None

    def __init__(self, categories):
        self.categories = categories

