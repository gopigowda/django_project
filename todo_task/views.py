from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from todo_task.models import Task

# Create your views here.

class TaskList(ListView):
	model = Task
	queryset = Task.filterAll(is_deleted=False)


class TaskView(DetailView):
	model = Task
	

class TaskCreate(CreateView):
	model = Task
	fields = ['title', 'description','task_time']
	success_url = reverse_lazy('task_list')

class TaskUpdate(UpdateView):
	model = Task
	fields = ['title', 'description','task_time']
	success_url = reverse_lazy('task_list')

class TaskDelete(DeleteView):
	model = Task
	success_url = reverse_lazy('task_list')
	
	def delete(self, request, *args, **kwargs):
		"""
		Call the delete() method on the fetched object and then redirect to the
		success URL.
		"""
		task_object = self.get_object()
		success_url = self.get_success_url()
		task_object.is_deleted =1
		task_object.save()
		return HttpResponseRedirect(success_url)