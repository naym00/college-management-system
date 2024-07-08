from help.common.b_two import Two
from rest_framework import status
class One(Two):
    def addRecord(self, clsDTLS, data, **kwargs):
        # allow_fields=[], required_fields=[], unique_fields=[], choice_fields=[], regex_fields=[], extra_fields={}
        response_messages = []
        response_data = None
        response_code = status.HTTP_400_BAD_REQUEST
        infos = {}
        self.allowFields(data, response_messages, infos, kwargs)
        self.extraFields(infos, kwargs)
        self.requiredFields(response_messages, infos, kwargs)
        self.uniqueFields(clsDTLS, response_messages, infos, kwargs)
        self.choiceFields(response_messages, infos, kwargs)
        self.regexFields(response_messages, infos, kwargs)
        if not response_messages:
            serializer = clsDTLS['serializer'](data=data, many=False)
            if serializer.is_valid():
                try:
                    serializer.save()
                    response_data = serializer
                    response_code = status.HTTP_201_CREATED
                except: response_messages.append('unique combination will break!')
            else: response_messages.append('something went wrong!')
        return {
            'data': response_data,
            'messages': response_messages,
            'code': response_code
        }
        
    def updateRecord(self, clsDTLS, id, data, **kwargs):
        # allow_fields=[], unique_fields=[], choice_fields=[], regex_fields=[], extra_fields={}
        response_messages = []
        response_data = None
        response_code = status.HTTP_400_BAD_REQUEST
        
        clsdtls = clsDTLS['model'].objects.filter(id=id)
        if clsdtls.exists():
            infos = {}
            self.allowFields(data, response_messages, infos, kwargs)
            self.extraFields(infos, kwargs)
            self.uniqueFields(clsDTLS, response_messages, infos, kwargs)
            self.choiceFields(response_messages, infos, kwargs)
            self.regexFields(response_messages, infos, kwargs)
            if not response_messages:
                serializer = clsDTLS['serializer'](data=data, instance=clsdtls.first(), partial=True)
                if serializer.is_valid():
                    try:
                        serializer.save()
                        response_data = serializer
                        response_code = status.HTTP_200_OK
                    except: response_messages.append('unique combination will break!')
                else: response_messages.append('something went wrong!')
        else:
            response_messages.append('record doesn\'t exist!')
            response_code = status.HTTP_404_NOT_FOUND
        return {
            'data': response_data,
            'messages': response_messages,
            'code': response_code
        }
        
    def deleteRecord(self, clsDTLS, id, relatedOBJS=[]):
        response_messages = []
        response_data = None
        response_code = status.HTTP_400_BAD_REQUEST
        
        clsdtls = clsDTLS['model'].objects.filter(id=id)
        if clsdtls.exists():
            for item in relatedOBJS:
                if item['CLS'].objects.filter(**{item['field']: id}).exists():
                    response_messages.append(f'can\'t delete, this record is associated to {item["CLS"].__name__} Model.')
                    response_code = status.HTTP_409_CONFLICT
            if not response_messages:
                try:
                    clsdtls.delete()
                    response_code = status.HTTP_202_ACCEPTED
                except: response_messages.append('unique combination will break!')
        else:
            response_messages.append('record doesn\'t exist!')
            response_code = status.HTTP_404_NOT_FOUND
        return {
            'data': response_data,
            'messages': response_messages,
            'code': response_code
        }