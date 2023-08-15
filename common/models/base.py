from django.db import models
from django.utils.translation import gettext_lazy as _

from users.models import User


class AbstractBaseModel(models.Model):
    """This is the base model from which all other models are derived."""

    validators = []

    def get_validators(self):
        """Returns list of validators"""

        return self.validators

    # def get_fields(self):
    #     """Returns all fields of the object"""
    #     fields = []
    #     # return [getattr(self, x.name) for x in self._meta.fields]
    #     for x in self._meta.fields:
    #         try:
    #             fields.append(getattr(self, x.name))
    #         except ObjectDoesNotExist:
    #             pass
    #     return fields

    # def get_screen_methods(self):
    #     """Returns list of all methods whose name starts with 'screen_'"""
    #
    #     screen_methods = []
    #     attributes = dir(self)
    #     pattern = re.compile("screen[_]*")
    #     for attribute in attributes:
    #         if pattern.match(attribute):
    #             screen_methods.append(getattr(self, attribute))
    #     return screen_methods

    def check_validators(self):
        """Pass the object to all validators for validation"""

        validators = self.get_validators()
        for validator in validators:
            validator(obj=self).validate()

    def clean(self, *args, **kwargs):
        super(AbstractBaseModel, self).clean()
        self.check_validators()

    def save(self, *args, **kwargs):
        self.full_clean()
        super(AbstractBaseModel, self).save(*args, **kwargs)

    # def serialized_version(self, format="json", fields=None):
    #     dumped = serialize(format, [self], fields=fields)
    #     dumped = json.loads(dumped)
    #     serialized = dumped[0]["fields"]
    #     serialized["id"] = dumped[0]["pk"]
    #     return serialized

    class Meta:
        abstract = True


class LogBase(AbstractBaseModel):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    created_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="%(class)s_created_by",
        null=True,
        blank=True,
    )
    updated_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="%(class)s_updated_by",
        null=True,
        blank=True,
    )

    class Meta:
        abstract = True


class BaseModel(LogBase):
    code = models.CharField(
        max_length=128, help_text=_("Unique reference by the user within the tenant")
    )
    is_active = models.BooleanField(
        default=True, help_text=_("if TRUE the record is available")
    )

    class Meta:
        abstract = True
