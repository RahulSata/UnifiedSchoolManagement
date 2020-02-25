from django.shortcuts import render
from Profiler.models  import *
from django.http import HttpResponse
from django.http import JsonResponse
from .forms import *
from django.template.loader import render_to_string
from django.shortcuts import get_list_or_404, get_object_or_404
# Create your views here.

def control_panel(request):
	return render(request,'Profiler/ControlPanel.html')

def add_student(request):
	All_depts=Department.objects.values('name').distinct()
	All_address= Address.objects.values('city').distinct()
	return render(request,'Profiler/add_student.html',{'All_depts':All_depts,'All_address':All_address})

def add_dept(request):
	print("oosi")
	data = dict()
	if request.method == 'POST':
		form = DepartmentForm(request.POST)
		print("The value is:")
		print(form.is_valid())
		if form.is_valid():
			form.save()
			data['form_is_valid'] = True
			All_depts= Department.objects.all()
			data['html_dropdown_list'] = render_to_string('Profiler/dropdown.html', {'All_depts': All_depts})
			data['html_table_list']=render_to_string('Profiler/dept_table.html', {'All_depts': All_depts})

		else:
			data['form_is_valid'] = False
	else:
		form = DepartmentForm()
	
	context = {'form': form}
	data['html_form'] = render_to_string('Profiler/add_dept.html',context,request=request)
	# return render(request,'Profiler/add_student.html',{'data':data})
	return JsonResponse(data)


def departments(request):
	All_depts = Department.objects.all()
	return render(request, 'Profiler/Departments.html', {'All_depts': All_depts})

def dept_update(request, name):
	department = get_object_or_404(Department, name=name)
	if request.method == 'POST':
		form = DepartmentForm(request.POST, instance=department)
	else:
		form = DepartmentForm(instance=department)
	return save_department_form(request, form, 'Profiler/edit_department_popup.html')

def save_department_form(request, form, template_name):
	data = dict()
	if request.method == 'POST':
		if form.is_valid():
			form.save()
			data['form_is_valid'] = True
			departments = Department.objects.all()
			data['html_book_list'] = render_to_string('Profiler/dept_table.html', {'All_depts': departments})
		else:
			data['form_is_valid'] = False
	context = {'form': form}
	data['html_form'] = render_to_string(template_name, context, request=request)
	return JsonResponse(data)

def address(request):
	All_address=Address.objects.all()
	return render(request,'Profiler/Address/all_address.html',{'All_address':All_address})

def add_address(request):
	data = dict()
	print("csscscscscs")
	if request.method == 'POST':
		form = AddressForm(request.POST)
		print("A")
		print(form.is_valid)
		if form.is_valid():
			print("B")
			form.save()
			data['form_is_valid'] = True
			All_address= Address.objects.all()
			data['html_dropdown_list'] = render_to_string('Profiler/Address/dropdown.html', {'All_address': All_address})
			data['html_table_list']=render_to_string('Profiler/Address/address_table.html', {'All_address': All_address})
		else:
			data['form_is_valid'] = False
	else:
		form = AddressForm()

	context = {'form': form}
	data['html_form'] = render_to_string('Profiler/Address/add_address.html',context,request=request)
	return JsonResponse(data)

def address_update(request,street):
	addressone = get_object_or_404(Address, street=street)
	if request.method == 'POST':
		form = AddressForm(request.POST, instance=addressone)
	else:
		form = AddressForm(instance=addressone)
	return save_Address_form(request, form, 'Profiler/Address/edit_address_popup.html')

def save_Address_form(request, form, template_name):
	data = dict()
	if request.method == 'POST':
		if form.is_valid():
			form.save()
			data['form_is_valid'] = True
			address = Address.objects.all()
			data['html_book_list'] = render_to_string('Profiler/Address/address_table.html', {'All_address': address})
		else:
			data['form_is_valid'] = False
	context = {'form': form}
	data['html_form'] = render_to_string(template_name, context, request=request)
	return JsonResponse(data)
