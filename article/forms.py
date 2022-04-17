from django import forms
from .models import Article



'''
To  relate your form with your model from models.py we equate them to each other.
model = Article
Django will create the fields which are in models.py. 
    - author
    - title
    - content
'''
class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ["title", "content", "article_image"]



