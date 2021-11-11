from django.urls import path
from . import views
urlpatterns=[
    
    path('userfeed/<id>',views.get_userfeed),
] 