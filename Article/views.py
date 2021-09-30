from django.shortcuts import render, redirect
from .models import feedback
from .forms import FeedbackForm
from django.views.decorators.http import require_POST
from .Scraper import Scrape
# Create your views here.

def Home(request) :


    url     = 'https://surenjanath.medium.com'
    header  = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36'}

    Articles       = Scrape(url, header)
    FBacks         = feedback.objects
    form           = FeedbackForm()
    context = {
               'Articles'  : Articles,
               'Feedbacks' : FBacks,
               'Form'      : form,
               }

    return render(request,'Article/index.html', context)

@require_POST
def addFeedbackItem(request):
    form = FeedbackForm(request.POST)
    if form.is_valid():
        new_feedback = feedback(Name = request.POST['Name'],
                               Email = request.POST['Email'],
                               Feedback = request.POST['Feedback']
                               )
        new_feedback.save()
    return redirect('Home')
