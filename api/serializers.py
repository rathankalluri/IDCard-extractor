from rest_framework import serializers
from .models import FileMeta

class FileSerializer(serializers.ModelSerializer):
  #image = serializers.FileField(max_length=None,use_url=True)
  class Meta():
    model = FileMeta
    fields = ('file',)