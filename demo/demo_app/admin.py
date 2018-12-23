from django.contrib import admin
from django.db import models
from .models import Post
# from mdeditor.widgets import MDEditorWidget
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    formfield_overrides = {
        # models.TextField: {'widget': MDEditorWidget()},
    }

admin.site.register(Post,PostAdmin)