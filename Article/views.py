from django.shortcuts import render, redirect
from .models import feedback
from .forms import FeedbackForm
from django.views.decorators.http import require_POST

# Create your views here.

def Home(request) :

    FBacks         = feedback.objects.order_by('Created')
    form           = FeedbackForm()
    context = {
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
