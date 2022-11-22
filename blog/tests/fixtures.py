import pytest

from django.contrib.auth.models import User


@pytest.fixture(scope="session")
def load_fixtures(django_db_setup, django_db_blocker):
    from django.core.management import call_command

    with django_db_blocker.unblock():
        call_command("loaddata", r".\tests\fixtures\user_fixtures.json")
        call_command("loaddata", r".\tests\fixtures\emailaddress_fixtures.json")
        call_command("loaddata", r".\tests\fixtures\post_fixtures.json")


@pytest.fixture(autouse=True)
def database_access(db):
    pass


@pytest.fixture
def api_client():
    from rest_framework.test import APIClient

    return APIClient()


@pytest.fixture
def verified_user(user_factory):
    return user_factory(verified=True)


@pytest.fixture
def unverified_user(user_factory):
    return user_factory()


@pytest.fixture
def post(post_factory):
    return post_factory()


@pytest.fixture()
def homer31(load_fixtures):
    return User.objects.get(pk=32)


@pytest.fixture()
def homer15(load_fixtures):
    return User.objects.get(pk=16)
