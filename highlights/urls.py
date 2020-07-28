from django.urls import path, include

from . import views

urlpatterns = [
    path('', include('inbound_email.urls')),
    path('', views.index, name='index'),
    path('e/<int:entry_id>/', views.entry, name='entry'),
    path('h/<int:highlight_id>/', views.highlight, name='highlight'),
    path('u/<int:user_id>/', views.user_page, name='user'),

]
