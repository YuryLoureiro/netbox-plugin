"""
from rest_framework.serializers import ModelSerializer

from bigipnetbox.models import MyModel1


class MyModel1Serializer(ModelSerializer):

    class Meta:
        model = MyModel1
        fields = '__all__'
"""
