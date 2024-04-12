import datetime
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser, User
from django.db import models
from django.utils.translation import gettext_lazy as _
from localflavor.br.models import BRCPFField, BRCNPJField

from rest_framework.authtoken.models import Token
from django.contrib.auth.signals import user_logged_in
from django.core.validators import MaxValueValidator, MinValueValidator

# class Company(models.Model):
#     created_at = models.DateField(auto_now_add=True)
#     cnpj = BRCNPJField(_('Business Document Number'), unique=True)
#     name = models.CharField(_('Business Name'), max_length=512)
    
#     def __str__(self):
#         return self.name
    
#     def to_dict(self):
#         return {"name": self.name, "cnpj": self.cnpj}
    
#     def to_json(self):
#         return {"name": self.name, "cnpj": self.cnpj}

#     class Meta:
#         verbose_name_plural = _("Companies")
#         verbose_name = _("Company")

# class Employee(models.Model):
    
#     name = models.CharField(_('Employee Name'), max_length=512)
#     cpf = BRCPFField(_('Document Number'), unique=True) 
#     company = models.ForeignKey(Company, on_delete=models.CASCADE)
#     entered_at = models.DateField(auto_now_add=True)
#     exited_at = models.DateField(null=True, blank=True)
#     vacation_days = models.IntegerField(default=0)
#     def __str__(self) -> str:
#         return str(self.name)

#     def get_company(self):
#         try:
#             return self.company
#         except Exception as e:
#             print(e)
#             return    
  

class User(AbstractUser):
    pass
class Quote(models.Model):

    ITEM_TYPE = [
        ('residencial', 'residencial'),
        ('automovel', 'automovel'),
        ('eletro-domestico','eletro-domestico'),
        ('eletro-portateis', 'eletro-portateis'),
        ('eletronicos', 'reconstrução')
    ]
     
    ITEM_CONDITION = [
        ('novo', 'novo'),
        ('seminovo', 'seminovo'),
        ('usado', 'usado')
    ]

    PAYMENT_TYPE = [
        ('a vista', 'a vista'),
        ('36 parcelas', 'a vista'),
        ('a vista', 'a vista'),
        ('a vista', 'a vista'),
    ]

    item_name = models.CharField(_('Item Name'), max_length=512)
    # item_type = models.CharField(_('Item Type'), max_length=512)
    item_description = models.CharField(_('Item Description'), max_length=512)
    item_value = models.DecimalField(_('Item Value'), decimal_places=2, max_digits=999999)
    installments = models.IntegerField(_('Parcelas'), default=1,
        validators=[
            MaxValueValidator(100),
            MinValueValidator(1)
        ])
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    # def to_dict(self):
    #     return {"name": self.name, "cnpj": self.cnpj}
    
    # def to_json(self):
    #     return {"name": self.name, "cnpj": self.cnpj}

