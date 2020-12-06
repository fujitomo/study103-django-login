from django.conf.urls.static import static
from .views import CharactorCreaterView, CharactorListView, CharactorUpdateView, Login, Logout
from django.conf import settings
from django.urls import path
from django.conf.urls import url


urlpatterns = [
    path('create/', CharactorCreaterView.as_view(), name='create'),
    path('list/', CharactorListView.as_view(), name='list'),
    path('update/<int:pk>', CharactorUpdateView.as_view(), name='update'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    # ルート
    url(r'^$',  Logout.as_view(), name='login'),
    # url(r'',  CharactorListView.as_view(), name='list'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
