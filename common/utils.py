import base64
import uuid

from django.utils.translation import ugettext_lazy as _


class CommonMixin:

    @staticmethod
    def get_object_or_none(model=None, *args, **kwargs):
        try:
            entity = model.objects.get(*args, **kwargs)
        except model.DoesNotExist:
            entity = None

        return entity

    @staticmethod
    def return_serializer_errors(dict={}):

        missingFields = []

        if not bool(dict):
            return False

        for k, v in dict.items():
            missingFields.append(k)

        fields = ', '.join(missingFields)

        return "%s %s" % (_("The following fields are required : "), fields)
