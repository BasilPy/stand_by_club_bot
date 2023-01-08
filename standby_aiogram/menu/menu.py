from stand_by_club_bot.standby_aiogram.menu.cocktails import all_cocktails
from stand_by_club_bot.standby_aiogram.menu.models import Menu, MenuCategory, MultiLangText
from stand_by_club_bot.standby_aiogram.menu.tinctures import all_tinctures

menu = Menu(
    categories=[
        MenuCategory(
            category_name='cocktails',
            instruction=MultiLangText(
                eng='Choose a cocktail 🍸 400мл:',
                ru='Выберите коктейль 🍸 400мл:',
                kz='Коктейльді таңдаңыз 🍸 400мл:',
            ),
            category_items=all_cocktails,
        ),
        MenuCategory(
            category_name='tinctures',
            instruction=MultiLangText(
                eng='Choose a tincture ◇ 50мл:',
                ru='Выберите настойку ◇ 50мл:',
                kz='Тұнбаны таңдаңыз ◇ 50мл:',
            ),
            category_items=all_tinctures,
        ),
    ]
)
