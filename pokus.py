from tests.factories import UserFactory, PostFactory
from blog.models import Post
from django.contrib.auth.models import User
from random import randint

for _ in range(100):
    ver = False if randint(1, 25) == 24 else True
    UserFactory(verified=ver)

users = User.objects.filter(emailaddress__verified=True)

for _ in range(2500):
    u = users.order_by('?').first()
    PostFactory(author=u)

