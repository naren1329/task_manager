from django.db import models

class task_table(models.Model):
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

class records(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    duedate = models.DateTimeField()
    user=models.ForeignKey(task_table,on_delete=models.CASCADE)
    select=[('high', 'high'),('medium','medium'),('low', 'low')]
    priority = models.CharField(max_length=255,choices=select)
    complete=[('complete','complete'),('not complete','not complete')]
    status=models.CharField(max_length=30,choices=complete)