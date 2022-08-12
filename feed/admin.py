from django.contrib import admin

# Register your models here.
from .models import Post

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    pass

#connect post with post admin

admin.site.register(Post,PostAdmin)