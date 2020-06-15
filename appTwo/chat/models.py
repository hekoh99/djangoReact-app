from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Chat(models.Model):
    name = models.CharField('NAME', max_length=200)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    create_dt = models.DateTimeField('CREATE DATE', auto_now_add=True)

    class Meta:
        verbose_name = 'chat' #테이블의 별칭
        verbose_name_plural = 'chats'
        ordering = ('-create_dt',)

    def __str__(self):
        return self.name
