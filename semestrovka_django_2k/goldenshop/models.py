from django.contrib.auth.models import User
from datetime import *
from django.db import models


class Review(models.Model):
    class Meta:
        db_table = "reviews"
        ordering = ['review_date']

    def __str__(self):
        return self.review_text

    review_text = models.TextField(help_text="Leave a comment")
    review_date = models.DateTimeField(default=datetime.now)
    review_author = models.ForeignKey(User)
