from rest_framework.decorators import api_view
from rest_framework.response import Response
from user.serializers.GET import serializer as GSLZR_USER
from user.serializers.POST import serializer as PSLZR_USER
from rest_framework import status
from user import models as MODELS_USER
from help.common.a_one import One as HELP
from help.choices import generic as CHOICE

@api_view(['GET'])
def getUsertype(request):
    usertype = MODELS_USER.Usertype.objects.all()
    usertypeserializers = GSLZR_USER.Usertypeserializer(usertype, many=True)
    return Response(usertypeserializers.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def addUsertype(request):
    response_data = {}
    clsDTLS = {
        'model': MODELS_USER.Usertype,
        'serializer': PSLZR_USER.Usertypeserializer
    }
    allow_fields = [
        {'field': 'title', 'type': 'str', 'allowed_values': []},
        {'field': 'description', 'type': 'str', 'allowed_values': []}
    ]
    required_fields = ['title']
    unique_fields = ['title']
    response = HELP().addRecord(
        clsDTLS,
        request.data,
        allow_fields=allow_fields,
        required_fields=required_fields,
        unique_fields=unique_fields
    )
    if response['data']: response_data = response['data'].data
    return Response({'data': response_data, 'messages': response['messages']}, status=response['code'])


@api_view(['PUT'])
def updateUsertype(request, usertypeid=None):
    response_data = {}
    clsDTLS = {
        'model': MODELS_USER.Usertype,
        'serializer': PSLZR_USER.Usertypeserializer
    }
    allow_fields = [
        {'field': 'title', 'type': 'str', 'allowed_values': []},
        {'field': 'description', 'type': 'str', 'allowed_values': []}
    ]
    unique_fields = ['title']
    response = HELP().updateRecord(
        clsDTLS,
        usertypeid,
        request.data,
        allow_fields=allow_fields,
        unique_fields=unique_fields
    )
    if response['data']: response_data = response['data'].data
    return Response({'data': response_data, 'messages': response['messages']}, status=response['code'])

@api_view(['DELETE'])
def deleteUsertype(request, usertypeid=None):
    response_data = {}
    clsDTLS = {
        'model': MODELS_USER.Usertype,
        'serializer': PSLZR_USER.Usertypeserializer
    }
    relatedOBJS = [
        {'CLS': MODELS_USER.User, 'field': 'type', 'records': []},
    ]
    response = HELP().deleteRecord(clsDTLS, usertypeid, relatedOBJS=relatedOBJS)
    return Response({'data': response_data, 'messages': response['messages']}, status=response['code'])


@api_view(['GET'])
def getUser(request):
    users = MODELS_USER.User.objects.all()
    userserializers = GSLZR_USER.Userserializer(users, many=True)
    return Response(userserializers.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def addUser(request):
    response_data = {}
    clsDTLS = {
        'model': MODELS_USER.User,
        'serializer': PSLZR_USER.Userserializer
    }
    required_fields = ['username']
    unique_fields = ['phone', 'username', 'email']
    choice_fields = [
        {'field': 'gender', 'values': [each[1] for each in CHOICE.GENDER]},
        {'field': 'homedistrict', 'values': [each[1] for each in CHOICE.DISTRICTS]},
        {'field': 'currentdistrict', 'values': [each[1] for each in CHOICE.DISTRICTS]}
    ]
    regex_fields = [
        {'field': 'birthdate', 'type': 'date'},
        {'field': 'phone', 'type': 'phonenumber'},
        {'field': 'email', 'type': 'email'},
    ]
    response = HELP().addRecord(
        clsDTLS,
        request.data,
        required_fields=required_fields,
        unique_fields=unique_fields,
        choice_fields=choice_fields,
        regex_fields=regex_fields
    )
    if response['data']: response_data = response['data'].data
    return Response({'data': response_data, 'messages': response['messages']}, status=response['code'])
