from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.db.models import CharField, EmailField
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from test.users.managers import UserManager


def validate_phone_number(value):
    if not value.startswith('+998'):
        raise ValidationError(_('Phone number must start with +998'))
    if len(value) != 13:
        raise ValidationError(_('Phone number must be 13 characters long with +998'))


class User(AbstractUser):
    """
    Default custom user model for test.
    If adding fields that need to be filled at user signup,
    check forms.SignupForm and forms.SocialSignupForms accordingly.
    """

    # First and last name do not cover name patterns around the globe
    name = CharField(_("Name of User"), blank=True, max_length=255)
    first_name = None  # type: ignore
    last_name = None  # type: ignore
    email = EmailField(_("email address"), null=True, blank=True)
    phone_number = CharField(_("Phone number"), max_length=13, unique=True, validators=[validate_phone_number])
    username = None  # type: ignore

    USERNAME_FIELD = "phone_number"
    REQUIRED_FIELDS = []

    objects = UserManager()

    def get_absolute_url(self) -> str:
        """Get URL for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"pk": self.id})
