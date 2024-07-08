class Validators:
    def regexs(self):
        return {
            'phonenumber': {
                'regex': '^01[3456789]{1}[0-9]{8}$',
                'format': '01700000000',
                'message': []
            },
            'date': {
                'regex': '^[0-9]{4}-[0-9]{2}-[0-9]{2}$',
                'format': '2024-01-01',
                'message': []
            },
            'email': {
                'regex': '^[a-z._]*[0-9]*@[a-z]*.[a-z]*$',
                'format': 'example@example.com',
                'message': []
            }
        }
        
    def getRegex(self, type):
        response = {'flag': False, 'message': [], 'data': None}
        if isinstance(type, str):
            regexs = self.regexs()
            if type in regexs:
                response['flag'] = True
                response['data'] = regexs[type]
            else: response['message'].append(f'No regex type exist with this name({type})!')
        else: response['message'].append(f'{type}\'s data type should be str!')
        return response