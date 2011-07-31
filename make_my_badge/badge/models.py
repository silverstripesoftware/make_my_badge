from django.db import models

from django.contrib.auth.models import User

class Event(models.Model):
    name = models.CharField(max_length=128)
    user = models.ForeignKey(User)
    zipped_content = models.FileField(null=True,blank=True,upload_to="zipped_content")

    def __unicode__(self):
        return "Event: " + self.name

class BadgeTemplate(models.Model):
    template_image = models.ImageField(upload_to="badge_template")
    event = models.ForeignKey(Event)

    def __unicode__(self):
        return self.event.name + ": " + self.template_image.name

class Item(models.Model):
    name = models.CharField(max_length=64)
    # We store the properties dict here in JSON format
    properties = models.TextField()
    generated_image = models.ImageField(null=True, blank=True, upload_to="generated_badges")
    event = models.ForeignKey(Event, null=True)

    def __unicode__(self):
        return self.event.name + ": " + self.name
