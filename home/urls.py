from django.urls import path
from .views import switch_language
from . import views
from .views import *

urlpatterns = [
    path('', home_view, name='home'),
    path('change-lang/', switch_language, name='switch_language'),
    path('contact/', contact_view, name='contact'),

]
