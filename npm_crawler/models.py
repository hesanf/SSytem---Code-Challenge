from django.db import models


class LastNews(models.Model):
    """
    in this model we create database for web crawling data to store
    """
    id = models.IntegerField(primary_key=True)
    url = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    sumamry = models.TextField()
    date_published = models.CharField(max_length=100)

    class Meta:
        db_table = "news"
