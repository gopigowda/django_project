from django.http import HttpResponse
from django.http import JsonResponse  
from django.views.generic import View,DetailView
from todo_task.models import Task
from django.core import serializers


class TaskList(View):
	def get(self, request):
		data = serializers.serialize('json', Task.objects.filter(is_deleted=False))
		return HttpResponse(data, content_type="application/json")


class TaskDetailView(View):

	"""A base view for displaying a single object."""
	def get(self, request, *args, **kwargs):
		try:
			data = serializers.serialize('json', [Task.objects.get(pk=kwargs['pk'])])
			return HttpResponse(data, content_type="application/json")
		except Task.DoesNotExist:
			return JsonResponse({"status":False,'error':'Task not found'}, content_type="application/json")