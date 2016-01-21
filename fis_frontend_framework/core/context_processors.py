from django.contrib.staticfiles.templatetags.staticfiles import static


def fis_framework(request):
    framework_context_dict = {
        'css_files': (
            static('fis_frontend_framework/jquery-ui/jquery-ui.css'),
            static('fis_frontend_framework/bootstrap-custom.css'),
            static('fis_frontend_framework/navbar.css'),
            static('fis_frontend_framework/footer.css'),
        ),
        'js_files': (
            'https://ajax.googleapis.com/ajax/libs/jquery/2.1.4/jquery.min.js',
            static('fis_frontend_framework/jquery-ui/jquery-ui.js'),
            static('fis_frontend_framework/bootstrap.js'),
            static('fis_frontend_framework/main.js'),
        ),
    }

    return {
        'fis_framework': framework_context_dict,
    }