from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from .models import imagesDB
# Create your views here.
from django.http import HttpResponse
from django.conf import settings


def index(request):
    return render(request, "frontend.html")


def upload_image(request):
    uploaded_file = request.FILES['filename']
    fs = FileSystemStorage()
    saved_name = fs.save(uploaded_file.name, uploaded_file)

    image_put = imagesDB(
        image_name=uploaded_file.name, image_url=settings.MEDIA_URL+saved_name)
    image_put.save()

    # USe opencv and edit the image
    # rewrite the image

    return redirect('http://127.0.0.1:8000'+settings.MEDIA_URL+saved_name)
