from django.conf.urls.static import static
from .views import CharactorCreaterView, CharactorListView, CharactorUpdateView
from django.conf import settings
from django.urls import path
from django.conf.urls import url


urlpatterns = [
    path('create/', CharactorCreaterView.as_view(), name='create'),
    path('list/', CharactorListView.as_view(), name='list'),
    path('update/<int:pk>', CharactorUpdateView.as_view(), name='update'),
    # �p�X�w��Ȃ��Ń��[�g�f�B���N�g���ɃA�N�Z�X������
    url(r'^$',  CharactorListView.as_view(),
        name='list'),
    # ���[�g�f�B���N�g���ȊO
    url(r'',  CharactorListView.as_view(), name='list'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
