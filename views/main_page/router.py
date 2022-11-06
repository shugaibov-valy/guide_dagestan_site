from views.main_page import views


def install(app):
    app.add_url_rule(
        '/main',
        view_func=views.MainPageView.as_view('main-page')
    )