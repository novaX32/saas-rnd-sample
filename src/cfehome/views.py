from django.http import HttpResponse
from django.shortcuts import render
import pathlib
from visits.models import PageVisit


this_dir_=pathlib.Path(__file__).resolve().parent


def home_page_view(request,*args,**kwargs):
    qs=PageVisit.objects.all()
    page_qs=PageVisit.objects.filter(path=request.path)
    my_title="Home Page"
    my_context={
        "page_title":my_title,
        "queryset":page_qs.count(),
        "percent":(page_qs.count()*100)/qs.count(),
        "total_visit_count":qs.count()
    }
    html_template="home.html"
    PageVisit.objects.create(path=request.path)
    return render(request,html_template,my_context)









def old_home_page_view(request,*args,**kwargs):
    my_title="My Page"
    my_context={
        "page_title":my_title
    }
    html_="""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{page_title}</title>
</head>
<body>
    <h1>Hello world How are you</h1>
    
</body>
</html>

""".format(**my_context)
    # html_file_path=this_dir_/"index.html"
    # html_=html_file_path.read_text()

    return HttpResponse(html_)