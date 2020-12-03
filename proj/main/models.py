from django.db import models
import json
from django.contrib.postgres.fields import JSONField


class Data(models.Model):
    Name = models.TextField()
    Text = models.TextField()
    Category = models.TextField()

    def toDict(self):
        return {
            'Name': self.Name,
            'Text': self.Text,
            'Category': self.Category,
        }

    def __repr__(self):
        return self.Name
        
    def __str__(self):
        return self.Name
        