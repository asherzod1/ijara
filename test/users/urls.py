from django.urls import path

from test.users.api.views import UserCreateView, UserLoginView
from test.users.views import (
    user_detail_view,
    user_redirect_view,
    user_update_view,
)

app_name = "users"
urlpatterns = [
    path("~redirect/", view=user_redirect_view, name="redirect"),
    path("~update/", view=user_update_view, name="update"),
    path("<int:pk>/", view=user_detail_view, name="detail"),
    path('register/', UserCreateView.as_view(), name='user-register'),
    path('login/', UserLoginView.as_view(), name='user-login'),
]
