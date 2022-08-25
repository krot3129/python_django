import datetime

class Ip_log:

    def __init__(self, get_responce):
        self.META = None
        self.get_responce = get_responce

    def __call__(self, requests):
        responce = self.get_responce(requests)
        x_forwarded_for = requests.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[-1].strip()
        else:
            ip = requests.META.get('REMOTE_ADDR')
        with open('IP_log', 'a', encoding='utf-8') as file:
            date = datetime.datetime
            file.write(str(date))
            file.write(ip)
        return responce





