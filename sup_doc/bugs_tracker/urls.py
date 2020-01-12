from django.urls import path
from . import views


urlpatterns = [
    path('', views.landing, name="landing_page"),
    path('ticket/all', views.index, name="index"),
    path('ticket/new', views.new_ticket, name="new_ticket"),
    path('ticket/edit/<int:ticket_id>', views.edit_ticket, name="edit_ticket"),
    path('ticket/<int:ticket_id>', views.ticket_detail, name="ticket_detail"),
    path('user/<int:user_id>', views.tickets_by_user, name="tickets_by_user"),
    path('user/login', views.login_user, name="user_login"),
    path('user/new', views.new_user, name="new_user"),
    path('user/all', views.all_users)
]