from flask import Flask

app = Flask(__name__)

from services.apps.main_app import views
