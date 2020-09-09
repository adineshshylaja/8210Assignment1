from django.contrib import admin

# Register your models here.
from .models import Client, Comment
#class ClientAdmin(admin.ModelAdmin):
#    model = Client

#admin.site.register(Client, ClientAdmin)

class CommentInline(admin.TabularInline):
    model = Comment


class ClientAdmin(admin.ModelAdmin):
    inlines = [
        CommentInline,
    ]

admin.site.register(Client, ClientAdmin)
admin.site.register(Comment)
