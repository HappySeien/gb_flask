from flask_combo_jsonapi import ResourceList, ResourceDetail

from services.extension import db
from services.models import Tag
from services.api.schemas import TagSchema


class TagList(ResourceList):
    schema = TagSchema
    data_layer = {
        'session': db.session,
        'model': Tag,
    }


class TagDetail(ResourceDetail):
    schema = TagSchema
    data_layer = {
        'session': db.session,
        'model': Tag,
    }
