#encoding:utf-8
from django.db import models
# from django.contrib.auth.models import (
#     BaseUserManager, AbstractBaseUser
# )


# class MyUserManager(BaseUserManager):
#     def create_user(self, email, date_of_birth, password=None):
#         """
#         Creates and saves a User with the given email, date of
#         birth and password.
#         """
#         if not email:
#             raise ValueError('Users must have an email address')

#         user = self.model(
#             email=MyUserManager.normalize_email(email),
#             date_of_birth=date_of_birth,
#         )

#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, email, date_of_birth, password):
#         """
#         Creates and saves a superuser with the given email, date of
#         birth and password.
#         """
#         user = self.create_user(email,
#             password=password,
#             date_of_birth=date_of_birth
#         )
#         user.is_admin = True
#         user.save(using=self._db)
#         return user


# class MyUser(AbstractBaseUser):
#     email = models.EmailField(
#         verbose_name='email address',
#         max_length=255,
#         unique=True,
#         db_index=True,
#     )
#     date_of_birth = models.DateField()
#     is_active = models.BooleanField(default=True)
#     is_admin = models.BooleanField(default=False)

#     objects = MyUserManager()

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ['date_of_birth']

#     def get_full_name(self):
#         # The user is identified by their email address
#         return self.email

#     def get_short_name(self):
#         # The user is identified by their email address
#         return self.email

#     def __unicode__(self):
#         return self.email

#     def has_perm(self, perm, obj=None):
#         "Does the user have a specific permission?"
#         # Simplest possible answer: Yes, always
#         return True

#     def has_module_perms(self, app_label):
#         "Does the user have permissions to view the app `app_label`?"
#         # Simplest possible answer: Yes, always
#         return True

#     @property
#     def is_staff(self):
#         "Is the user a member of staff?"
#         # Simplest possible answer: All admins are staff
#         return self.is_admin

from django.contrib.auth.models import User
from django.db import models
from datetime import datetime
from time import strftime
#
# Custom field types in here.
#
class UnixTimestampField(models.DateTimeField):
    """UnixTimestampField: creates a DateTimeField that is represented on the
    database as a TIMESTAMP field rather than the usual DATETIME field.
    """
    def __init__(self, null=False, blank=False, **kwargs):
        super(UnixTimestampField, self).__init__(**kwargs)
        # default for TIMESTAMP is NOT NULL unlike most fields, so we have to
        # cheat a little:
        self.blank, self.isnull = blank, null
        self.null = True # To prevent the framework from shoving in "not null".

    def db_type(self, connection):
        typ=['TIMESTAMP']
        # See above!
        if self.isnull:
            typ += ['NULL']
        if self.auto_created:
            # typ += ['default CURRENT_TIMESTAMP on update CURRENT_TIMESTAMP']
            typ += ['default CURRENT_TIMESTAMP']
        return ' '.join(typ)

    def to_python(self, value):
        return datetime.from_timestamp(value)

    def get_db_prep_value(self, value, connection, prepared=False):
        if value==None:
            return None
        return strftime('%Y%m%d%H%M%S',value.timetuple())

    def to_python(self, value):
        return value
USER_TYPE = (#The first element in each tuple is the actual value to be stored, and the second element is the human-readable name.
    ('M', 'MERCHANT'),
    ('E', 'Employee'),
    ('C', 'CUSTOMER'),
    ('A', 'ADMIN'),
    )
class UserPofile(models.Model):
    user = models.OneToOneField(User)
    department = models.CharField(max_length=100) 
    access_ip = models.CharField(max_length=12, default='*')
    code = models.CharField(max_length=25, default='')#编号
    user_type = models.CharField(choices=USER_TYPE, max_length=6)
    create_time = UnixTimestampField()
    belong_to = models.ForeignKey('self', related_name='+', blank=True, null=True)


from django.db.models.signals import post_save
# method for updating
def add_userprofile(sender, instance, created, **kwargs):
    
    if created:
        e = UserPofile()
        e.user = instance
        UserPofile.save(e)

# register the signal
post_save.connect(add_userprofile, sender=User, dispatch_uid="add_userprofile")   
