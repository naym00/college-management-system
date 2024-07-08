from django.contrib import admin
from user import models as MODELS_USER

admin.site.register([
    MODELS_USER.Usertype,
    MODELS_USER.User,
    MODELS_USER.Photo,
    MODELS_USER.Profilepic,
    MODELS_USER.Coverphoto
])