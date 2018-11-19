from django.contrib import admin
from django.urls import path

from polls.views import *
urlpatterns = [
    path('', index),
    # path('<int:question_id>',detail),
    path('<int:question_id>',detail,name='detail'),
    path('<int:num1>/<int:num2>',detail2),
    path('<int:question_id>/vote',vote),
    path('<int:question_id>/edit',edit),
    path('<int:question_id>/save',save)
]
