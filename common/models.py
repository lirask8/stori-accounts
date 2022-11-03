import uuid
from django.db import models


class BaseModel(models.Model):
    """Base model"""

    id = models.CharField(
        primary_key=True, unique=True, default=uuid.uuid4, editable=False, max_length=36
    )
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ('modified_at',)
