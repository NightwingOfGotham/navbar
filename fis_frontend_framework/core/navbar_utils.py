navbar = {}

def create_brand_item(render_brand, image_link):
    return {
        'render_brand': render_brand,
        'image_link': image_link,
    }

def create_navbar_item(role, html_class, href, label):
    return {
        'dropdown': False,
        'role': role,       # Only for dropdown items
        'class': html_class,
        'href': href,
        'label': label,
    }

def create_dropdown_navbar_item(main_href, main_label, html_class, href, label, navbar_item_list):
    return {
        'dropdown': True,
        'dropdown_main_href': main_href,
        'dropdown_main_label': main_label,
        'class': html_class,
        'href': href,
        'label': label,
        'dropdown_list_items': navbar_item_list
    }

def create_navbar(left_navbar_items_list, right_navbar_items_list, brand_item):

    number_of_navbar_items = len(left_navbar_items_list) + len(right_navbar_items_list)

    return {
        'render_navbar': True,
        'brand': brand_item,
        'number_of_navbar_items': number_of_navbar_items,
        'left_navbar_items': left_navbar_items_list,
        'right_navbar_items': right_navbar_items_list,
    }