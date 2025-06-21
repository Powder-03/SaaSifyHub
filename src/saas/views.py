from django.http import HttpResponse
from django.shortcuts import render
from visits.models import PageVisit
# Create your views here.

def home_page_view(request , *args , **kwargs):
    queryset = PageVisit.objects.all()  # Fetch all PageVisit records
    my_title = "MY TITLE"
    my_context = {
        "my_title": my_title,
        "object_list": queryset,
    }
    html_template = "home.html"  # Ensure this template exists in your templates directory
    PageVisit.objects.create()  # Log the visit
    return render(request, html_template, my_context)
    
    return HttpResponse("Welcome to the SaaS application home page!")