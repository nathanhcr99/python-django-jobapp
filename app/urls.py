from django.urls import path

from . import views




urlpatterns = [
    path('',views.job_list,name='jobs_home'),
    path('job/<int:id>',views.detailpage,name = 'jobs_detail'),
    path('hello/',views.hello, name='hello'),
]
