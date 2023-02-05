from menu.models import MenuItem, MultiLangText

all_cocktails = [
    MenuItem(
        name=MultiLangText(
            eng='ABSOLUT with juice',
            ru='ABSOLUT c соком',
            kz='Шырын қосылған ABSOLUTE'
        ),
        price=2000,
        item_id='absolut_j'
    ),
    MenuItem(
        name=MultiLangText(
            eng='JAMESON with juice',
            ru='JAMESON с соком',
            kz='Шырын қосылған JAMESON'
        ),
        price=2000,
        item_id='jameson_j'
    ),
    MenuItem(
        name=MultiLangText(
            eng='Gin and tonic',
            ru='ДЖИН ТОНИК',
            kz='Джин және тоник'
        ),
        price=2000,
        item_id='gin_ton'
    ),
    MenuItem(
        name=MultiLangText(
            eng='Rum with mint soda 🥃',
            ru='РОМ с мятной содовой 🥃',
            kz='Жалбыз содасы бар ром 🥃'
        ),
        price=2000,
        item_id='rom_soda'
    )
]
