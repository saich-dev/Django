from django.shortcuts import render,redirect
from .models import cust_contact,cab_services,add_cust,payfinal,add_emp,leave_add,rooms
import easygui


def indexlanding(request):
    return render(request,"indexlanding.html")
def roomslanding(request):
    return render(request,"roomslanding.html")
def Gallarylanding(request):
    return render(request,"Gallarylanding.html")
def contactlanding(request):
    return render(request,"contactlanding.html")
def aboutuslanding(request):
    return render(request,"aboutuslanding.html")





def index(request):
    return render(request,"index.html")
def AboutHotel(request):
    return render(request,"About Hotel.html")
def addcustomers(request):
    return render(request,"add customers.html")
def addemployee(request):
    return render(request,"add-employee.html")
def insert_addemployee(request):
    if request.method == 'POST':
        k = add_emp (fname=request.POST['fname'],lname=request.POST['lname'],user_name=request.POST['user_name'],email_id=request.POST['email'],password=request.POST['Password'],
                             confirm_password=request.POST['confirm_password'],emp_id=request.POST['emp_id'],
                             join_date=request.POST['join_date'], phn_number=request.POST['phn_number'], select=request.POST['select'])
        k.save()
        easygui.msgbox("Data added Successfully")
        return redirect('/addemployee')
    else:
        easygui.msgbox("Data not added ")
        return render(request,"add-employee.html")
def Employeelist(request):
    all_data=add_emp.objects.all()
    return render(request,"Employee-list.html",{'all_data':all_data})
def edit_addemp(request,id):
     data1 = add_emp.objects.get(id=id)
     return render(request,"edit addemp.html",{'data1':data1})
def delete2(request,id):
     all_data=add_emp.objects.get(id=id)
     all_data.delete()
     return redirect('/Employeelist')
def update_addemployee(request):
    if request.method == 'POST':
        o=add_emp(fname=request.POST['fname'],lname=request.POST['lname'],user_name=request.POST['user_name'],email_id=request.POST['email'],password=request.POST['Password'],
                             confirm_password=request.POST['confirm_password'],emp_id=request.POST['emp_id'],
                             join_date=request.POST['join_date'], phn_number=request.POST['phn_number'], select=request.POST['select'])
        o.save()
        easygui.msgbox("Data added Successfully")
        return redirect('/Employeelist')
    
def addholiday(request):
    return render(request,"add-holiday.html")
def addleave(request):
    return render(request,"add-leave.html")
def insert_addleave(request):
    if request.method == 'POST':
        g = leave_add( emp_name=request.POST['emp_name'],emp_id=request.POST['emp_id'],select=request.POST['select'],from_date=request.POST['from'],to_date=request.POST['to'],
                             num_of_days=request.POST['num_of_days'],leave_reason=request.POST['leave'])
        g.save()
        easygui.msgbox("Data added Successfully")
        return redirect('/addleave')
    else:
        easygui.msgbox("Data not added ")
        return render(request,"add-leave.html")
def leave(request):
    all_data=leave_add.objects.all()
    return render(request,"leave.html",{'all_data':all_data})    
def edit_addleave(request,id):
     data1 = leave_add.objects.get(id=id)
     return render(request,"edit addleave.html",{'data1':data1})
def delete(request,id):
     all_data = leave_add.objects.get(id=id)
     all_data.delete()
     return redirect('/leave')
def update_addleave(request):
    if request.method == 'POST':
        g = leave_add( emp_name=request.POST['emp_name'],emp_id=request.POST['emp_id'],select=request.POST['select'],from_date=request.POST['from'],to_date=request.POST['to'],
                             num_of_days=request.POST['num_of_days'],leave_reason=request.POST['leave'])
        g.save()
        easygui.msgbox("Data added Successfully")
        return redirect('/leave')
def add(request):
    return render(request,"add.html")
def AdminLoginPage(request):
    return render(request,"Admin Login Page.html")
def Attendence(request):
    return render(request,"Attendence.html")
def Bar(request):
    return render(request,"Bar.html")
def Contact(request):
    return render(request,"Contact.html")
def insert_Contact(request):
    if request.method == 'POST':
       e= cust_contact(fname=request.POST['fname'],email=request.POST['email'],mob_no=request.POST['mob_no'],sub=request.POST['sub'])
       e.save()
       easygui.msgbox("Contact Added Sucessfully")
       return redirect('/Contact')
    else:
        easygui.msgbox("Contact Not Added Sucessfully")
        return render(request,"Contact.html")
    
def insert_add_customers(request):
    if request.method == 'POST':
        cust = add_cust(fname=request.POST['fname'],lname=request.POST['lname'],
                             email=request.POST['email'],phone_number=request.POST['phone_number'],
                             select_room=request.POST['select_rooms'],num_of_guests=request.POST['no_of_guests'],
                             check_in_date=request.POST['check_in_date'],check_out_date=request.POST['check_out_date'])
        cust.save()
        easygui.msgbox("Customer added Successfully")
        return redirect('/addcustomers')
    else:
        easygui.msgbox("Customer not added ")
        return render(request,"addcustomers.html")
