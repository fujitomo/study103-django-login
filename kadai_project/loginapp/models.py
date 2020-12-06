from django.db import models
from datetime import datetime


class SexModel(models.Model):
    """性別マスタModel
    ※勉強の為、マスタ用テ－ブルを作成しました。
    わざわざ作成しなくても良かったですが、
    テーブル間のリレーション処理がよくわからないので、後々の勉強用に作成しました。
    """
    sex_id = models.CharField(unique='true', max_length=1)
    value = models.CharField(max_length=10, verbose_name="性別ID")
    create_dt = models.DateTimeField(default=datetime.now)

    def __str__(self):
        """ 管理画面の表示名 """
        return self.value

    class Meta:
        # 管理画面で表示される名前
        verbose_name = "性別マスタ"
        verbose_name_plural = "性別マスタ"


class KimetsuCharactorModel(models.Model):
    """鬼滅の刃キャラクターModel"""
    # 名前
    name = models.CharField(max_length=30, verbose_name="名前")
    # 性別
    sex_id = models.ForeignKey(
        SexModel, on_delete=models.CASCADE, verbose_name="性別ID")
    # 特徴
    characteristic = models.CharField(
        max_length=300, verbose_name="特徴")

    # 画像
    image = models.ImageField(
        upload_to='images/', null=True, verbose_name="イメージ画像")

    # 更新日
    create_dt = models.DateTimeField(
        default=datetime.now, verbose_name="更新日")

    def __str__(self):
        """ 管理画面の表示名 """
        return self.name

    class Meta:
        # 管理画面で表示される名前
        verbose_name = "鬼滅の刃キャラクター"
        verbose_name_plural = "鬼滅の刃キャラクター"
        # 複合主キー
        unique_together = (("name", "sex_id"))
