from django.conf.urls import url
from django.urls import include, path

from .views import ImageParser
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Image Extractor API')

urlpatterns = [
url(r'^$', ImageParser.as_view(), name='post-file'),
]