from django.contrib.auth.backends import BaseBackend
from django.contrib.auth.models import User

class EmailOrUsernameBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        try:
            # Check if the input is an email
            user = User.objects.get(email=username)
        except User.DoesNotExist:
            # If not an email, assume it's a username
            try:
                user = User.objects.get(username=username)
            except User.DoesNotExist:
                return None

        # Check the password
        if user.check_password(password):
            return user
        return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
