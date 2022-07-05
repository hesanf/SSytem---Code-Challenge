from rest_framework import viewsets
from rest_framework.filters import SearchFilter, OrderingFilter
from .serializers import LastNewsSerializer
from .models import LastNews


def http_methods_disable(*methods):
    def decorator(cls):
        cls.http_method_names = [
            method for method in cls.http_method_names if method not in methods]
        return cls
    return decorator


@http_methods_disable('post', 'delete')
class LastNewsViewSet(viewsets.ModelViewSet):
    queryset = LastNews.objects.all().order_by('-id')[:5]
    serializer_class = LastNewsSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ["title", "date_published"]
    ordering_fields = ["id"]
