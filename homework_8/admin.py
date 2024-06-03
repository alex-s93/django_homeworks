from django.contrib import admin

from homework_8.models import Task, Subtask, Category


class SubtaskInline(admin.StackedInline):
    model = Subtask
    extra = 1


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    inlines = [SubtaskInline]
    list_display = ('title', 'get_categories', 'status', 'deadline', 'created_at')

    def get_categories(self, task):
        return ", ".join(category.name for category in task.categories.all())

    get_categories.short_description = 'Categories'


@admin.register(Subtask)
class SubtaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'task', 'status', 'deadline', 'created_at')


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    ...
