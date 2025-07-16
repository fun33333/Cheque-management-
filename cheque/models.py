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

APPROVED_BY_CHOICES = [
    ('Head Sir', 'Head Sir'),
    ('Madam', 'Madam'),
    ('Saad', 'Saad'),
    ('Abdullah', 'Abdullah'),
]

class Project(models.Model):
    name = models.CharField(max_length=100)
    is_head_office = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Employee(models.Model):
    name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} ({self.designation} - {self.project.name})"

class Cheque(models.Model):
    description = models.CharField(max_length=255)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

    amount = models.DecimalField(max_digits=12, decimal_places=2)
    cheque_number = models.CharField(max_length=20, unique=True, blank=True)
    due_date = models.DateField()

    status = models.CharField(max_length=50, choices=STATUS_CHOICES)
    responsible_person = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, blank=True)
    other_responsible_name = models.CharField(max_length=100, blank=True)  # if not an employee
    approved_by = models.CharField(max_length=100, choices=APPROVED_BY_CHOICES)
    payment_mode = models.CharField(max_length=10, choices=PAYMENT_CHOICES)
    cheque_date = models.DateField()

    received_by = models.CharField(max_length=100, blank=True)
    bill_available = models.BooleanField(default=False)
    shared_on_group = models.BooleanField(default=False)
    bill_attachment = models.FileField(upload_to='bills/', blank=True, null=True)
    notes = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.cheque_number:
            last_cheque = Cheque.objects.order_by('id').last()
            next_number = 90001 if not last_cheque else int(last_cheque.cheque_number.replace('CHK', '')) + 1
            self.cheque_number = f"CHK{next_number}"
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.description} - {self.cheque_number}"
