from django.urls import path,include
from.import views
urlpatterns = [
    
    
    path('',views.indexlanding,name='indexlanding'),
    path('indexlanding',views.indexlanding,name='indexlanding'),
    path('aboutuslanding',views.aboutuslanding,name='aboutuslanding'),
    path('contactlanding',views.contactlanding,name='contactlanding'),
    path('Gallarylanding',views.Gallarylanding,name='Gallarylanding'),
    path('roomslanding',views.roomslanding,name='roomslanding'),
    
    
    
    path('',views.AboutHotel,name='AboutHotel'),
    path('addcustomers',views.addcustomers,name='addcustomers'),
    path('edit_addcustomers/<int:id>',views.edit_addcustomers,name='edit_addcustomers'),
    path('delete1/<int:id>',views.delete1,name='delete1'),
    path('update_addcustomers',views.update_addcustomers,name='update_addcustomers'),
    path('insert_add_customers',views.insert_add_customers,name='insert_add_customers'),
    
    path('addemployee',views.addemployee,name='addemployee'),
    path('insert_addemployee',views.insert_addemployee,name='insert_addemployee'),
    path('edit_addemp/<int:id>',views.edit_addemp,name='edit_addemp'),
    path('delete2/<int:id>',views.delete2,name='delete2'),
    path('update_addemployee',views.update_addemployee,name='update_addemployee'),
    
    
    path('addholiday',views.addholiday,name='addholiday'),
    
    path('addleave',views.addleave,name='addleave'),
    path('insert_addleave',views.insert_addleave,name='insert_addleave'),
    path('edit_addleave/<int:id>',views.edit_addleave,name='edit_addleave'),
    path('delete/<int:id>',views.delete,name='delete'),
    path('update_addleave',views.update_addleave,name='update_addleave'),
    
    
    
    
    path('add',views.add,name='add'),
    path('index',views.index,name='index'),
    path('AdminLoginPage',views.AdminLoginPage,name='AdminLoginPage'),
    path('Attendence',views.Attendence,name='Attendence'),
    path('Bar',views.Bar,name='Bar'),
    path('Contact',views.Contact,name='Contact'),
    path('insert_Contact',views.insert_Contact,name="insert_Contact"),
    path('insert add customers',views.insert_add_customers,name='insert add customers'),
    path('customerdetails',views.customerdetails,name='customerdetails'),
    path('customerlogin',views.customerlogin,name='customerlogin'),
    path('customerprofile',views.customerprofile,name='customerprofile'),
    path('customerregistration',views.customerregistration,name='customerregistration'),
    path('dataTables',views.dataTables,name='AboutdataTables'),
    path('employeedetail',views.employeedetail,name='employee detail'),
    path('employeedetails',views.employeedetails,name='employee details'),
    path('Employeelist',views.Employeelist,name='Employee-list'),
    path('events',views.events,name='events'),
    
    path('finalpay',views.finalpay,name='finalpay'),
    path('insert_finalpay',views.insert_finalpay,name='insert_finalpay'),
    path('edit_finalpay/<int:id>',views.edit_finalpay,name='edit_finalpay'),
    path('delete5/<int:id>',views.delete5,name='delete5'),
    path('update_finalpay',views.update_finalpay,name='update_finalpay'),
    
    
    
    path('forgetpassword',views.forgetpassword,name='forgetpassword'),
    path('Gallery',views.Gallery,name='Gallery'),
    path('Holidays',views.Holidays,name='Holidays'),
    path('invoice',views.invoice,name='invoice'),
    path('leave',views.leave,name='leave'),
    path('Map',views.Map,name='Map'),
    path('Order',views.Order,name='Order'),
    
    path('payments',views.payments,name='payments'),
    path('paymenthistory',views.paymenthistory,name='paymenthistory'),
    
    
    path('pricing',views.pricing,name='pricing'),
    path('report',views.report,name='report'),
    path('Resfood',views.Resfood,name='Resfood'),
    path('ResPay',views.ResPay,name='ResPay'),
    
    path('RestarantMenu',views.RestarantMenu,name='RestarantMenu'),
    path('room1',views.room1,name='room1'),
    path('insert_room1',views.insert_room1,name='insert_room1'),
    path('edit_room1/<int:id>',views.edit_room1,name='edit_room1'),
    path('delete6/<int:id>',views.delete6,name='delete6'),
    path('update_room1',views.update_room1,name='update_'),
    
    path('roomhistory',views.roomhistory,name='roomhistory'),
    path('room2',views.room2,name='room2'),
    path('room3',views.room3,name='room3'),
    path('party',views.party,name='party'),
    path('spa',views.spa,name='spa'),
    path('Customer',views.Customer,name='Customer'),
    
    path('Transportation',views.Transportation,name='Transportation'),
    path('insert_Transportation',views.insert_Transportation,name='insert_Transportation'),
    path('edit_Transportation/<int:id>',views.edit_Transportation,name='edit_Transportation'),
    path('delete3/<int:id>',views.delete3,name='delete3'),
    path('update_Transportation',views.update_Transportation,name='update_Transportation'),
    
    
    path('AboutHotelpanel',views.AboutHotelpanel,name='AboutHotelpanel'),
    path('Gallerypanel',views.Gallerypanel,name='Gallerypanel'),
    path('CustamerRatingpanel',views.CustamerRatingpanel,name='CustamerRatingpanel'),
    path('Mappanel',views.Mappanel,name='Mappanel'),
    
    path('Room1panel',views.Room1panel,name='Room1panel'),
    path('insert_Room1panel',views.insert_Room1panel,name='insert_Room1panel'),
    
   
    
    path('Room2panel',views.Room2panel,name='Room2panel'),
    path('Room3panel',views.Room3panel,name='Room3panel'),
    path('Pricingpanel',views.Pricingpanel,name='Pricingpanel'),
    path('Partypanel',views.Partypanel,name='Partypanel'),
    path('Eventspanel',views.Eventspanel,name='Eventspanel'),
    path('Paymentspanel',views.Paymentspanel,name='Paymentspanel'),
    path('Cabpanel',views.Cabpanel,name='Cabpanel'),
    path('cabhistory',views.cabhistory,name='cabhistory'),
    path('Restarentpanel',views.Restarentpanel,name='Restarentpanel'),
    path('ResFoodpanel',views.ResFoodpanel,name='ResFoodpanel'),
    path('Respaypanel',views.Respaypanel,name='Respaypanel'),
    path('Orderpanel',views.Orderpanel,name='Orderpanel'),
    path('Barpanel',views.Barpanel,name='Barpanel'),
    path('emppanel',views.emppanel,name='emppanel'),
    path('Contactpanel',views.Contactpanel,name='Contactpanel'),
    path('addpanel',views.addpanel,name='addpanel'),
    path('Emplistpanel',views.Emplistpanel,name='Emplistpanel'),
    path('leavepanel',views.leavepanel,name='leavepanel'),
    path('addleavepanel',views.addleavepanel,name='addleavepanel'),
    path('Attendencepanel',views.Attendencepanel,name='Attendencepanel'),
    path('finalpaypanel',views.finalpaypanel,name='finalpaypanel'),
    
    
    path('Spapanel',views.Spapanel,name='Spapanel'),
    path('emploginpanel',views.emploginpanel,name='emploginpanel'),
    path('cusregistrationpanel',views.cusregistrationpanel,name='cusregistrationpanel'),
    path('manager',views.manager,name='manager'),
    path('Accountent',views.Accountent,name='Accountent'),
    path('SupportingStaff',views.SupportingStaff,name='SupportingStaff'),
    path('edit',views.edit,name='edit'),
    path('receptionist',views.receptionist,name='receptionist'),
    path('customerdetailspanel',views.customerdetailspanel,name='customerdetailspanel'),
    path('editcustomers',views.editcustomers,name='editcustomers'),
    path('supervisor',views.supervisor,name='supervisor'),
    
      
]
