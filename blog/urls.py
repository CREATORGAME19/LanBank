from django.urls import path
from . import views
from django.urls import path, include 
urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('login', include('django.contrib.auth.urls'), name='login'),
    path('add',views.add, name='add'),
    path('test',views.test, name='test'),
    path('testsubmit',views.test_c, name='testsubmit'),
    path('remove',views.remove, name='remove'),
    path('find',views.find, name='find'),
    path('view',views.view, name='view'),
    path('results',views.results, name='results'),
    path('new_account',views.account_new, name='new_account'),
]
