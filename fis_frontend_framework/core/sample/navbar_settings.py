from django.conf import settings

brand = {
    'render_brand': True,
    'image_link': settings.STATIC_URL + 'fis_frontend_framework/ut-brand.png'
}

left_navbar = [
    {
        'dropdown': False,
        'class': 'active',
        'href': '#',
        'label': 'Navbar active link',
    },
    {
        'dropdown': False,
        'class': '',
        'href': '#',
        'label': 'Navbar link',
    },
    {
        'dropdown': False,
        'class': '',
        'href': '#',
        'label': 'Navbar link',
    },
    {
        'dropdown': True,
        'dropdown_main_href': '#',
        'dropdown_main_label': 'Dropdown menu',
        'class': '',
        'href': '#',
        'label': 'HelloDropdown',
        'dropdown_list_items': [
            {
                'role': '',
                'class': 'dropdown-header',
                'href': '#',
                'label': 'Dropdown header',
            },
            {
                'role': '',
                'class': '',
                'href': '#',
                'label': 'Dropdown item',
            },
            {
                'role': 'separator',
                'class': 'divider',
                'href': '#',
                'label': '',
            },
            {
                'role': '',
                'class': '',
                'href': '#',
                'label': 'Dropdown item',
            },
            {
                'role': '',
                'class': '',
                'href': '#',
                'label': 'Dropdown item',
            },
            {
                'role': '',
                'class': '',
                'href': '#',
                'label': 'Dropdown item',
            },
            {
                'role': '',
                'class': '',
                'href': '#',
                'label': 'Dropdown item',
            },
            {
                'role': 'separator',
                'class': 'divider',
                'href': '#',
                'label': '',
            },
            {
                'role': '',
                'class': '',
                'href': '#',
                'label': 'Dropdown item',
            },
            {
                'role': '',
                'class': '',
                'href': '#',
                'label': 'Dropdown item',
            },
        ]
    }
]

right_navbar = [
    {
        'dropdown': False,
        'class': '',
        'href': '#',
        'label': 'Navbar link',
    },
    {
        'dropdown': False,
        'class': '',
        'href': '#',
        'label': 'Navbar link',
    },
    {
        'dropdown': False,
        'class': '',
        'href': '#',
        'label': 'Navbar link',
    },
    {
        'dropdown': True,
        'dropdown_main_href': '#',
        'dropdown_main_label': 'Dropdown menu',
        'class': '',
        'href': '#',
        'label': 'HelloDropdown',
        'dropdown_list_items': [
            {
                'role': '',
                'class': '',
                'href': '#',
                'label': 'Dropdown item',
            },
            {
                'role': '',
                'class': '',
                'href': '#',
                'label': 'Dropdown item',
            },
            {
                'role': 'separator',
                'class': 'divider',
                'href': '#',
                'label': '',
            },
            {
                'role': '',
                'class': '',
                'href': '#',
                'label': 'Dropdown item',
            },
            {
                'role': '',
                'class': '',
                'href': '#',
                'label': 'Dropdown item',
            },
            {
                'role': '',
                'class': '',
                'href': '#',
                'label': 'Dropdown item',
            },
            {
                'role': '',
                'class': '',
                'href': '#',
                'label': 'Dropdown item',
            },
            {
                'role': 'separator',
                'class': 'divider',
                'href': '#',
                'label': '',
            },
            {
                'role': '',
                'class': '',
                'href': '#',
                'label': 'Dropdown item',
            },
            {
                'role': '',
                'class': '',
                'href': '#',
                'label': 'Dropdown item',
            },
        ]
    }
]

number_of_navbar_items = len(left_navbar) + len(right_navbar)

navbar = {
    'render_navbar': True,
    'brand': brand,
    'number_of_navbar_items': number_of_navbar_items,
    'left_navbar_items': left_navbar,
    'right_navbar_items': right_navbar,
}