from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Article(models.Model):  # table name Article
    author = models.ForeignKey("auth.User", on_delete=models.CASCADE, verbose_name="Writer")
    '''
    We will use ready user table. we will write a foreign key shows that user table.
    author points auth.User table, if we want to show/point another tables, we always use Foreignkey.
    '''
    title = models.CharField(max_length=50, verbose_name="Header")
    content = RichTextField(verbose_name="Text Field")
    created_date = models.DateTimeField(auto_now_add=True)
    article_image = models.FileField(blank=True, null=True, verbose_name="Add an image")

    '''
    (blank=True, null=True) means this Field is not mandatory. 
    When this article is created ?
    When we add a data into DB, it is going to insert the date automatically with "auto_now_add=True"
    Admin panelde article olusturdugumuzda herbiri "article object1..n " adi ile olusturuluyor.
    Eger biz bu olusturulan articlelari acmadan ne hakinda yazildigi hakkinda onceden bilgi sahibi olmak istersek
    title' in gosterilmesini isteyebiliriz. onun icinde str fonksiyonunu kullanabiliriz.
    '''
    def __str__(self):
        return self.title
    '''
    To personalize the Admin panel, We modified the admin.py script. We used decorator in line 14 in admin.py.
    '''



