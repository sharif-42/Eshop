from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils import timezone


class UserLoginLog(models.Model):
    """
    The model for keeping log of successful and unsuccessful login attempts
    """
    email = models.EmailField(
        _('email'),
        max_length=255,
        help_text=_('The email address used for the login attempt.'),
    )
    is_successful = models.BooleanField(
        default=True,
        help_text=_('True denotes that the login was successful'),
    )
    attempted_time = models.DateTimeField(
        _('time attempted'),
        auto_now_add=True
    )
    ip_address = models.GenericIPAddressField(
        _('IP address'),
        help_text=_('The IP from which the login was attempted'),
        blank=True, null=True,
    )
    browser = models.CharField(
        _('browser'),
        max_length=30,
        help_text=_('The browser used to login'),
        blank=True, null=True,
    )

    class Meta:
        # TODO: Define index
        ordering = ('-id',)
        verbose_name = 'User Login Log'
        verbose_name_plural = 'User Login Logs'

    def __str__(self):
        return f"{self.email} - {self.is_successful}"
