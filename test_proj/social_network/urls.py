from django.conf.urls import url
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r"users", views.UserModelViewSet, basename="User")
router.register(r"posts", views.PostViewSet, basename="Post")

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
]
urlpatterns += [path("", include(router.urls))]

