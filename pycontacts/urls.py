# pycontacts/urls.py
from django.urls import path
from .views import (
    contact_list,
    contact_detail,
    contact_create,
    contact_update,
    contact_confirm_delete,  # Use the correct view name
)

urlpatterns = [
    path('contacts/', contact_list, name='contact_list'),
    path('contacts/<int:pk>/', contact_detail, name='contact_detail'),
    path('contacts/create/', contact_create, name='contact_create'),
    path('contacts/<int:pk>/update/', contact_update, name='contact_update'),
    path('contacts/<int:pk>/delete/', contact_confirm_delete, name='contact_confirm_delete'),  # Use the correct name
]






