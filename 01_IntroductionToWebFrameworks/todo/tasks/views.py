from django.http import HttpResponse

from django.views import View


class ToDoView(View):

    def get(self, request, *args, **kwargs):
        return HttpResponse('<ul>'
                            '<li>Запустить сервер!</li>'
                            '<li>Понять почему суда не заходит</li>'
                            '<li>Зайти в админку, но не зайти на сайт</li>'
                            '<li>Пойти пить кофе</li>'
                            '<li>Почитать форумы и всё таки увидеть список дел</li>'
                            '</ul>')
