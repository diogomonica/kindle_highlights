from django.urls import path, include

from . import views

urlpatterns = [
    path('', include('inbound_email.urls')),
    path('', views.index, name='index'),
    path('e/<int:entry_id>/', views.entry, name='entry'),
]
