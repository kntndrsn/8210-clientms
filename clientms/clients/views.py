from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.views.generic import ListView, DetailView
from .models import models
from .models import Client
from .models import Comment
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404

class ClientListView(LoginRequiredMixin,ListView):
    model = Client
    template_name = 'client_list.html'
    
    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        # Super users can see all clients
        if self.request.user.is_superuser:

            context['object_list'] = Client.objects.all()

        else:
            # Filtering the object list by the current user
            context['object_list'] = Client.objects.filter(author = self.request.user)        

        return context
        

class ClientDetailView(LoginRequiredMixin,DetailView):
    model = Client
    template_name = 'client_detail.html'
    login_url = 'login'

class ClientUpdateView(LoginRequiredMixin,UpdateView):
    model = Client
    fields = ('name', 'notes', 'address', 'city', 'state', 'zipcode', 'email', 'cell_phone', 'acct_number')
    template_name = 'client_edit.html'

class ClientDeleteView(LoginRequiredMixin,DeleteView):
    model = Client
    template_name = 'client_delete.html'
    success_url = reverse_lazy('client_list')

class ClientCreateView(LoginRequiredMixin,CreateView):
    model = Client
    template_name = 'client_new.html'
    fields = ('name', 'notes', 'address', 'city', 'state', 'zipcode', 'email', 'cell_phone', 'acct_number')
    login_url = 'login'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class ClientAddCommentView(LoginRequiredMixin,CreateView):

    model = Comment
    template_name = 'comment_new.html'
    fields = ('comment',)
    login_url = 'login'
    success_url = reverse_lazy('client_list')

    def form_valid(self, form):
        form.instance.client = get_object_or_404(Client, pk=self.kwargs['pk'])
        form.instance.author = self.request.user
        return super().form_valid(form)