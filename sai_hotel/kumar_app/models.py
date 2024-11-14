from django.db import models
# Create your models here.
class add_cust(models.Model):
    fname=models.CharField(max_length=200)
    lname=models.CharField(max_length=200)
    email=models.EmailField(max_length=200)
    phone_number=models.CharField(max_length=200)
    select_room=models.CharField(max_length=200)
    num_of_guests=models.CharField(max_length=200)
    check_in_date=models.CharField(max_length=200)
    check_out_date=models.CharField(max_length=200)


    
    def __str__(self):
        return self.fname
    
class add_emp(models.Model):
    fname=models.CharField(max_length=200)
    lname=models.CharField(max_length=200)
    user_name=models.CharField(max_length=200)
    email_id=models.EmailField(max_length=200)
    password=models.CharField(max_length=200)
    confirm_password=models.CharField(max_length=200)
    emp_id=models.CharField(max_length=200)
    join_date=models.CharField(max_length=200)
    phn_number=models.CharField(max_length=200)
    select=models.CharField(max_length=200)
    

    def __str__(self):
        return self.fname
    
class leave_add(models.Model):
    emp_name=models.CharField(max_length=200)
    emp_id=models.CharField(max_length=200)
    select=models.CharField(max_length=200)
    from_date=models.CharField(max_length=200)
    to_date=models.CharField(max_length=200)
    num_of_days=models.CharField(max_length=200)
    leave_reason=models.CharField(max_length=200)


    
    def __str__(self):
        return self.emp_name 
    
class adminlogin(models.Model):
    email=models.EmailField(max_length=200)
    password=models.CharField(max_length=200)
    
    
    def __str__(self):
        return self.email
    
class cust_contact(models.Model):
    fname=models.CharField(max_length=200)
    email=models.CharField(max_length=200)   
    mob_no=models.CharField(max_length=200)
    sub=models.CharField(max_length=200)
    
    
    def __str__(self):
        return self.fname 
    
class payfinal(models.Model):
    name=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    select_card=models.CharField(max_length=200)
    name_on_card=models.CharField(max_length=200)
    cvv=models.CharField(max_length=200)
    captcha=models.CharField(max_length=200)
    
    
    def __str__(self):
        return self.name 
    
class party_type(models.Model):
    fname=models.CharField(max_length=200)
    lname=models.CharField(max_length=200)
    email=models.EmailField(max_length=200)
    party_hall_type=models.CharField(max_length=200)
    num_of_guests=models.CharField(max_length=200)
    start_date=models.DateField(max_length=200)
    end_date=models.DateField(max_length=200)
    special_request=models.CharField(max_length=200)
    occation_of_party=models.CharField(max_length=200)
    order=models.CharField(max_length=200)
    

    def __str__(self):
        return self.fname
    

class payments(models.Model):
    fname=models.CharField(max_length=200)
    lname=models.CharField(max_length=200)
    email=models.EmailField(max_length=200)
    select_room=models.EmailField(max_length=200)
    num_of_guests=models.CharField(max_length=200)
    Arrival_date=models.DateField(max_length=200)
    Departure_Date=models.DateField(max_length=200)
    flight_number=models.CharField(max_length=200)
    special_request=models.CharField(max_length=200)
    

    def __str__(self):
        return self.fname
    
class respay(models.Model):
    name=models.CharField(max_length=200)
    email_id=models.EmailField(max_length=200)
    city=models.CharField(max_length=200)
    phn_number=models.CharField(max_length=200)
    zip=models.CharField(max_length=200)
    location=models.CharField(max_length=200)
    address=models.CharField(max_length=200)


    def __str__(self):
        return self.name
    
class rooms(models.Model):
    fname=models.CharField(max_length=200)
    lname=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    room_type=models.CharField(max_length=200)  
    no_of_persons=models.CharField(max_length=200)
    check_in_date=models.CharField(max_length=200)
    mob_no=models.CharField(max_length=200)
    luggage=models.CharField(max_length=200)


    
    def __str__(self):
        return self.fname
    
class room2(models.Model):
    fname=models.CharField(max_length=200)
    lname=models.CharField(max_length=200)
    email=models.EmailField(max_length=200)
    select_room=models.CharField(max_length=200)
    num_of_guests=models.CharField(max_length=200)
    check_in_date=models.DateField(max_length=200)
    check_out_date=models.DateField(max_length=200)
    flight_number=models.CharField(max_length=200)
    special_request=models.CharField(max_length=200)
    select_city=models.CharField(max_length=200)
    

    def __str__(self):
        return self.fname
    
class room3(models.Model):
    fname=models.CharField(max_length=200)
    lname=models.CharField(max_length=200)
    email=models.EmailField(max_length=200)
    select_room=models.CharField(max_length=200)
    num_of_guests=models.CharField(max_length=200)
    check_in_date=models.DateField(max_length=200)
    check_out_date=models.DateField(max_length=200)
    flight_number=models.CharField(max_length=200)
    special_request=models.CharField(max_length=200)
    select_city=models.CharField(max_length=200)
    

    def __str__(self):
        return self.fname
    
class cab_services(models.Model):
    fname=models.CharField(max_length=200)
    lname=models.CharField(max_length=200)
    email=models.CharField(max_length=200)
    Cab_Type=models.CharField(max_length=200)
    num_of_persons=models.CharField(max_length=200)
    Pickup_Date_time=models.CharField(max_length=200)
    Mobile_Number=models.CharField(max_length=200)
    Luggage_Size=models.CharField(max_length=200)
    
    

    def __str__(self):
        return self.fname
    