from django.db import models

# Create your models here.
class User(models.Model):
    GENDER_CHOICES = (
        (0,'male'),
        (1,'female')
    )
    user_id = models.CharField(max_length=20,verbose_name='用户ID',primary_key=True)
    user_name = models.CharField(max_length=255,verbose_name='用户昵称')
    user_pw = models.CharField(max_length=10,verbose_name='用户密码')
    user_sex = models.SmallIntegerField(choices=GENDER_CHOICES, default=0,verbose_name='性别')
    user_email = models.CharField(max_length=40,verbose_name='用户邮箱')
    regist_date = models.DateField(verbose_name='注册日期')

class User_log(models.Model):
    user_id = models.CharField(max_length=20,verbose_name='用户ID',primary_key=True)
    user_name = models.CharField(max_length=255, verbose_name='用户昵称')
    act_name = models.CharField(max_length=255, verbose_name='用户动作')
    keywords = models.CharField(max_length=255, verbose_name='搜索关键词')
    uptime = models.DateField(verbose_name='上线时间')
    downtime = models.DateField(verbose_name='下线时间')   #十分钟不答复默认为下线

class User_friends(models.Model):
    user_id = models.CharField(max_length=20,verbose_name='用户ID',primary_key=True)
    user_name = models.CharField(max_length=255, verbose_name='用户昵称')
    friend_id = models.CharField(max_length=20,verbose_name='朋友ID')
    friend_name = models.CharField(max_length=255, verbose_name='朋友昵称')

class admin(models.Model):
    admin_id = models.CharField(max_length=20,verbose_name='管理员ID',primary_key=True)
    admin_name = models.CharField(max_length=255, verbose_name='管理员昵称')
    admin_pw = models.CharField(max_length=10, verbose_name='管理员密码')
    admin_power = models.CharField(max_length=255, verbose_name='管理员权限')

class admin_log(models.Model):
    admin_id = models.CharField(max_length=20, verbose_name='管理员ID', primary_key=True)
    admin_act = models.CharField(max_length=255, verbose_name='管理员操作')
    changetime = models.DateField(verbose_name='操作时间')

    # class Meta:
    #     db_table = 'user'                        #用户信息表
    #     verbose_name = '用户信息'                 #显示在admin站点中的名称
    #     verbose_name_plural = verbose_name       #显示的复数名称
    def _str_(self):
        return self.user_id