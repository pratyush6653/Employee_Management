from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Emp

# Create your views here.
def emp_home(request):
    emps=Emp.objects.all()

    return render(request,"emp/home.html",{
        'emps':emps
    })
def add_emp(request):
    if request.method=="POST":

        # data fetch
        emp_name=request.POST.get("emp_Name")
        emp_id=request.POST.get("emp_Id")
        emp_email=request.POST.get("emp_Email")
        emp_phone=request.POST.get("emp_Phone")
        emp_address=request.POST.get("emp_Address")
        emp_department=request.POST.get("emp_Department")
        emp_status=request.POST.get("emp_Status")
        #emp_password=request.POST.get("emp_Password")

        #validation
        # create model object and  set the data 
        e=Emp()
        e.name=emp_name
        e.emp_Id=emp_id
        e.phone=emp_phone
        e.address=emp_address 
        if emp_status is None:
            e.working=False
        else:
            e.working=True
        e.department=emp_department
        e.email=emp_email
        # save the object
        e.save()

        # prepare msg (optional)






        print("Request is coming")
        return  redirect("/employee/home")
    return render(request,"emp/add_emp.html",{})



#deleting the emp
def delete_emp(request,emp_id):
    emp=Emp.objects.get(id=emp_id)
    emp.delete()

    print(emp_id)
    return redirect("/employee/home")