from django import forms
from .models import KimetsuCharactorModel, SexModel
from .widgets import FileInputWithPreview
from django.contrib.auth.forms import AuthenticationForm


class KimetsuCharactorForm(forms.ModelForm):
    """鬼滅の刃キャラクターForm用"""
    name = forms.CharField(
        label='名前', max_length=30
    )

    sex_id = forms.ModelChoiceField(
        SexModel.objects, label='性別'
    )

    image = forms.ImageField(
        widget=FileInputWithPreview(include_preview=False), label='イメージ画像'
    )

    class Meta:
        model = KimetsuCharactorModel
        # TODO : このコードがないとエラーが発生する
        fields = ('name', 'sex_id', 'characteristic', 'image')
        widgets = {
            'image': FileInputWithPreview,
        }


class LoginForm(AuthenticationForm):
    """ログインフォーム"""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = field.label
