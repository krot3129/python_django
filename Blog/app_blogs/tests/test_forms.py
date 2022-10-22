from django.contrib.auth.models import User
from django.test import TestCase, Client
from ..forms import ProfileForm

class Setup_class(TestCase):

    def setUp(self) -> None:
        self.user = User.objects.create_user(username='TestUser', email='test@test.ru')
        self.user.set_password('qwerty12345')
        self.user.save()
        self.client.login(username=self.user.username, password=self.user.password)

    def test_user_form(self):
        form = ProfileForm(data={
            'first_name':'usserstesting',
            'last_name':'test',
            'about':'some  user',
            'email':'test@test.ru',
            'city':'rostov'
        })


        self.assertTrue(form.is_valid())




