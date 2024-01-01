from django.db.models.fields.related import ForeignKey


class BaseModelService:
    """
    Base service class for a specific model.
    """
    model = None

    def get_app_label(self):
        """
        give back the app_name, based on the model
        :return:
        """
        if self.model:
            return self.model._meta.app_label
        return None

    def get_model_field_names(self, model):
        """
        Get the name of the model fields.
        :return: set of model fields name if model is present otherwise empty set.
        """

        model_field_names_set = set()

        if model:
            for field in model._meta.get_fields():
                if isinstance(field, ForeignKey):
                    db_field_name = field.name + "_id"
                    keys = [field.name, db_field_name]
                else:
                    keys = [field.name]
                model_field_names_set.update(keys)

        return model_field_names_set

    def map_model_fields_and_data(self, defaults, model_class,  *args, **kwargs):
        """
        For create update methods, inject tenant_code to the data dictionary if
        in the model, tenant_code is available.
        :param defaults:
        :param model_class:
        :param args:
        :param kwargs:
        :return:
        """
        if hasattr(model_class, "tenant_code"):
            if hasattr(self, "tenant_code"):
                defaults.update({"tenant_code": self.tenant_code})

        model_field_names_set = self.get_model_field_names(model_class)
        filtered_fields = {
            key: val
            for key, val in defaults.items()
            if key in model_field_names_set
        }
        return filtered_fields

    def create_model_instance(self, model_class, **field_values):
        """
        Create model instance from given fields.
        It takes field values, check whether the fields are valid model fields and finally create model instance from
        the fields that belong to the given model class.

        :param model_class: Model class
        :param field_values: Values to be saved
        :return: Created model instance
        """
        filtered_fields = self.map_model_fields_and_data(field_values, model_class())
        instance = model_class(**filtered_fields)
        instance.save()
        return instance

    def create(self, *args, **kwargs):
        """
        Create instance for the model defined in the service class.
        :param args: Positional arguments (Not used).
        :param kwargs: Field values to be saved.
        :return: Created model instance.
        """
        assert self.model is not None, (
            "'%s' should either include a `model` attribute, "
            "or override the `create()` method." % self.__class__.__name__
        )
        return self.create_model_instance(self.model, **kwargs)


