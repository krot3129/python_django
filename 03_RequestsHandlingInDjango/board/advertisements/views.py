from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView

class Main_page(View):

    def get(self, requests):
        return render(requests, 'advertisements/main_page.html')


# def advertisement_list(request, *args, **kwargs):
#
#     advertisements_1 = [
#         'Мастер на час',
#         'Выведение из запоя',
#         'Услуги экскаватора-погрузчика, гидромолота, ямобура'
#     ]
#     return render(request, 'advertisements/advertisement_list.html', {'advertisements_1': advertisements_1})

class Advertisements(View):

    def get(self, requests):
        advertisements = [
            'Мастер на час',
            'Выведение из запоя',
            'Услуги экскаватора-погрузчика, гидромолота, ямобура'
        ]
        return render(requests, 'advertisements/advertisements.html', {'advertisements':advertisements})

class Contacts(TemplateView):
    template_name = 'advertisements/contacts.html'

    def get_context_data(self, **kwargs):
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
    template_name = 'advertisements/about.html'

    def get_context_data(self, **kwargs):
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