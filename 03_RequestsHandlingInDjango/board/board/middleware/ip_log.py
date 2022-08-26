import datetime
from django.core.exceptions import PermissionDenied

class IPLOG:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, requests):

        with open('Log_file.txt', 'a', encoding='utf-8') as file:
            file.write(str(f'datetime:{datetime.datetime.now()}\n'
                           f'URl:{requests.META.get("PATH_INFO")}\n'
                           f'HTTP:{requests.META.get("HTTP_HOST")}\n\n'))
        response = self.get_response(requests)

        return response





