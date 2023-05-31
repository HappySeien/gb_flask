from flask_combo_jsonapi import ResourceList, ResourceDetail

from services.extension import db
from services.models import User
from services.api.schemas import UserSchema

from services.api.permissions.user import UserListPermission, UserPatchPermission


class UserList(ResourceList):
    schema = UserSchema
    data_layer = {
        'session': db.session,
        'model': User,
        'permission_get': [UserListPermission],
    }


class UserDetail(ResourceDetail):
    schema = UserSchema
    data_layer = {
        'session': db.session,
        'model': User,
        'permission_patch': [UserPatchPermission],
    }
