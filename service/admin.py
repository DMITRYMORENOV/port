from django.contrib import admin
from service.models import Post, Comment, Message


admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Message)