navbar = {}

def create_brand_item(render_brand, image_link):
    return {
        'render_brand': render_brand,
        'image_link': image_link,
    }

def create_navbar_item(html_class, href, label):
    return {
        'dropdown': False,
        'class': html_class,
        'href': href,
        'label': label,
    }

def create_dropdown_navbar_item(main_href, main_label, html_class, href, label, navbar_items_list):
    return {
        'dropdown': True,
        'dropdown_main_href': main_href,
        'dropdown_main_label': main_label,
        'class': html_class,
        'href': href,
        'label': label,
        'dropdown_list_items': navbar_items_list
    }