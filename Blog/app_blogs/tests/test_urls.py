from django.test import TestCase
from http import HTTPStatus
from django.urls import reverse, resolve
from ..views import BlogDetail

class BlogpagesTest(TestCase):

    def test_blog_urls_and_status(self):
        """
        Тест на проверку Главной страницы и использование шаблона главной страницы.

        """
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'site/main_page.html')

    def test_blog_list_urls(self):
        """
        Тест на проверку страницы записей и использование шаблона.
        """
        responce = self.client.get('/blog_list')
        self.assertEqual(responce.status_code, 200)
        self.assertTemplateUsed(responce, 'site/blog_list.html')

    def test_is_login_page(self):
        """
        Тест на проверку страницы входа, с последующим перенаправлением.
        Проверка использоваемого шаблона

        """
        response = self.client.get('/login', follow=True)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, 'site/login.html')

    def test_is_register_page(self):
        """
        Тест на проверку страницы регистрации, а так же используемого шаблона.
        """
        response = self.client.get('/register')
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, 'site/register.html')

    def test_upload_cvs_url(self):
        """
        Тест на проверку страницу загрузки cvs файла
        """
        response = self.client.get('/update_post')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'site/upload_cvs.html')

    def test_detail_url(self):
        """
        Тест на проверку страницы детального отображения поста
        """
        url = reverse('blog_detail', args=[1])
        self.assertEqual(resolve(url).func.view_class, BlogDetail)
