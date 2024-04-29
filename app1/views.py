from ast import And
from django.shortcuts import render
from django.shortcuts import redirect
from .models import EmpData

# Create your views here.

def dataSearch(request):
    data = EmpData.objects.all()
    return render(request,'dataSearch/data_search.html',{'datas': data})


def dataForm(request):    
    if request.method == "POST":
        # Process the form data
        selected_option = request.POST.get('selectOption')
        id_field = request.POST.get('idField')
        text_id_field = request.POST.get('textIdField')
        name_field = request.POST.get('nameField')
        text_name_field = request.POST.get('textNameField')
        
        if text_name_field is not None:
            text_name_field = text_name_field.lower()
    
        
        # Perform any additional processing or querying based on the form data
        if selected_option == "id":
            if text_id_field:
                data = EmpData.objects.filter(emp_id=text_id_field)
            # Query data based on ID
            elif id_field:
                data = EmpData.objects.filter(emp_id=id_field)
            else:
                data = None
        elif selected_option == "name":
            # Query data based on Name
            if name_field:
                data = EmpData.objects.filter(emp_name=name_field)
            elif text_name_field:
                data = EmpData.objects.filter(emp_name=text_name_field)
            else:
                data = None
        else:
            # Handle the case when "Select a Field" is chosen
            data = None  # Or any other appropriate action
        
        # Pass the form data and result data to the template
        # for i in data:
            # print(i)
        print(type(data))
        return render(request, 'dataSearch/data_search.html', {
            'datas': EmpData.objects.all(),  # Pass all data for dropdown options
            'selected_option': selected_option,
            'id_field': id_field,
            'name_field': name_field,
            'result_data': data,
        })
    
    # If the request method is not POST, redirect back to the dataSearch view
    return redirect('dataSearch')