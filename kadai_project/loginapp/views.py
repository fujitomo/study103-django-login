from django_tables2 import SingleTableView

from .models import KimetsuCharactorModel
from django.views.generic import CreateView
from django.urls import reverse_lazy
from .forms import KimetsuCharactorForm, LoginForm
from .tables import KimetsuCharactorTable  # new

from django.views.generic.edit import UpdateView
from django.urls import reverse
from django.contrib.auth.views import LoginView, LogoutView


class CharactorCreaterView(CreateView):
    """鬼滅の刃キャラクター登録View"""
    model = KimetsuCharactorModel
    form_class = KimetsuCharactorForm
    template_name = 'create.html'
    success_url = reverse_lazy('list')


class CharactorUpdateView(UpdateView):
    """鬼滅の刃キャラクター更新View"""
    template_name = 'update.html'
    model = KimetsuCharactorModel
    form_class = KimetsuCharactorForm
    success_url = reverse_lazy('list')

    # 更新画面を再表示
    # def get_success_url(self):
    #    return reverse('update', kwargs={'pk': self.object.pk})


class CharactorListView(SingleTableView):
    """鬼滅の刃キャラクター一覧View"""

    model = KimetsuCharactorModel
    table_class = KimetsuCharactorTable
    table_data = KimetsuCharactorModel.objects.all()
    template_name = 'list.html'
    # 1ページに表示される上限
    table_pagination = {
        'per_page': 3,
    }


class Login(LoginView):
    """ログインページ"""
    form_class = LoginForm
    template_name = 'login.html'


class Logout(LogoutView):
    """ログアウトページ"""
    template_name = 'login.html'
