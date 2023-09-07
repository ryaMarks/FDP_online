from django.urls import path
from ..accounts import views as v

app_name = 'accounts'
urlpatterns = [
    path('login/', v.user_login, name='user_login'),
    path('new_user/', v.CreateUser.as_view(), name='new_user'),
]
