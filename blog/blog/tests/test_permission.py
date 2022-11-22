import pytest
from rest_framework.reverse import reverse


# todo dodelat testy s authentikaci, tedka nemam paru jak na to


@pytest.mark.loadedfixtures
def test_post_permission_post_is_owner(api_client, homer31):
    """
    test that owner of post have permission to update and delete.
    """
    data = {"title": "updated"}
    post = homer31.post_set.first()
    url = reverse("post-detail", args=[post.id])
    print(api_client.force_login(homer31))
    res = api_client.post(
        url,
        data,
    )
    print(res.data)
    assert res.status_code == 401
    assert 0
