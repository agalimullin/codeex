from django.db import models
from datetime import *
from django.contrib.auth.models import User


class Category(models.Model):
    class Meta:
        db_table = "category"
        ordering = ['category_title']

    def __str__(self):
        return self.category_title

    category_title = models.CharField(max_length=30)

    def get_absolute_url(self):
        return "/categories/%i/" % self.id


class Product(models.Model):
    class Meta:
        db_table = "products"
        verbose_name_plural = 'Products'
        unique_together = ['product_title', 'product_short_description']

    product_category = models.ForeignKey(Category)
    product_title = models.CharField(max_length=20)
    product_short_description = models.TextField()
    product_img = models.ImageField(upload_to="images")
    product_cost = models.PositiveIntegerField(default=0)
    release_date = models.DateTimeField(default=datetime.now)
    likes = models.IntegerField(default=0)
    available = models.BooleanField()

    def is_available(self):
        if self.available:
            return 'Exists'
        else:
            return 'Not exist'

    def __str__(self):
        return self.product_title

    def get_absolute_url(self):
        return "/product/%i/" % self.id


class Comment(models.Model):
    class Meta:
        db_table = "comments"
        ordering = ['comment_date']

    def __str__(self):
        return self.comment_text

    comment_text = models.TextField(help_text="Leave a comment")
    comment_date = models.DateTimeField(default=datetime.now)
    comment_product = models.ForeignKey(Product)
    comment_author = models.ForeignKey(User)
