from django.conf.urls import url
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt import views as jwt_views

# from rest_framework_simplejwt

from . import views

router = DefaultRouter()
# router.register(r"users", views.CreateUserModelViewSet, basename="User")
router.register(r"posts", views.PostViewSet, basename="Post")
router.register(r"likes", views.LikeViewSet, basename="Like")
router.register(
    r"users_activity", views.UserActivityRetrieveListViewSet, basename="UserActivity"
)
urlpatterns = [
    path("users/", views.CreateUserModelViewSet.as_view()),
    path("token/", jwt_views.TokenObtainPairView.as_view()),
    path("token/refresh/", jwt_views.TokenRefreshView.as_view()),
    path("api-auth/", include("rest_framework.urls")),
]
urlpatterns += [path("", include(router.urls))]
