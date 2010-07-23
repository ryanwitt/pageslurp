from models import Page
from django.core.files.base import ContentFile
from django.http import HttpResponse
import hashlib


def receive(request):

    url = request.GET.get('url')
    hash = hashlib.sha1(url).hexdigest()
    data = request.raw_post_data
    user_agent = request.META.get('HTTP_USER_AGENT')

    p = Page()
    p.url = url
    p.user_agent = user_agent
    p.page_file.save('%s.html' % hash, ContentFile(data), save=False)
    p.save()

    return HttpResponse('thanks!', mimetype = 'text/text')
    
