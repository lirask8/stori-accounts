from django.db import models
from django.contrib.auth.hashers import make_password
from django.utils.translation import ugettext_lazy as _

from common.models import BaseModel


class User(BaseModel):
    name = models.CharField(max_length=100, null=False, blank=False)
    lastName = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(max_length=100, null=False, blank=False)
    password = models.CharField(max_length=100, null=False, blank=False)
    isActive = models.BooleanField(null=False, default=True)

    def is_authenticated(self):
        return True

    def makepassword(self):
        self.password = make_password(self.password)

    def save(self, *args, **kwargs):
        if self.password.find('pbkdf2_sha256$') == -1 and len(self.password) != 77:
            self.makepassword()
        super(User, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('User')
        verbose_name_plural = _('Users')