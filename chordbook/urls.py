from django.contrib import admin
from django.urls import path

from .memberlist import views as memberlist_views

urlpatterns = [
	path('admin/', admin.site.urls),
	path('members', memberlist_views.member_list, name='member_list'),
]
