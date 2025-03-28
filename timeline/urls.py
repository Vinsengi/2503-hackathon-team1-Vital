from django.urls import path

from . import views

app_name = 'timeline'

urlpatterns = [
    path('', views.timeline, name='timeline'),
    path(
        'honour/<int:timeline_id>/', views.toggle_honour, name='toggle_honour'
    ),
    path(
        '<int:timeline_id>/honour/', views.toggle_honour, name='toggle_honour'
    ),
    path('detail/<int:timeline_id>/', views.event_detail, name='event_detail'),
]
