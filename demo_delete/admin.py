from django.contrib import admin

from .models import  post, comment, post_protect, comment_protect
# Register your models here.

admin.site.register(post)
admin.site.register(comment)
admin.site.register(post_protect)
admin.site.register(comment_protect)
