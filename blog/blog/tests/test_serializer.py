from blog.serializers import PostSerializer
from blog.models import Post


def test_post_serializer_creating_post(verified_user, rf):
    request = rf.get("")
    request.user = verified_user  # dummy request with user
    data_post = {
        "title": "test_title",
        "text": "i dont know",
    }
    ser = PostSerializer(data=data_post, context={"request": request})
    assert ser.is_valid()
    ser.save()
    assert verified_user.post_set.count() == 1
    assert verified_user.post_set.first().title == data_post["title"]
    assert verified_user.post_set.first().text == data_post["text"]


def test_post_serializer_get_nested_ser(post):
    """
    test of nested user serializer in post
    """
    data = PostSerializer(post).data
    author = data["author"]
    assert author["id"] == post.author.id
    assert author["first_name"] == post.author.first_name
    assert author["last_name"] == post.author.last_name
