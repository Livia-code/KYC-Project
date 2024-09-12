from django.shortcuts import render
from .forms import KnowYourCustomerForm

# Create your views here.
def home(request):
    form = KnowYourCustomerForm()
    if request.method == 'POST':
        form = KnowYourCustomerForm(request.POST)
        if form.is_valid():
            form.save()
        return render(request, 'KYCapp/success.html')
    return render(request, 'home.html',{'form':form})