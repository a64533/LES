from django.urls import path

from . import views

app_name = 'inscription'
urlpatterns = [
    #path('', views.home_page, name='home_page'),
    path('', views.all_events, name='all_events'),
    path('<int:event_id>', views.event_page, name='event_page'),
    path('inscription_action/<int:event_id>', views.inscription_action, name='inscription_action'),
    path('inscription_form/<int:event_id>', views.inscription_form, name='inscription_form'),
]