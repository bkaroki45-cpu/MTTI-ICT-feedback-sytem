from django.shortcuts import render, redirect
from .form import ICTFeedbackForm

# Create your views here.
def home(request):
    return render(request, 'feed/home.html')

def see(request):
    if request.method == 'POST':
        form = ICTFeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('message')
    else:
        form = ICTFeedbackForm()
    return render(request, 'feed/see.html', {'form':form})

def message(request):
    return render(request, 'feed/message.html')