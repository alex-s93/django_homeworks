from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'task_manager_category'
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'
        # NOTE: закомментил строку, чтобы проверить валидатор в сериализаторе, иначе выдавало сообщение об ошибке:
        #       "non_field_errors": [
        #         "The fields name must make a unique set."
        #       ]
        # unique_together = ('name',)
