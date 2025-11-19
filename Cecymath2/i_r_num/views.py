from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "i_r_num/home.html")