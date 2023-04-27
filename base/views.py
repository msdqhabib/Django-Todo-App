from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from .models import Task
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


class TaskList(LoginRequiredMixin,ListView):
    model = Task
    context_object_name = 'task_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['task_list'] = context['task_list'].filter(user=self.request.user)
        context['count'] = context['task_list'].filter(complete=False).count()
        
        #search-bar is name of form input field
        search_input = self.request.GET.get('search-bar') or ''
        #if text search exists!
        if search_input:
            #if we want filter should search from start of the task_list words
            #Than replace icontains with startswith
            context['task_list'] = context['task_list'].filter(
                title__icontains=search_input
            )
        #To show the search text in search bar
            context['search_input'] = search_input
        return context


class TaskDetail(LoginRequiredMixin,DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'base/task.html'


class TaskCreate(LoginRequiredMixin,CreateView):
    model = Task
    fields = ['title','description','complete']
    #if everything goes correctly, than redirect user to task list page
    success_url = reverse_lazy('task_list')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskCreate, self).form_valid(form)

class TaskUpdate(LoginRequiredMixin,UpdateView):
    model = Task
    fields = ['title','description','complete']
    success_url = reverse_lazy('task_list')

class TaskDelete(LoginRequiredMixin,DeleteView):
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('task_list')
