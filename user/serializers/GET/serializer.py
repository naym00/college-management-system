from rest_framework import serializers
from user import models as MODELS_USER

class Usertypeserializer(serializers.ModelSerializer):
    class Meta:
        model =MODELS_USER.Usertype
        fields='__all__'

class Userserializer(serializers.ModelSerializer):
    class Meta:
        model =MODELS_USER.User
        fields='__all__'
        
class Photoserializer(serializers.ModelSerializer):
    class Meta:
        model =MODELS_USER.Photo
        fields='__all__'
        
class Profilepicserializer(serializers.ModelSerializer):
    class Meta:
        model =MODELS_USER.Profilepic
        fields='__all__'
        
class Coverphotoserializer(serializers.ModelSerializer):
    class Meta:
        model =MODELS_USER.Coverphoto
        fields='__all__'