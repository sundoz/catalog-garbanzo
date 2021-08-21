
import random
from django.http import HttpResponse    
from django.template.loader import render_to_string
from articles.models import Article



def home_view(request, *args, **kwargs):
    name = 'Biba'
    
    article_obj = Article.objects.get(id=random.randint(1,3))
    article_title = article_obj.title
    article_content = article_obj.content

    article_queryset = Article.objects.all()
    context = {
        "object_list": article_queryset,
        "title": article_obj.title,
        "content": article_obj.content,
        "id" : article_obj.id
        
    }
    HTML_STRING = render_to_string("home-view.html", context=context)
    #HTML_STRING = """
    #<h1>{title}(id: {id})!</h1>
    #<p>{content}!</p>
    #""".format(**context)
    return HttpResponse(HTML_STRING)
