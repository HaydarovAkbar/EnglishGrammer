from rest_framework.serializers import ModelSerializer
from .models import Grammer


class GrammerSerializers(ModelSerializer):
    class Meta:
        model = Grammer
        fields = ('__all__')
