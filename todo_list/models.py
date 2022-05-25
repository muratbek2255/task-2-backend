from django.db import models


from django.contrib.auth import get_user_model

User = get_user_model()



class Todo(models.Model):
    """Задачи"""
    title = models.CharField('Название', max_length=155)
    comment = models.TextField('Комментарий')
    deadline = models.DateTimeField('Дедлайн', auto_now=False)
    create_todo = models.DateTimeField('Создание задачи', auto_now=True)
    file = models.FileField()
    is_completed = models.BooleanField(default=False)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='users', default=1)

    def __unicode__(self):
        return self.title
