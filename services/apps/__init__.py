from .main_app.views import index
from .article_app.views import article
from .reports_app.views import report
from .user_app.views import user
from .auth_app.views import auth

VIEWS = [
    index,
    user,
    auth,
    article,
    report,
]
