# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Customer(models.Model):
    name = models.CharField(max_length=30, blank=True, null=True)
    id_customer_category = models.ForeignKey('CustomerCategory', models.DO_NOTHING, db_column='id_customer_category', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customer'


class CustomerCategory(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    name = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'customer_category'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Item(models.Model):
    name = models.CharField(max_length=30, blank=True, null=True)
    serial_number = models.CharField(unique=True, max_length=30)
    id_item_category = models.ForeignKey('ItemCategory', models.DO_NOTHING, db_column='id_item_category')

    class Meta:
        managed = False
        db_table = 'item'


class ItemCategory(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    name = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'item_category'


class Penerimaan(models.Model):
    tgl = models.DateField(blank=True, null=True)
    serial_number_item = models.ForeignKey(Item, models.DO_NOTHING, db_column='serial_number_item')
    id_customer = models.ForeignKey(Customer, models.DO_NOTHING, db_column='id_customer')
    keterangan = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'penerimaan'


class Pengeluaran(models.Model):
    tgl = models.DateField(blank=True, null=True)
    serial_number_item = models.ForeignKey(Item, models.DO_NOTHING, db_column='serial_number_item')
    id_customer = models.ForeignKey(Customer, models.DO_NOTHING, db_column='id_customer')
    keterangan = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pengeluaran'

class V_Item(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    stock = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'v_item'

class V_Out(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    serial_number = models.CharField(unique=True, max_length=30)
    item_name = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'v_pengeluaran'