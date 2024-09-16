from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),     # admin
    path('news/', include('news.urls')), # news
    path('', include('news.urls')),      # перенаправление на новости по умолчанию
]
