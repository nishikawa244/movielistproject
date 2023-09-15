from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import Record
from django.urls import reverse_lazy
# Create your views here.

class RecordListView(ListView):
    template_name='movielist.html'
    model=Record

class RecordDetailView(DetailView):
    template_name='detail.html'
    model=Record

class RecordCreateView(CreateView):
    template_name='create.html'
    model=Record
    fields=("title","memo","rate","kinds","date")
    success_url=reverse_lazy("movielist")

class RecordUpdateView(UpdateView):
    template_name='update.html'
    model=Record
    fields=("title","memo","rate","kinds","date")
    success_url=reverse_lazy("movielist")

class RecordDeleteView(DeleteView):
    template_name='delete.html'
    model=Record
    success_url=reverse_lazy("movielist")
