from django.conf.urls import include, url
from django.contrib import admin
from rest_framework import routers

from api import views

router = routers.DefaultRouter()
router.register(r'parkingviolations', views.ParkingViolationSet)


urlpatterns = [
    # Examples:
    # url(r'^$', 'dctraffic_project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^', include(router.urls)),
    url(r'^api/v1/', include('rest_framework.urls', namespace='rest_framework')),

    url(r'^admin/', include(admin.site.urls)),
]
