from django.urls import path
from . import views


urlpatterns = [
    path('', views.listcontacts, name='listcontacts'),
    path('addcontacts/', views.addcontacts, name='addcontacts'),
    path('updatecontacts/<int:pk>', views.updatecontacts, name='updatecontacts'),
    path('deletecontacts/<int:pk>', views.deletecontacts, name='deletecontacts'),
    
]