from django.db import models


# Create your models here.
class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Todo(models.Model):
    STATES = [('i', 'In Progress'),
              ('f', 'Finished')]

    PRIORITY = [('1', 'High'),
                ('2', 'Medium'),
                ('3', 'Low')]

    title = models.CharField(max_length=50,)
    description = models.TextField(max_length=250, blank=True)
    e_time = models.DateTimeField(blank=True, null=True)
    priority = models.CharField(choices=PRIORITY, default='2')
    state = models.CharField(choices=STATES, default='i')
    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return self.title
