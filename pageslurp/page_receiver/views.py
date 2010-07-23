from models import Page
from django.core.files.base import ContentFile
from django.http import HttpResponse
import hashlib
import urllib


def receive(request):

    url = urllib.unquote(request.POST.get('url'))
    hash = hashlib.sha1(url).hexdigest()
    data = urllib.unquote(str(request.POST.get('page_text')))
    user_agent = request.META.get('HTTP_USER_AGENT')

    p = Page()
    p.url = url
    p.user_agent = user_agent
    p.page_file.save('%s.txt' % hash, ContentFile(data), save=False)
    p.save()

    return HttpResponse('thanks!', mimetype = 'text/plain')
    
