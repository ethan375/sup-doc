from django.urls import path
from . import views


urlpatterns = [
    path('tickets/', views.index, name="index"),
    path('ticket/new', views.new_ticket, name="new_ticket"),
    path('ticket/edit/<int:ticket_id>', views.edit_ticket, name="edit_ticket")
]