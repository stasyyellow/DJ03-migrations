from django.contrib import admin
from .models import News_post

@admin.register(News_post)
class NewsPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'pub_date')  # Отображение столбцов в админке
    search_fields = ('title', 'author__username')  # Добавление поиска по названию и автору
    list_filter = ('pub_date', 'author')  # Фильтр по дате публикации и автору
    date_hierarchy = 'pub_date'  # Навигация по датам в админке

# admin.site.register(News_post) больше не нужен, так как используется декоратор @admin.register
