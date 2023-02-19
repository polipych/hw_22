from django.contrib import admin
from taskapp.models import Task
import datetime
from django.contrib.admin.actions import delete_selected

delete_selected.short_description = "Удалить выбранные задачи"


@admin.action(description="Завершить выбранные задачи")
def deactivate(modeladmin, request, queryset):
    """Кастомное действие в админке todo - завершение выбранных задач."""
    queryset.update(status=False, end=None)


@admin.action(description="Вернуть в работу")
def activate(modeladmin, request, queryset):
    """Кастомное действие в админке todo - активация выбранных задач."""
    queryset.update(status=True, end=datetime.datetime.now())


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "status", "start", "end"]
    actions = [
        deactivate,
        activate,
    ]  # Добавление дополнительного действия в выпадающем меню
    search_fields = ("title",)  # по каким полям будет производиться поиск
