from django.contrib import admin
from catalog.models import *

from catalog.models import *

admin.AdminSite.site_header = '1 admin - 1 project'


class CategoryAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['category_title']})
    ]
    list_display = ['category_title']
    ordering = ['category_title']


class ProductAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['product_category', 'product_title', 'product_short_description', 'product_img',
                           'product_cost', 'release_date', 'likes', 'available']})
    ]
    list_display = ['product_title', 'product_short_description', 'product_cost']
    prepopulated_fields = {'product_short_description': ['product_title']}
    ordering = ['product_title']
    list_filter = ['release_date']


class CommentAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['comment_text', 'comment_date', 'comment_product', 'comment_author']})
    ]
    list_display = ['comment_text', 'comment_date']
    ordering = ['comment_date']
    list_filter = ['comment_author']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Comment, CommentAdmin)