def customerdetails(request):
    all_data=add_cust.objects.all()
    return render(request,"customer details.html",{'all_data':all_data}) 
def edit_addcustomers(request,id):
     data1 = add_cust.objects.get(id=id)
     return render(request,"edit addcustomers.html",{'data1':data1})
def delete1(request,id):
     all_data=add_cust.objects.get(id=id)
     all_data.delete()
     return redirect('/customerdetails')
def update_addcustomers(request):
    if request.method == 'POST':
        g = add_cust(fname=request.POST['fname'],lname=request.POST['lname'],
                             email=request.POST['email'],phone_number=request.POST['phone_number'],
                             select_room=request.POST['select_rooms'],num_of_guests=request.POST['no_of_guests'],
                             check_in_date=request.POST['check_in_date'],check_out_date=request.POST['check_out_date'])
        g.save()
        easygui.msgbox("Data added Successfully")
        return redirect('/customerdetails')


def customerlogin(request):
    return render(request,"customer login.html")
def customerprofile(request):
    return render (request,"customer profile.html")
def customerregistration(request):
    return render(request,"customer registration.html")
def dataTables(request):
    return render(request,"dataTables.html")
def employeedetail(request):
    return render(request,"employee detail.html")
def employeedetails(request):
    return render(request,"employee details.html")

def events(request):
    return render(request,"events.html")
def finalpay(request):
    return render(request,"finalpay.html")
def insert_finalpay(request):
    if request.method == 'POST':
        c = payfinal(name=request.POST['name'],email=request.POST['email'],select_card=request.POST['select_card'],name_on_card=request.POST['name_on_card'],cvv=request.POST['cvv'],captcha=request.POST['captcha'])
        c.save()
        easygui.msgbox("Data added Successfully")
        return redirect('/finalpay')
    else:
        easygui.msgbox("Data not added ")
        return render(request,"finalpay.html")
def paymenthistory(request):
    all_data=payfinal.objects.all()
    return render(request,"paymenthistory.html",{'all_data':all_data})

def edit_finalpay(request,id):
     data1 =payfinal.objects.get(id=id)
     return render(request,"edit finalpay.html",{'data1':data1})
def delete5(request,id):
     all_data =payfinal.objects.get(id=id)
     all_data.delete()
     return redirect('/paymenthistory')
def update_finalpay(request):
    if request.method == 'POST':
        c = payfinal(name=request.POST['name'],email=request.POST['email'],select_card=request.POST['select_card'],
                             name_on_card=request.POST['name_on_card'],cvv=request.POST['cvv'],captcha=request.POST['captcha'])      
        c.save()
        easygui.msgbox("Data added Successfully")
        return redirect('/paymenthistory') 
          

    
def forgetpassword(request):
    return render(request,"forget_password.html")
def Gallery(request):
    return render(request,"Gallery.html")
def Holidays(request):
    return render(request,"Holidays.html")
def invoice(request):
    return render(request,"invoice.html")



def Map(request):
    return render(request,"Map.html")
def Order(request):
    return render(request,"Order.html")
def party(request):
    return render(request,'Party.html')
def payments(request):
    return render(request,"payments.html")

def pricing(request):
    return render(request,"pricing.html")
def report(request):
    return render(request,"report.html")
def Resfood(request):
    return render(request,"Res.food.html")
def ResPay(request):
    return render(request,"Res.Pay.html")

def RestarantMenu(request):
    return render(request,"Restarant Menu.html")
def room1(request):
    return render(request,"room1.html")
def insert_room1(request):
    if request.method == 'POST':
        room = rooms(fname=request.POST['fname'],lname=request.POST['lname'],
                             email=request.POST['email'],room_type=request.POST['room_type'],no_of_persons=request.POST['no_of_persons'],
                             check_in_date=request.POST['check_in_date'],mob_no=request.POST['mob_no'],
                             luggage=request.POST['luggage'],)
        room.save()
        easygui.msgbox("Room Booked Successfully")
        return redirect('/room1')
    else:
        easygui.msgbox("Room Booking Failed ")
        return render(request, "room1.html")
def roomhistory(request):
    all_data = rooms.objects.all()
    return render(request,"roomhistory.html",{'all_data':all_data})
def edit_room1(request,id):
     data1 = rooms.objects.get(id=id)
     return render(request,"edit room1.html",{'data1':data1})
def delete6(request,id):
     all_data=rooms.objects.get(id=id)
     all_data.delete()
     return redirect('/roomhistory')
def update_room1(request):
    if request.method == 'POST':
        room=rooms (fname=request.POST['fname'],lname=request.POST['lname'],email=request.POST['email'],select_room=request.POST['select_room'],
                             num_of_guests=request.POST['num_of_guests'],check_in_date=request.POST['check_in_date'],
                             check_out_date=request.POST['check_out_date'],flight_number=request.POST['flight_number'],special_request=request.POST['special_request'],select_city=request.POST['select_city'])
       
        room.save()
        easygui.msgbox("Data added Successfully")
        return redirect('/roomhistory')

