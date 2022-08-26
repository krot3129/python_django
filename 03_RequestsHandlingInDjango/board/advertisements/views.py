from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView
from django.http import HttpResponseRedirect

class Main_page(View):
    """
    Класс который описывает вид главной страницы сайта
    """

    def get(self, requests):
        return render(requests, 'advertisements/main_page.html')

    def post(self, requests):
        return render(requests, 'advertisements/main_page.html')


class Advertisements(View):
    """
    Класс описывающий страницу с объявлениями.
    """

    def get(self, requests):
        """
        Метод который передает данные согласно запросу

        :param requests:
        :return:
        advertisements: Список с доступными услугами.
        """
        advertisements = [
            'Мастер на час',
            'Выведение из запоя',
            'Услуги экскаватора-погрузчика, гидромолота, ямобура'
        ]
        return render(requests, 'advertisements/advertisements.html', {'advertisements':advertisements})

    def post(self, requests):
        return render(requests, 'advertisements/advertisements.html')



class Contacts(TemplateView):
    """
    Класс описывающий страницу связи с администрацией сайта
    """
    template_name = 'advertisements/contacts.html'

    def get_context_data(self, **kwargs):
        """
        Метод который передает данные согласно запросу
        :param kwargs:
        :return: Context Данные для передачи представлений в HTML страницу
        """
        context = super().get_context_data(**kwargs)
        context['name'] = 'Информация для обратной связи'
        context['title'] = 'Контакты'
        context['description'] = """
        Если у вас есть какие-то вопросы, пожалуйста, не стесняйтесь и напишите мне.
        Если вы не получили немедленный ответ, это значит, что я путешествую где-то у черта на куличках. Я отвечу, как только смогу. 
        Обещаю!
        """
        context['phone'] = 'Телефон для связи 8-800-000-000'
        context['email'] = 'email: Sergey@sergey.ru'
        return context

class About(TemplateView):
    """
    Класс описывающий страницу с информацией о компании
    """
    template_name = 'advertisements/about.html'
    count = 0

    def get_context_data(self, **kwargs):
        """
        Метод который передает данные согласно запросу
        :param kwargs:
        :return: Context Данные для передачи представлений в HTML страницу
        """
        context = super().get_context_data(**kwargs)
        context['title'] = 'Информация о компании'
        context['name'] = 'Рады приветствовать вас на сайте нашей компании'
        context['description'] = """
        Продаете много товаров?
        Оказываете услуги и ищете клиентов?
        Хотите выйти на новую аудиторию?

        Мы сделали удобный сервис для предпринимателей, который помогает развивать бизнес и зарабатывать больше.
        """
        return context

    def post(self, request, *args, **kwargs):

        return HttpResponseRedirect('about', self.template_name, 'Данные обновлены')
