from django.db import models
from django.core.validators import RegexValidator

# Create your models here.
POSITION_DATA = [('manager',"Manager"),('csm',"Customer Service Manager"),
	('om',"Operation Manager"),('do',"Digital Officer"),('icm',"Internal Control Manager"),
	('bs',"Business Manager"),]

class Branch(models.Model):
        name = models.CharField(max_length=50, unique=True, db_index=True)
        phone_regex = RegexValidator(regex=r'^\+?251?\d{9}$', message="Phone number incorrect.")
        phone = models.CharField(validators=[phone_regex], max_length=13, unique=True, default='04xxxxxxxx')
        phone1 = models.CharField(validators=[phone_regex], max_length=13, unique=True, blank=True, default='')
        phone2 = models.CharField(validators=[phone_regex], max_length=13, unique=True, blank=True, default='')
        phone3 = models.CharField(validators=[phone_regex], max_length=13, unique=True, blank=True, default='')
        phone4 = models.CharField(validators=[phone_regex], max_length=13, unique=True, blank=True, default='')

        def __str__(self):
                return self.name

class Manager(models.Model):
        name = models.CharField(max_length=50, unique=True, db_index=True)
        branch = models.OneToOneField(Branch, on_delete=models.CASCADE, primary_key=True)
        position = models.CharField(max_length=100, choices=POSITION_DATA, default="Manager")
        mphone_regex = RegexValidator(regex=r'^\+?251?\d{9}$', message="Phone number incorrect.")
        m_phone = models.CharField(validators=[mphone_regex], max_length=13, unique=True, default='04xxxxxxxx')
        m_phone1 = models.CharField(validators=[mphone_regex], max_length=13, unique=True, blank=True, default='')
        m_phone2 = models.CharField(validators=[mphone_regex], max_length=13, unique=True, blank=True, default='')
        m_phone3 = models.CharField(validators=[mphone_regex], max_length=13, unique=True, blank=True, default='')

        def __str__(self):
                return self.name
