from django_filters import FilterSet
from .models import Post


class PostFilter(FilterSet):

    class Meta:
        model = Post

        fields = {
            'author__user': ['exact'],
            'created': ['date__gt'],
        }

