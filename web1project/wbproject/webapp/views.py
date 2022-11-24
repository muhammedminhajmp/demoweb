from django.shortcuts import render
from . models import dress
# Create your views here.
def demo(request):
    obj=dress.objects.all()
    return render(request,"index.html",{'result':obj})