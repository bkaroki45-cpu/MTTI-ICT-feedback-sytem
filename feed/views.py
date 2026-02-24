from django.shortcuts import render, redirect
from .form import ICTFeedbackForm

# Create your views here.
def home(request):
    return render(request, 'feed/index.html')

def feedback(request):
    if request.method == 'POST':
        form = ICTFeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('message')
    else:
        form = ICTFeedbackForm()
    return render(request, 'feed/feedback.html', {'form':form})

def message(request):
    return render(request, 'feed/message.html')


def clubs(request):
    return render(request, 'feed/clubs.html')

def courses(request):
    return render(request, 'feed/courses.html')

def contacts(request):
    return render(request, 'feed/contacts.html')