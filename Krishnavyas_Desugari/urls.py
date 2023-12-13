# Krishnavyas_Desugari/urls.py
from django.contrib import admin
from django.urls import path, include
from pycontacts.views import contact_list, contact_create, contact_confirm_delete, contact_update  

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', contact_list, name='redirect_home'),  # Adjust the redirect to point directly to contact_list
    path('contacts/', include('pycontacts.urls')),
    # Your other patterns go here
]





