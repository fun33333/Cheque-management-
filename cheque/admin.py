from django.contrib import admin
from .models import Cheque

@admin.register(Cheque)
class ChequeAdmin(admin.ModelAdmin):
    list_display = ('description', 'campus', 'amount', 'cheque_number', 'status', 'payment_mode', 'cheque_date')
    list_filter = ('status', 'campus', 'payment_mode')
    search_fields = ('description', 'cheque_number', 'responsible_person', 'approved_by')
