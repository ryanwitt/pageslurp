from django.db import models

class Page(models.Model):

    url = models.URLField(verify_exists=False, max_length=4096)
    user_agent = models.CharField(max_length=255)
    page_file = models.FileField(upload_to='page_files/%Y/%b/%d')
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-date_created',)
