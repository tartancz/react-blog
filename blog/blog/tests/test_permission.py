import pytest
from rest_framework.reverse import reverse

# todo dodelat testy


@pytest.mark.loadedfixtures
def test_permission_post_is_owner(api_client, homer31):
    """
    test that owner of post have permission to update and delete.
    """
    post = homer31.post_set.first()
    url = reverse("post-detail", args=[post.id])
    assert 1
