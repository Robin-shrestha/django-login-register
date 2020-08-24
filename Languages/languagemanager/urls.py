
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView
urlpatterns = [
    path('', include('language.urls')),
    path('admin/', admin.site.urls),
    path('account/', include('Users.urls')),
]
