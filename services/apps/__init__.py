from .main_app.views import index
from .article_app.views import article
from .reports_app.views import report
from .user_app.views import user

VIEWS = [
    index,
    user,
    article,
    report,
]
