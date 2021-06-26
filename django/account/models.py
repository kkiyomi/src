from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
# from django.contrib.auth.models import PermissionsMixin

from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from tvshow.models import TVShow, ReleaseV2


class MyAccountManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError('Users must have an email address')
        if not username:
            raise ValueError('Users must have a username')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            username=username,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser):
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    username = models.CharField(max_length=30, unique=True)
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    objects = MyAccountManager()

    def __str__(self):
        return self.username

    # For checking permissions. to keep it simple all admin have ALL permissons
    def has_perm(self, perm, obj=None):
        return self.is_admin

    # Does this user have permission to view this app? (ALWAYS YES FOR SIMPLICITY)
    def has_module_perms(self, app_label):
        return True


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


class ReadingList(models.Model):
    name = models.CharField(max_length=200, default='-1')
    account = models.OneToOneField(
        Account,
        on_delete=models.CASCADE,
        primary_key=True,
    )

    def __str__(self):
        return f"{self.account.username}"


class Serie(models.Model):
    readinglist = models.ForeignKey(ReadingList, on_delete=models.CASCADE)
    tvshow = models.ForeignKey(TVShow, on_delete=models.CASCADE)
    current_release_id = models.IntegerField(default=0)
    release = models.ForeignKey(ReleaseV2, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        unique_together = (("tvshow", "readinglist"),)

    def save(self, *args, **kwargs):
        if self.current_release_id != 0:
            self.release = ReleaseV2.objects.get(id=self.current_release_id)
            self.release.save()
        super(Serie, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.tvshow.title} {self.current_release_id}"
