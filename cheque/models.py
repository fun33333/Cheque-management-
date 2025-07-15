# Create your models here.
from django.db import models

STATUS_CHOICES = [
    ('not_started', 'Not Started'),
    ('in_progress', 'In Progress'),
    ('blocked', 'Blocked'),
    ('completed', 'Completed'),
]

PAYMENT_CHOICES = [
    ('cash', 'Cash'),
    ('transfer', 'Transfer'),
]

class Cheque(models.Model):
    description = models.CharField(max_length=255)
    campus = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    cheque_number = models.CharField(max_length=20, unique=True)
    due_date = models.DateField()
    
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='not_started')
    responsible_person = models.CharField(max_length=100)
    approved_by = models.CharField(max_length=100)
    payment_mode = models.CharField(max_length=10, choices=PAYMENT_CHOICES)
    cheque_date = models.DateField()
    
    received_by = models.CharField(max_length=100)
    bill_available = models.BooleanField(default=False)
    shared_on_group = models.BooleanField(default=False)
    bill_attachment = models.FileField(upload_to='bills/', blank=True, null=True)
    notes = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.description} - {self.cheque_number}"
