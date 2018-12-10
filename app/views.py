from django.shortcuts import render, redirect
from django.views import View
from . import forms
from app import models


class Note(View):
    def get(self, request):
        return render(request, 'leave-note.html', {'form': forms.NoteForm()})

    def post(self, request):
        form = forms.NoteForm(data=request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            message = form.cleaned_data['message']
            models.Guest.submitted(name, message)
            return redirect('home')
        else:
            return render(request, 'leave-note.html', {'form': form})


class GuestBook(View):
    def get(self, request):
        return render(request, 'home.html',
                      {'guests': models.Guest.objects.all()})
