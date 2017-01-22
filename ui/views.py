from django.shortcuts import render
from django.http import HttpResponse
from ui.models import Feedback

def submit_feedback(request):
    title = "Feedback"
    return render(request,'base.html',{"page_title": title})

def show_feedback(request):
    #title = "Received feedback"
    feedbacks = Feedback.objects.all()
    return render(request,'feedbacks.html',{"Feedbacks":feedbacks})
# Create your views here.
