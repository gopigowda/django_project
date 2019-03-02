from django.db import models
from django.utils import timezone
from django.utils.translation import gettext as _

class Task(models.Model):
	title = models.CharField(max_length=200)
	description = models.TextField()
	task_time = models.DateTimeField(default=timezone.now)
	is_deleted = models.BooleanField(default=False)
	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)
	
	def __str__(self):
		return u'%s' % (self.title)

	class Meta:
		verbose_name = _('task')
		verbose_name_plural = _('tasks')
		db_table = 'tbl_tasks'
	@classmethod
	def filterAll(self,**kwargs):
		return Task.objects.filter(**kwargs)

	@classmethod
	def getOne(self,**kwargs):
		return Task.objects.get(**kwargs)