import base64
import uuid

from django.utils.translation import ugettext_lazy as _


class CommonMixin:

    @staticmethod
    def getObjectOrNone(model=None, *args, **kwargs):

        try:
            entity = model.objects.get(*args, **kwargs)
        except model.DoesNotExist:

            entity = None

        return entity

    def returnSerializerErrors(self, dict={}):

        missingFields = []

        if not bool(dict):
            return False

        for k, v in dict.items():
            missingFields.append(k)

        fields = ', '.join(missingFields)

        return "%s %s" % (_("The following fields are required : "), fields)


def unique_id():
    """Generate unique id"""
    return base64.urlsafe_b64encode(uuid.uuid4(
        ).bytes).decode('utf-8').replace('==', '')


def get_object_or_none(model, *args, **kwargs):
    """Get object or none"""
    try:
        obj = model.objects.get(*args, **kwargs)
    except model.DoesNotExist:
        obj = None
    return obj
