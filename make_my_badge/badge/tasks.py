import StringIO

from django.core.files.uploadedfile import InMemoryUploadedFile

from celery.decorators import task
from badge.models import BadgeTemplate
from badge.badgeImage import BadgeImage

@task()
def generate_badge(item):
    event = item.event
    badge_template = BadgeTemplate.objects.filter(event=event)[0]
    badge_img = BadgeImage(badge_template.template_image.path)
    badge_img.drawPerson(item.name)
    badge_img.drawCompany("Silver Stripe Software")
    badge_img.drawId(str(item.id))
    badge_io = StringIO.StringIO()
    badge_img.img.save(badge_io,"png")
    badge_file = InMemoryUploadedFile(badge_io, None, 'temp_file.png', 'image/png',badge_io.len, None)
    item.generated_image.save("badge_image_%d.png"%(item.id,),badge_file)
    item.save()