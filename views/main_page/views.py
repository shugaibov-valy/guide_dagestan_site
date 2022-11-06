from flask import render_template, request
from flask.views import MethodView


class MainPageView(MethodView):
    def get(self):
        return render_template("pages/main_page/index.html")

    def post(self):
        login = request.form.get("login")
        password = request.form.get("password")
        print(login, password)
        return render_template("pages/main_page/index.html")