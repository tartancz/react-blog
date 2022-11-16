from allauth.account.adapter import DefaultAccountAdapter

class AccountAdapter(DefaultAccountAdapter):
    def get_email_confirmation_url(self, request, emailconfirmation):
        # url address for email verify with email confirmation
        return f'https://mywebsite.com/register/verify/{emailconfirmation.key}'