from django.shortcuts import render

# Create your views here.
def static_folder(request):
    return render(request,'static_folder.html')