from django.contrib import admin

from transactions.models import Account, Transaction


class AccountAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'number',
        'is_active',
    )


class TransactionAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'account',
        'id_in_file',
        'date',
        'amount',
        'is_credit',
    )


admin.site.register(Account, AccountAdmin)
admin.site.register(Transaction, TransactionAdmin)
