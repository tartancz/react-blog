import pytest

from rest_framework.reverse import reverse

from django.db.models import Q

from blog.models import Post

from rest_framework.views import Response
from blog.views import PostViewSet
from django.contrib.auth.models import User


@pytest.mark.loadedfixtures
def test_get_list_view_filter_by_author(load_fixtures, api_client, homer31):
    """
    test for filtering by user in query params
    """
    url = reverse("post-list") + f"?author={homer31.id}"
    response = api_client.get(url)
    data = response.data
    assert data["count"] == homer31.post_set.count()
    assert response.status_code == 200


def test_get_list_view_filter_by_text(api_client, post):
    """
    test for filtering by user in query params
    """
    url = reverse("post-list") + f"?text={post.title}"
    response = api_client.get(url)
    data = response.data
    assert data["count"] == 1
    assert data["results"][0]["text"] == post.text
    assert response.status_code == 200


@pytest.mark.loadedfixtures
def test_get_list_view_filter_query_set(api_client):
    search = "eta"
    url = reverse("post-list") + f"?text={search}"
    response = api_client.get(url)
    data = response.data

    query_set = (
        Post.objects.all()
        .filter(Q(title__icontains=search) | Q(text__icontains=search))
        .annotate(up=Q(title__icontains=search))
        .order_by("-up", "-created_at")
    )

    assert data["count"] == len(query_set)
    assert data["results"][0]["id"] == query_set.first().id
    assert response.status_code == 200
