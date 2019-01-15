from . import views
from django.conf.urls import url
from rest_framework import routers

router = routers.DefaultRouter(trailing_slash=False)

urlpatterns = [
    url(r'/calculate_product_tax', views.calculate),
]


urlpatterns += router.urls
