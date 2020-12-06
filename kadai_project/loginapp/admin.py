from django.contrib import admin

from loginapp.models import KimetsuCharactorModel, SexModel


class KimetsuCharactorAdmin(admin.ModelAdmin):
    """鬼滅の刃キャラクターModel用"""
    list_display = ['name', 'sex_id', 'characteristic', 'create_dt']


class SexModelAdmin(admin.ModelAdmin):
    """性別マスタModel用
    ※勉強の為、マスタ用テ－ブルを作成しました。
    わざわざ作成しなくても良かったですが、
    テーブル間のリレーション処理がよくわからないので、後々の勉強用に作成しました。
    """
    list_display = ['sex_id', 'value', 'create_dt']


admin.site.register(KimetsuCharactorModel, KimetsuCharactorAdmin)
admin.site.register(SexModel, SexModelAdmin)
