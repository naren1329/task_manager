from django.shortcuts import render,redirect
from . models import task_table,records

def task_homepage(request):
    return render(request,'task_home.html')

def register(request):
    if request.method == 'POST':
        rname=request.POST.get("name")
        remail=request.POST.get("email")
        rpassword=request.POST.get("password")
        if not task_table.objects.filter(email=remail).exists():
            ins=task_table(name=rname,email=remail,password=rpassword)
            ins.save()
            return redirect(reg_login_fun)
    return render(request,'register.html')

def reg_login_fun(request):
    global logemail
    if request.method =='POST':
        logemail=request.POST.get("lemail")
        logpassword=request.POST.get("lpassword")
        if task_table.objects.filter(email=logemail,password=logpassword):
            return redirect(add_task)
    return render(request,'login.html')

def forgot_fun(request):
    if request.method =='POST':
        f_email=request.POST.get("f_email")
        if task_table.objects.filter(email=f_email).exists():
            new_password=request.POST.get("n_password")
            confirm_password=request.POST.get("c_password")
            if new_password == confirm_password:
                task_table.objects.filter(email=f_email).update(password=new_password)
                return redirect(reg_login_fun)
    return render(request,'forgot.html')   

def dashboard(request):
    s=task_table.objects.get(email=logemail)
    obj=records.objects.filter(user=s)
    if request.method=='POST':
        search=request.POST.get('searchbutton')
        s=task_table.objects.get(email=logemail)
        obj=records.objects.filter(user=s,title__icontains=search)
    sort=request.GET.get('sort')
    if sort == 'priority':
        obj=obj.order_by('priority')
    elif sort == 'duedate':
        obj=obj.order_by('duedate')        
    return render(request,'alltask.html',{'obj':obj})

def add_task(request):
    s=task_table.objects.get(email=logemail)
    if request.method =='POST':
        title=request.POST.get('title')
        description=request.POST.get('description')
        duedate=request.POST.get('duedate')
        priority=request.POST.get('priority')
        status=request.POST.get('status')
        ins=records(title=title,description=description,duedate=duedate,priority=priority,status=status,user=s)
        ins.save()
        return redirect(dashboard)
    return render(request,'tasks.html')   

def delete_task(request,id):
    if request.method =='POST':
        s=records.objects.filter(id=id)
        s.delete()
        return redirect(dashboard)
    return render(request,'delete.html')

def update_task(request,id):
    s=records.objects.filter(id=id)
    if request.method =='POST':
         state=request.POST.get('status')
         records.objects.filter(id=id).update(status=state)
         return redirect(dashboard)
    return render(request,'update.html',{'s':s})
        
