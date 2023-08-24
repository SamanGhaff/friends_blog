from django.db import models


class ArticleManager(models.Manager):
    def counter(self):
        return len(self.all())

    def published(self):
        return self.filter(published=True)
    
    def get_queryset(self):
        return super(ArticleManager, self).get_queryset().filter(status=True)
