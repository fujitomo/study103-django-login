import django_tables2 as tables
from .models import KimetsuCharactorModel
import django_tables2 as tables


class KimetsuCharactorTable(tables.Table):
    """鬼滅の刃キャラクターForm用"""

    class Meta:
        model = KimetsuCharactorModel
        template_name = "tables.html"
        fields = ("name", "sex_id.value", "characteristic", "image")
        row_attrs = {
            'id': lambda record: record.id,
            'name': lambda record: record.name,
            'sex_id': lambda record: record.sex_id.value,
            'characteristic': lambda record: record.characteristic,
            'image': lambda record: record.image,
        }
