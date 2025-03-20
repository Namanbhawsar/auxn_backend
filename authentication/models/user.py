from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models

from auxn_backend.base_models import BaseIndexedModel
from auxn_backend.constants import CASE_INSENSITIVE_DB_COLLATION
from auxn_backend.mixins import HistoryModelMixin

USER_TYPES = (
    ("buyer", "Buyer"),
    ("admin", "Admin"),
    ("seller", "Seller")
)


class User(
    AbstractBaseUser,
    PermissionsMixin,
    BaseIndexedModel,
    HistoryModelMixin,
):
    email = models.EmailField(unique=True, db_collation=CASE_INSENSITIVE_DB_COLLATION)
    validated_email = models.BooleanField(null=False, default=False)
    first_name = models.TextField(max_length=50, blank=True, db_collation=CASE_INSENSITIVE_DB_COLLATION)
    middle_name = models.TextField(max_length=50, blank=True, null=True,db_collation=CASE_INSENSITIVE_DB_COLLATION)
    last_name = models.TextField(max_length=50, blank=True, db_collation=CASE_INSENSITIVE_DB_COLLATION)

    phone = models.CharField(max_length=20, blank=True)
    country_code = models.CharField(max_length=5,blank=True)
    user_type = models.CharField(max_length=10, choices=USER_TYPES, default='buyer')

    USERNAME_FIELD = 'email'
    @property
    def contact_number(self):
        return str(self.country_code) + str(self.phone)

    @property
    def full_name(self):
        names = [self.first_name if self.first_name else "", self.middle_name if self.middle_name else "",
                 self.last_name if self.last_name else ""]
        return " ".join(names)
