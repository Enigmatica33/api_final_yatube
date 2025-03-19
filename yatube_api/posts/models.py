from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()

MAX_TITLE_LENGTH = 256


class Group(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name='Название сообщества'
    )
    slug = models.SlugField(unique=True)
    description = models.TextField(verbose_name='Описание сообщества')

    class Meta:
        verbose_name = "Сообщество"
        verbose_name_plural = "Сообщества"
        ordering = ('title',)

    def __str__(self):
        return self.title


class Follow(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='follower',
        verbose_name='Подписчик'
    )
    following = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='following',
        verbose_name='Автор'
    )

    class Meta:
        verbose_name = "Подписка"
        verbose_name_plural = "Подписки"
        ordering = ('following',)
        constraints = [
            models.UniqueConstraint(
                fields=['user', 'following'],
                name='unique_following_check'
            ),
            models.CheckConstraint(
                check=~models.Q(user=models.F("following")),
                name='self_following_check'
            ),
        ]

    def __str__(self):
        return self.following


class Post(models.Model):
    text = models.TextField()
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='posts')
    image = models.ImageField(
        upload_to='posts/', null=True, blank=True)
    group = models.ForeignKey(
        Group, on_delete=models.SET_NULL,
        related_name='posts', blank=True, null=True
    )

    class Meta:
        verbose_name = "Публикация"
        verbose_name_plural = "Публикации"
        ordering = ('-pub_date',)

    def __str__(self):
        return self.text[:MAX_TITLE_LENGTH]


class Comment(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='comments')
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    created = models.DateTimeField(
        'Дата добавления', auto_now_add=True, db_index=True)

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"
        ordering = ('-created',)

    def __str__(self):
        return self.text[:MAX_TITLE_LENGTH]
