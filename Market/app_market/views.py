from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.views import View
from django.views.decorators.http import require_POST
from django.views.generic import ListView, DetailView
from .forms import UserRegisterForm,  LkUserForm, BasketForm
from django.contrib.auth.views import LoginView, LogoutView
from .models import *
from django.db import transaction
from django.contrib import messages
import logging

logger = logging.getLogger(__name__)
class MainPage(View):

    def get(self, request):
        return render(request, 'market/main_page.html')

class MarketView(ListView):
    model = MarketModel
    template_name = 'market/shop_list.html'
    context_object_name = 'market'



class ProductView(DetailView):
    model = MarketModel
    template_name = 'market/product.html'
    context_object_name = 'shop'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['shops'] = ProductModel.objects.filter(market__pk=self.kwargs['pk'])
        context['basket'] = BasketForm()
        return context

    def post(self, request, pk):
        basket = BasketForm(request.POST)
        if basket.is_valid():
            store = ProductModel.objects.get(id=pk)
            add = basket.save(commit=False)
            add.user = request.user
            add.quantity = basket.cleaned_data.get('quantity')
            add.product = store
            add.save()
            messages.success(request,'Товар добавлен')
            basket.save()
            logger.info(f'заказ пользователя {request.user.username} оформлен  {store}')
            return HttpResponseRedirect(reverse('market'))
        else:
            print(basket.errors)
            # messages.success(request, 'ошибка')
            # basket = BasketModel()
        return render(request, 'market/product.html', {'basket':basket})

class BasketView(View):

    def get(self, request):
        basket = BasketModel.objects.get(user=request.user)
        return render(request, 'market/basket.html', context={'basket':basket})

    def post(self, request):
        basket = BasketModel.objects.get(user=request.user)
        user_lk = LkUser.objects.get(user=request.user)
        price = basket.product.price
        product = ProductModel.objects.get(name=basket.product)

        with transaction.atomic():
            total = user_lk.balance - (price * basket.quantity)
            user_lk.balance = total
            user_lk.save()
            logger.info(f'С баланса {request.user.username} списано {total} заказаз оплачен')
            stock = product.in_stock - basket.quantity
            product.in_stock = stock
            product.save()
            BasketModel.objects.get(user=request.user).delete()
            messages.success(request, 'Покупка успешна')
        return HttpResponseRedirect(reverse('profile'))




class RegisterUser(View):

    def get(self, request):
        if request.user.is_authenticated:
            return HttpResponseRedirect(reverse('profile'))
        user_form = UserRegisterForm()
        return render(request, 'market/register.html', context={'user_form':user_form})

    def post(self, request):
        user_form = UserRegisterForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            LkUser.objects.create(user=new_user)
            return render(request, 'market/register_ok.html', context={'new_user':new_user})
        return render(request, 'market/register.html', context={'user_form': user_form})




class Login(LoginView):
    logger.info(f'Пользователь  вошел в систему')
    template_name = 'market/login.html'

class Logout(LogoutView):
    next_page = '/'


class UserLkView(View):


    def get(self, request):
        user = LkUser.objects.filter(user=request.user)
        return render(request, 'market/profile.html', context={'user':user})


class AddBalance(View):

    def get(self, request):
        if request.user.is_authenticated:
            form = LkUserForm()
            return render(request, 'market/add_balance.html', {'form':form})
        else:
            return redirect('login')


    def post(self, request):
        if request.method == 'POST' and request.user.is_authenticated:
            lk_user = LkUser.objects.get(user=request.user)
            # form = LkForm(request.POST, instance=user)
            form = LkUserForm(request.POST)
            if form.is_valid():
                lk_user.balance += form.cleaned_data['balance']
                lk_user.update_status()
                lk_user.save()
                logger.info(f'Баланс пользователя {request.user.username} пополнен на {form.cleaned_data["balance"]}')
                logger.info(f'Пользователь {request.user.username} у него статус {lk_user.status}')
                return redirect('profile')
        else:
            form = LkUserForm()
        return render(request, 'market/add_balance.html', {'form': form})

