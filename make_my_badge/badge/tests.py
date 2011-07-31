"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""
import simplejson
from django.test import TestCase
from django.http import HttpRequest
from django.contrib.auth.models import User

from badge.models import Event, Item
from badge.views import generate_badges, are_badges_ready

class GenerateBadgeViewTest(TestCase):
    def test_generate_badge_returns_ok(self):
        u = User.objects.create_user("test","test@test.com","pass")
        e = Event.objects.create(name="Test",user = u)
        i = Item.objects.create(event=e,name="Blah",properties="{}")
        request = HttpRequest()
        request.GET = {}
        response = generate_badges(request,e.id)
        self.assertEquals(200,response.status_code)
        self.assertEquals("application/json",response["Content-Type"])


class AreBadgesReadyViewTest(TestCase):
    def test_generate_badge_returns_false_when_blank_files_exist(self):
        u = User.objects.create_user("test","test@test.com","pass")
        e = Event.objects.create(name="Test",user = u)
        i = Item.objects.create(event=e,name="Blah",properties="{}")
        request = HttpRequest()
        request.GET = {}
        response = are_badges_ready(request,e.id)
        self.assertEquals(200,response.status_code)
        self.assertEquals("application/json",response["Content-Type"])
        self.assertEquals(False,simplejson.loads(response.content)["status"]["ready"])

    def test_generate_badge_returns_true_when_operation_is_complete(self):
        u = User.objects.create_user("test","test@test.com","pass")
        e = Event.objects.create(name="Test",user = u)
        request = HttpRequest()
        request.GET = {}
        response = are_badges_ready(request,e.id)
        self.assertEquals(200,response.status_code)
        self.assertEquals("application/json",response["Content-Type"])
        self.assertEquals(True,simplejson.loads(response.content)["status"]["ready"])

