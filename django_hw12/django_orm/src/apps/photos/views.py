from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import render, redirect
from apps.photos.forms import PhotoForm


def image_view(request):
    if request.method == 'POST':
        form = PhotoForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = PhotoForm()
    return render(request, 'add_image.html', {'form': form})


def success(request):
    return HttpResponse('successfully uploaded')
