from django.shortcuts import render, HttpResponse
from .forms import ContactForm

# Create your views here.
def homePage(request):
    """
    A functional based view for the home page
    """
    if request.method == 'POST':
        if request.method == 'POST':
            form = ContactForm(request.POST)
            if form.is_valid():
                form.save()  # Save to the database
                return HttpResponse("Thank you for your message!")
    else:
        form = ContactForm()


    return render(request, "index.html", {'form': form})
