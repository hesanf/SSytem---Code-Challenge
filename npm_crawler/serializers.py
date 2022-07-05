from rest_framework import serializers

from npm_crawler.models import LastNews


class LastNewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = LastNews
        fields = ["id", "url", "title", "sumamry", "date_published"]
