from django.shortcuts import render
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from toy.models import Toy

# Create your views here.
class ToyCreate(CreateView):
    model = Toy
    template_name = "toy_form.html"
    fields = "__all__"
    
class ToyListView(ListView):
    template_name = "toy_List.html"
    model = Toy
    def get_queryset(self):
        qs=Toy.objects.all()  
        return qs
    
class ToyDetails(DetailView):
    model = Toy
    template_name = "toy_Detail.html"
    
class ToyUpdate(UpdateView):
    model = Toy
    template_name = "toy_form.html"
    fields = "__all__"
    success_url = "/list"
    
class ToyDelete(DeleteView):
    model = Toy
    template_name="toy_confirm_delete.html"
    success_url = "/list"
    