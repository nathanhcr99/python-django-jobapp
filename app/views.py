from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render
from django.shortcuts import redirect
from django.urls import reverse
from django.template import loader
from app.models import JobPost
# Create your views here.

job_title = [
    "First Job",
    "Second Job",
    "Third Job",
]

job_description = [
    "First job description",
    "Second job description",
    "Third job description"

]

class TempClass:
    x = 5


def hello(request):
   
    lista = ["ABC","DEF"]
    temp = TempClass()
    is_authenticated = False
    context={"name":"Django","first_list": lista,"temp_obj": temp,"age": 24,"is_authenticated": is_authenticated}
    return render(request,'app/hello.html',context)

def job_list(request):

    # list
    # for i,job in enumerate(job_title):
    #     detail_url = reverse('job_detail', args = (i,))
    #     list_jobs += f"<li><a href='{detail_url}'>{job}</a></li>"
    jobs = JobPost.objects.all()
    context = {"jobs": jobs}
    return render(request,'app/index.html',context)


def detailpage(request,id):

    try:
        if id == 0:
            return redirect(reverse('jobs_home'))
        job = JobPost.objects.get(id=id)
        context = {'job': job }
        return render(request,"app/detailpage.html",context)
        # return_html = f'<h1> {job_title[id]}</h1> <h3>{job_description[id]}</h3>'
        # return HttpResponse(return_html)
    except:
        return HttpResponseNotFound("<h1>Not Found</h1>")
    