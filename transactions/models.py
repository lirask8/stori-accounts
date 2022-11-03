from django.db import models
from django.utils.translation import ugettext_lazy as _


from common.models import BaseModel
from accounts.models import User


class Account(BaseModel):
    user = models.ForeignKey(User, models.PROTECT)
    number = models.PositiveIntegerField(null=False, blank=False)
    is_active = models.BooleanField(null=False, default=True)

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = _('Account')
        verbose_name_plural = _('Accounts')


class Transaction(BaseModel):
    account = models.ForeignKey(Account, models.PROTECT)
    id_in_file = models.CharField(max_length=10, null=False, blank=False)
    date = models.DateField(blank=False, null=False)
    amount = models.DecimalField(max_digits=10, decimal_places=2, blank=False, null=False)
    is_credit = models.BooleanField(null=False, default=True)

    class Meta:
        verbose_name = _('Transaction')
        verbose_name_plural = _('Transactions')
