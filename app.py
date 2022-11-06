from flask import Flask


def make_app() -> Flask:
   from views.main_page import router as main_router

    # Initialization the app application
   app = Flask(__name__)
   main_router.install(app)

   app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
   return app
