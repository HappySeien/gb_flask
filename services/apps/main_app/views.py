from services.apps.main_app import app


@app.route('/')
def index():
    return 'Test page'
