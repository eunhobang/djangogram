from django.db import models
from djangogram.users import models as user_model

class TimestamedModel(models.Model):
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True


class Post(TimestamedModel):
    author = models.ForeignKey(
        user_model.User,
        null=True,
        on_delete=models.CASCADE,
        related_name='post_author'
    )
    image = models.ImageField(blank=True)
    caption = models.TextField(blank=True)
    image_likes = models.ManyToManyField(user_model.User, related_name='post_image_likes')

class Comment(TimestamedModel):
    author = models.ForeignKey(
            user_model.User,
            null=True,
            on_delete=models.CASCADE,
            related_name='comment_author'
    )
    posts = models.ForeignKey(
            Post,
            null=True,
            on_delete=models.CASCADE,
            related_name='comment_author'
    )
    contens = models.TextField(blank=True)


