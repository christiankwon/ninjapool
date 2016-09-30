from __future__ import unicode_literals
from django.db import models
import re, bcrypt

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

# Create your models here.
class UserManager(models.Manager):
    def register(self, data):
        errors = []

        fname = data['fname']
        lname = data['lname']
        email = data['email']
        passw = data['pass']
        cpass = data['cpass']
        address = data['address']
        city = data['city']
        state = data['state']
        zcode = data['zip']

        if len(email) < 1:
            errors.append("An email must be provided.")
        elif not EMAIL_REGEX.match(email):
            errors.append("Invalid email provided.")
        elif self.filter(email=email).exists():
            errors.append("Email is already in use. Please log in or try another email.")

        if len(fname) < 2:
            errors.append("First name must be atleast two characters long.")
        elif re.search(r'[0-9]', fname):
            errors.append("First name cannot contain a number.")
        elif not fname.isalpha():
            errors.append("First name can only have letters.")

        if len(lname) < 2:
            errors.append("Last name must be atleast two characters long.")
        elif re.search(r'[0-9]', lname):
            errors.append("Last name cannot contain a number.")
        elif not lname.isalpha():
            errors.append("Last name can only have letters.")

        if len(passw) < 1:
            errors.append("Password cannot be empty.")
        elif len(passw) < 8:
            errors.append("Password must be longer than 8 characters.")

        if len(cpass) < 1:
            errors.append("Confirm password cannot be empty.")
        elif passw != cpass:
            errors.append("Passwords must match.")

        if len(address) < 1:
            errors.append("An address is required to register.")

        if len(city) < 1:
            errors.append("A city is required to register.")
        elif not city.isalpha():
            errors.append("A city can only have letters.")

        if len(state) < 1:
            errors.append("A state is required to register.")
        elif not state.isalpha():
            errors.append("A state can only have letters.")

        if len(zcode) < 1:
            errors.append("A zip code is required to register.")

        if not errors:
            passw_enc = bcrypt.hashpw(passw.encode(), bcrypt.gensalt())
            data = {
                'first_name': fname,
                'last_name': lname,
                'email': email,
                'password': passw_enc,
                'address': address,
                'city': city,
                'state': state,
                'zipcode': zcode,
            }

            self.create(**data)

            return (True, "Account successfully created. Please log in now.")
        else:
            return (False, errors)


    def login(self, data):
        email = data['email']
        passw = data['pass']

        if not email or not passw:
            return (False, "Both email and password fields are required to login.")

        try:
            data = self.get(email=email)
            hashed = data.password.encode()
        except:
            return (False, "Email does not exist. Please try another.")

        if bcrypt.hashpw(passw.encode(), hashed) == hashed:
            return (True, "Successful login!", data)
        else:
            return (False, "Password is incorrect. Please try again.")


    def new_car(self, data, user_id):
        data = {
            'owner': self.get(id=user_id),
            'make': data['make'],
            'model': data['model'],
            'year': data['year'],
            'seats': data['seats'],
        }

        try:
            newcar = Car.objects.create(**data)
            
            return (True, "Successfully created a car!", newcar)

        except:
            return (False, "Something went wrong.")


class User(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    email = models.EmailField()
    password = models.CharField(max_length=200)
    carpool_id = models.IntegerField(null=True)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    state = models.CharField(max_length=200)
    zipcode = models.IntegerField()
    arrive_by = models.TimeField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()


class Car(models.Model):
    make = models.CharField(max_length=200)
    model = models.CharField(max_length=200)
    year = models.IntegerField()
    seats = models.IntegerField()
    owner = models.ForeignKey(User)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
