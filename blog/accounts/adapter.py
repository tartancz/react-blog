from allauth.account.adapter import DefaultAccountAdapter

from django.conf import settings


class AccountAdapter(DefaultAccountAdapter):
    def get_email_confirmation_url(self, request, emailconfirmation):
        # url address for frontend email verify with email confirmation
        return f"{settings.FROND_END_VERIFY_URL}{emailconfirmation.key}"
