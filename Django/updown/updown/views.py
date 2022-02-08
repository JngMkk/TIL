from django.http import HttpResponse
from django.shortcuts import render
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage

def index(request):
    return render(request, 'index.html')

def upload_process(request):
    upload_file = request.FILES['uploadfile']
    # print(upload_file)
    # print(type(upload_file))

    uploaded = default_storage.save(upload_file.name, ContentFile(upload_file.read()))
    # print(uploaded)
    # print(type(uploaded))

    return render(request, 'download.html', {'filename' : uploaded})

def download_process(request, filename):
    response = HttpResponse(filename)
    response['Content-Disposition'] = f"attachment; filename={filename}"

    return response