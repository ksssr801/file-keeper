from django.db import models

class UserInfo(models.Model):
    user_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=254)
    email_id = models.EmailField(max_length=254)
    password = models.CharField(max_length=254)
    creation_time = models.IntegerField(null=True)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        db_table = 'tbl_user_info'

class LoginInfo(models.Model):
    login_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(UserInfo, db_column='user_id', related_name='user_login_id_mapping')
    token = models.TextField()
    creation_time = models.IntegerField(null=True)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        db_table = 'tbl_login_info'