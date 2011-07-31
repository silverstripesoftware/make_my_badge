import os
import StringIO
import zipfile

from django.core.files.uploadedfile import InMemoryUploadedFile

from celery.decorators import task
from badge.models import BadgeTemplate
from badge.badgeImage import BadgeImage

@task()
def generate_badge(item):
    event = item.event
    badge_img = BadgeImage(event.template_image.path, name_color=event.name_color, company_color=event.company_color)
    badge_img.drawPerson(item.name)
    badge_img.drawCompany(item.properties)
    badge_img.drawId(str(item.id))
    badge_io = StringIO.StringIO()
    badge_img.img.save(badge_io,"png")
    badge_file = InMemoryUploadedFile(badge_io, None, 'temp_file.png', 'image/png',badge_io.len, None)
    item.generated_image.save("badge_image_%d.png"%(item.id,),badge_file)
    item.save()

@task()
def zip_file(event):
    item_list = event.item_set.all()
    zipped_io = StringIO.StringIO()
    zip_obj = zipfile.ZipFile(zipped_io,mode="w")
    for item in item_list:
        zip_obj.write(item.generated_image.path, os.path.basename(item.generated_image.path))
    zip_obj.close()
    zipped_file = InMemoryUploadedFile(zipped_io, None, 'event_%d.zip'%(event.id,), 'application/x-zip-compressed',zipped_io.len, None)
    event.zipped_content.save('event_%d.zip'%(event.id,),zipped_file)
    event.save()
