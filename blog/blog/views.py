from django.db.models import Q, Value, IntegerField

from rest_framework import viewsets, mixins

from django_filters import rest_framework as filters

from blog.serializers import PostSerializer
from blog.models import Post
from blog.permisions import isOwnerOrReadOnly

# Create your views here.


class ProductFilter(filters.FilterSet):
    author = filters.NumberFilter(field_name="author__id")
    text = filters.CharFilter(method="text_filter")

    class Meta:
        model = Post
        fields = ["author"]

    def text_filter(self, queryset, name, value):
        """
        return all post where is value in title or in text
        ordered by first in title and then in text
        """
        return (
            queryset.filter(Q(title__icontains=value) | Q(text__icontains=value))
            .annotate(up=Q(title__icontains=value))
            .order_by("-up", "-created_at")
        )


class PostViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):
    permission_classes = [isOwnerOrReadOnly]
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    filterset_class = ProductFilter
