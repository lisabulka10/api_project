from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

from crmlite.models import Company


class User(AbstractUser):
    email = models.EmailField(max_length=256, unique=True)
    is_company_owner = models.BooleanField(default=False)
    company = models.OneToOneField(Company, on_delete=models.SET_NULL, related_name='owner', default=None, null=True, blank=True)

    # is_staff = models.BooleanField(default=False) пока под вопросом
    #is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    #def has_perm(self, perm, obj=None):
    #    return True

    #def has_module_perms(self, app_label):
    #    return True



# class UserManager(BaseUserManager):
#     def create_user(self, email, password=None, **extra_fields):
#         if not email:
#             raise ValueError('The Email field must be set')
#         email = self.normalize_email(email)
#         user = self.model(email=email, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user
#
#     def create_superuser(self, email, password, **extra_fields):
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)
#         return self.create_user(email, password=password, **extra_fields)

