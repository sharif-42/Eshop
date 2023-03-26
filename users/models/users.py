from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, PermissionsMixin
)
from django.utils.translation import gettext_lazy as _


class UserManager(BaseUserManager):
    def create_user(self, email, password,  **extra_fields):
        user = self.model(
            email=email,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        user = self.create_user(
            email=email,
            password=password,
            **extra_fields
        )
        user.is_superuser = True
        user.is_dashboard_user = True
        user.is_pending = False
        user.is_active = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        verbose_name='Email Address',
        max_length=255,
        unique=True,
        help_text=_("User unique email. This is using as username.")
    )
    first_name = models.CharField(
        max_length=255,
        blank=True,
        help_text=_("User first name")
    )
    last_name = models.CharField(
        max_length=255,
        blank=True,
        help_text=_("User last/nick name")
    )
    phone_number = models.CharField(
        max_length=16,
        verbose_name='Contact Number',
        blank=True,
        help_text=_('User Contact Number')
    )

    # user boolean field
    is_pending = models.BooleanField(default=True, help_text=_('User activity is pending for some reasons.'))
    is_dashboard_user = models.BooleanField(default=False, help_text=_('User is a dashboard user.'))
    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_("Designates whether the user can log into this admin site."),
    )
    is_active = models.BooleanField(
        _("is_active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )
    # blocking related fields
    is_blocked = models.BooleanField(default=False, help_text=_('User is blocked by authority for some reasons.'))

    # common fields
    joined_date = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True, blank=True)

    objects = UserManager()
    EMAIL_FIELD = "email"
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")
        ordering = ('-id',)
        # TODO: Define index

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def get_full_name(self):
        """
        Return the first_name plus the last_name, with a space in between.
        """
        full_name = "%s %s" % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        """Return the short name for the user."""
        return self.first_name

    def __str__(self):
        return self.email


