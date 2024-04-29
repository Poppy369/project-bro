from django.contrib import admin
from .models import EmpData, Location, Department
# Register your models here.

@admin.register(EmpData)
class YourModelAdmin(admin.ModelAdmin):
    # Define customizations for the admin interface
    list_display = ('emp_id', 'emp_name', 'location','department')  # Example: Display these fields in the list view
    # list_filter = ('field1',)  # Example: Add filter options for field1
    # search_fields = ('field1', 'field2')  # Example: Add search functionality for these fields
    # Add more customizations as needed
    
admin.site.register(Location)
admin.site.register(Department)