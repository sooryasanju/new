from django.db import models
import datetime


# Create your models here.
class Course(models.Model):
    """This is for adding course details such as coursename,coursefee """
    course_name=models.CharField(max_length=150,unique=True,)
    course_fee=models.IntegerField()

    def __str__(self):

        return self.course_name
class Batch(models.Model):
    """This is for adding Batch details such as batchname """
    course_name=models.ForeignKey(Course,on_delete=models.CASCADE)
    batch_name=models.CharField(max_length=150,unique=True)

    def __str__(self):

        return self.batch_name
class Role(models.Model):
    """This is for adding Role details such as role name """
    role_name=models.CharField(max_length=200,unique=True)


    def __str__(self):

        return self.role_name


class ClassRoom(models.Model):
    """This is for adding class details such as class name """
    class_name = models.CharField(max_length=200,unique=True)

    def __str__(self):
        return self.class_name

class Hr(models.Model):
    """This is for adding HR details such as HR name,user name, password """
    hr_name = models.CharField(max_length=200)
    hr_username=models.CharField(max_length=200,unique=True)
    hr_password=models.CharField(max_length=100)

    def __str__(self):
        return self.hr_name

class Trainer(models.Model):
    """This is for adding Trainer details such as Trainer name,Trainer password """
    t_id=models.IntegerField(auto_created=True)
    course_name=models.ForeignKey(Course,on_delete=models.CASCADE)
    trainer_name=models.CharField(max_length=200)
    trainer_mobile = models.IntegerField()
    trainer_doj = models.DateTimeField(default=datetime.date.today())
    trainer_email = models.CharField(max_length=200)
    trainer_username=models.CharField(max_length=200,unique=True)
    trainer_password=models.CharField(max_length=100)
    role_name=models.ForeignKey(Role,on_delete=models.CASCADE)

    def __str__(self):
        return self.trainer_name

class TimeTable(models.Model):
    """This is for adding Timetable details such as Timetable date,and time  """
    batch_name=models.ForeignKey(Batch,on_delete=models.CASCADE)
    class_name=models.ForeignKey(ClassRoom,on_delete=models.CASCADE)
    timetable_date=models.DateField()
    start_time=models.TimeField()
    end_time=models.TimeField()
    time_flag=models.IntegerField(default=0)

    def __str__(self):
        return self.timetable_date
class User(models.Model):
    """This is for adding User details  """
    u_id=models.IntegerField(auto_created=True)
    user_name=models.CharField(max_length=200)
    user_address=models.CharField(max_length=250)
    user_mobile=models.IntegerField()
    user_doj=models.DateTimeField(default=datetime.date.today())
    user_email=models.CharField(max_length=200)
    user_username=models.CharField(max_length=200,unique=True)
    user_password=models.CharField(max_length=200)
    confirm_password=models.CharField(max_length=200)
    course_name = models.ForeignKey(Course, on_delete=models.CASCADE)
    batch_name = models.ForeignKey(Batch, on_delete=models.CASCADE)
    user_payment=models.IntegerField()
    role_name= models.ForeignKey(Role, on_delete=models.CASCADE)
    image=models.ImageField(upload_to='profile_image/',blank=True,default='profile_image/default.jpeg')

    def __str__(self):
        return self.user_username

class Placement(models.Model):
    """This is for adding placement details  """

    placement_date=models.DateField()
    course_name = models.ForeignKey(Course, on_delete=models.CASCADE)
    user_name=models.ForeignKey(User,on_delete=models.CASCADE)
    batch_name = models.ForeignKey(Batch, on_delete=models.CASCADE)
    company=models.CharField(max_length=200)
    image=models.ImageField(upload_to='images/',default=None)
    def __str__(self):
        return self.company
class Feedback(models.Model):

    user_username = models.ForeignKey(User, on_delete=models.CASCADE)
    batch_name = models.ForeignKey(Batch, on_delete=models.CASCADE)
    trainer_name=models.ForeignKey(Trainer,on_delete=models.CASCADE)
    feedback_date=models.DateTimeField(default=datetime.date.today())
    feedback_data = models.CharField(max_length=2000)
    feedback_comment=models.CharField(max_length=1000,null=True)
    def __str__(self):
        return self.feedback_data