def room2(request):
    return render(request,"room2.html")
def room3(request):
    return render(request,"room3.html")
def spa(request):
    return render(request,"spa.html")
def Customer(request):
    return render(request,"Customer.html")
def Transportation(request):
    return render(request,"Transportation.html")
def insert_Transportation(request):
    if request.method == 'POST':
        cab=cab_services (fname=request.POST['fname'],lname=request.POST['lname'],email=request.POST['email'],Cab_Type=request.POST['Cab_Type'],
                             num_of_persons=request.POST['num_of_persons'],Pickup_Date_time=request.POST['Pickup_Date_time'],
                             Mobile_Number=request.POST['Mobile_Number'],Luggage_Size=request.POST['Luggage_Size'])
        cab.save()
        easygui.msgbox("Cabservices added Successfully")
        return redirect('/Transportation')
    else:
        easygui.msgbox("Cabservices not added ")
        return render(request,"Transportation.html")
def cabhistory(request):
    all_data=cab_services.objects.all()
    return render(request,"cabhistory.html",{'all_data':all_data}) 
def edit_Transportation(request,id):
     data1 = cab_services.objects.get(id=id)
     return render(request,"edit Transportation.html",{'data1':data1})
def delete3(request,id):
     all_data=cab_services.objects.get(id=id)
     all_data.delete()
     return redirect('/cabhistory')
def update_Transportation(request):
    if request.method == 'POST':
        cab=cab_services (fname=request.POST['fname'],lname=request.POST['lname'],email=request.POST['email'],Cab_Type=request.POST['Cab_Type'],
                             num_of_persons=request.POST['num_of_persons'],Pickup_Date_time=request.POST['Pickup_Date_time'],
                             Mobile_Number=request.POST['Mobile_Number'],Luggage_Size=request.POST['Luggage_Size'])
       
        cab.save()
        easygui.msgbox("Data added Successfully")
        return redirect('/cabhistory')











 
  
    
def AboutHotelpanel(request):
    return render(request,"About Hotel panel.html")
def Gallerypanel(request):
    return render(request,"Gallerypanel.html")
def CustamerRatingpanel(request):
    return render(request,"Custamer Rating panel.html")
def Mappanel(request):
    return render(request,"Map panel.html")
def Room1panel(request):
    return render(request,"Room1 panel.html")

def insert_Room1panel(request):
    if request.method == 'POST':
        room = rooms(fname=request.POST['fname'],lname=request.POST['lname'],
                             email=request.POST['email'],room_type=request.POST['room_type'],no_of_persons=request.POST['no_of_persons'],
                             check_in_date=request.POST['check_in_date'],mob_no=request.POST['mob_no'],
                             luggage=request.POST['luggage'],)
        room.save()
        easygui.msgbox("Room Booked Successfully")
        return redirect('/Room1panel')
    else:
        easygui.msgbox("Room Booking Failed ")
        return render(request,"Room1panel.html")

def Room2panel(request):
    return render(request,"Room2 panel.html")
def Room3panel(request):
    return render(request,"Room3 panel.html")
def Pricingpanel(request):
    return render(request,"Pricing panel.html")
def Partypanel(request):
    return render(request,"Party panel.html")
def Eventspanel(request):
    return render(request,"Events panel.html")
def Paymentspanel(request):
    return render(request,"Payments panel.html")
def Cabpanel(request):
    return render(request,"Cab panel.html")
def Restarentpanel(request):
    return render(request,"Restarent panel.html")
def ResFoodpanel(request):
    return render(request,"Res Food panel.html")
def Respaypanel(request):
    return render(request,"Res Pay panel.html")
def Orderpanel(request):
    return render(request,"Order panel.html")
def Barpanel(request):
    return render(request,"Bar panel.html")
def Spapanel(request):
    return render(request,"Spa panel.html")
def Contactpanel(request):
    return render(request,"Contactpanel.html")
def emppanel(request):
    return render(request,"emppanel.html")
def addpanel(request):
    return render(request,"addpanel.html")
def Emplistpanel(request):
    return render(request,"Emplistpanel.html")
def leavepanel(request):
    return render(request,"leavepanel.html")
def addleavepanel(request):
    return render(request,"addleavepanel.html")
def Attendencepanel(request):
    return render(request,"Attendencepanel.html")
def finalpaypanel(request):
    return render(request,"finalpay panel.html")
def emploginpanel(request):
    return render(request,"emploginpanel.html")
def cusregistrationpanel(request):
    return render(request,"cus registration panel.html")
def manager(request):
    return render(request,"manager.html")
def Accountent(request):
    return render(request,"Accountent.html")
def SupportingStaff(request):
    return render(request,"Supporting Staff.html")
def edit(request):
    return render(request,"edit.html")
def receptionist(request):
    return render(request,"receptionist.html")
def customerdetailspanel(request):
    return render(request,"customer details panel.html")
def editcustomers(request):
    return render(request,"edit customers.html")
def supervisor(request):
    return render(request,"supervisor.html")


              