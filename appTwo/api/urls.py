from django.urls import path, re_path
from api import views
from django.conf.urls import url

urlpatterns = [
    path('chat/', views.chatLV.as_view()),
    path('chat/<int:pk>/', views.chatDV.as_view()),
    # path('<int:pk>/', views.ChatDV.as_view(), name='detail',),
]
