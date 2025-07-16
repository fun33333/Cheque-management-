from django.contrib import admin
from django import forms
from .models import Project, Employee, Cheque

# -------------------------------
# Custom Form for Cheque (Date Pickers)
# -------------------------------
class ChequeAdminForm(forms.ModelForm):
    class Meta:
        model = Cheque
        fields = '__all__'
        widgets = {
            'due_date': forms.DateInput(attrs={'type': 'date'}),
            'cheque_date': forms.DateInput(attrs={'type': 'date'}),
        }

# -------------------------------
# Project Admin
# -------------------------------
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['name', 'is_head_office']
    list_filter = ['is_head_office']
    search_fields = ['name']

# -------------------------------
# Employee Admin
# -------------------------------
@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['name', 'designation', 'project']
    list_filter = ['designation', 'project']
    search_fields = ['name', 'designation']

# -------------------------------
# Cheque Admin
# -------------------------------
@admin.register(Cheque)
class ChequeAdmin(admin.ModelAdmin):
    form = ChequeAdminForm
    list_display = [
        'description', 'cheque_number', 'amount', 'status',
        'project', 'responsible_person', 'approved_by', 'cheque_date'
    ]
    list_filter = ['status', 'approved_by', 'payment_mode', 'project']
    search_fields = ['description', 'cheque_number', 'notes']
    raw_id_fields = ['responsible_person']  # Dropdown replaced with search field
    readonly_fields = ['cheque_number']     # Cheque number is auto & read-only
    date_hierarchy = 'cheque_date'
