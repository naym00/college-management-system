from help.common.c_three import Three
import re

class Two(Three):
    def allowFields(self, data, response_messages, infos, kwargs):
        if 'allow_fields' in kwargs:
            if isinstance(kwargs['allow_fields'], list):
                if kwargs['allow_fields']:
                    for item in kwargs['allow_fields']:
                        # {'field': 'title', 'type': 'str', 'allowed_values': 'all'}
                        if item['type'] == 'str':
                            value = data.get(item['field'])
                            if value != None:
                                if value:
                                    if isinstance(value, str):
                                        if isinstance(item['allowed_values'], list):
                                            if item['allowed_values']:
                                                if value not in item['allowed_values']:
                                                    response_messages.append(f'{item["field"]}({value}) - please choose a value from here {item["allowed_values"]}!')
                                                    value = None
                                    else:
                                        try:
                                            value = str(value)
                                            if isinstance(item['allowed_values'], list):
                                                if item['allowed_values']:
                                                    if value not in item['allowed_values']:
                                                        response_messages.append(f'{item["field"]}({value}) - please choose a value from here {item["allowed_values"]}!')
                                                        value = None
                                        except:
                                            response_messages.append(f'{item["field"]}({value}) - couldn\'t change {type(value).__name__} to {item["type"]}!')
                                            value = None
                                    if value != None: infos.update({item["field"]: value})
                        elif item['type'] == 'int':
                            value = data.get(item['field'])
                            if value != None:
                                if value:
                                    if isinstance(value, int):
                                        if isinstance(item['allowed_values'], list):
                                            if item['allowed_values']:
                                                if value not in item['allowed_values']:
                                                    response_messages.append(f'{item["field"]}({value}) - please choose a value from here {item["allowed_values"]}!')
                                                    value = None
                                    else:
                                        try:
                                            value = int(value)
                                            if isinstance(item['allowed_values'], list):
                                                if item['allowed_values']:
                                                    if value not in item['allowed_values']:
                                                        response_messages.append(f'{item["field"]}({value}) - please choose a value from here {item["allowed_values"]}!')
                                                        value = None
                                        except:
                                            response_messages.append(f'{item["field"]}({value}) - couldn\'t change {type(value).__name__} to {item["type"]}!')
                                            value = None
                                    if value != None: infos.update({item["field"]: value})
                        elif item['type'] == 'bool':
                            value = data.get(item['field'])
                            if not isinstance(value, bool):
                                if isinstance(value, str):
                                    if value.lower() in ['true', '1']: value = True
                                    elif value.lower() in ['false', '0']: value = False
                                    else:
                                        response_messages.append(f'{item["field"]}({value}) - couldn\'t change {type(value).__name__} to {item["type"]}!')
                                        value = None
                                else:
                                    if isinstance(value, int):
                                        if value == 1: value = True
                                        elif value == 0: value = False
                                        else:
                                            response_messages.append(f'{item["field"]}({value}) - couldn\'t change {type(value).__name__} to {item["type"]}!')
                                            value = None
                            if value != None: infos.update({item["field"]: value})
        else: infos.update(data)
        
    def extraFields(self, infos, kwargs):
        if 'extra_fields' in kwargs:
            if isinstance(kwargs['extra_fields'], dict):
                if kwargs['extra_fields']:
                    infos.update(kwargs['extra_fields'])
        
    def requiredFields(self, response_messages, infos, kwargs):
        if 'required_fields' in kwargs:
            if isinstance(kwargs['required_fields'], list):
                if kwargs['required_fields']:
                    for field in kwargs['required_fields']:
                        if field not in infos:
                            response_messages.append(f'{field} field is required!')
                        
    def uniqueFields(self, clsDTLS, response_messages, infos, kwargs):
        if 'unique_fields' in kwargs:
            if isinstance(kwargs['unique_fields'], list):
                if kwargs['unique_fields']:
                    for field in kwargs['unique_fields']:
                        if 'model' in clsDTLS:
                            if field in infos:
                                value = infos[field]
                                if clsDTLS['model'].objects.filter(**{field:value}).exists():
                                    response_messages.append(f'{field}({value}) is already exist!')
                        else: response_messages.append('Model is not added to clsDTLS!')
    
    def choiceFields(self, response_messages, infos, kwargs):
        if 'choice_fields' in kwargs:
            if isinstance(kwargs['choice_fields'], list):
                if kwargs['choice_fields']:
                    for item in kwargs['choice_fields']:
                        # {'field': 'title', 'values': ['employee', 'staff', 'nurse']}
                        if item['field'] in infos:
                            value = infos[item['field']]
                            if value not in item['values']: response_messages.append(f'{item["field"]}({value}) field\'s allowed values are {item["values"]}')
                            
    def regexFields(self, response_messages, infos, kwargs):
        if 'regex_fields' in kwargs:
            if isinstance(kwargs['regex_fields'], list):
                if kwargs['regex_fields']:
                    # print(kwargs['regex_fields'])
                    for item in kwargs['regex_fields']:
                        # {'field': 'title', 'type': 'email'}
                        if item['field'] in infos:
                            value = infos[item['field']]
                            response = self.getRegex(item['type'])
                            if response['flag']:
                                rematch = re.search(response['data']['regex'], value)
                                if not bool(rematch):
                                    response_messages.append(f'{item["field"]}({value}) field\'s value format is {response["data"]["format"]}!')
                            else:
                                if response['message']:
                                    response_messages.extend([f'{item["field"]}({value}) {message}' for message in response['message']])