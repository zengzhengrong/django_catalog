from django.db import models
# from mdeditor.fields import MDTextField
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=10,unique=True)
    slug = models.SlugField(unique_for_date='pulish_data')
    content = models.TextField()
    pulish_data = models.DateField(auto_now_add=True)

    class Meta:
        ordering = ('-pulish_data',)
        db_table = ''
        managed = True
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
    def __str__(self):
        return self.title
        


        