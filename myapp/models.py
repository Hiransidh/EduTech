from django.db import models

# Create your models here.

class login(models.Model):
    login_id = models.AutoField(primary_key=True)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    class Meta:
        db_table = "login"
        

class course(models.Model):
    course_id = models.AutoField(primary_key=True)
    course_name = models.CharField(max_length=100)
    course_duration = models.IntegerField()
    description = models.TextField()
    no_of_installments = models.IntegerField()
    
    class Meta:
        db_table = "course"
        
        
class Subject(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    course = models.ForeignKey('course',on_delete=models.CASCADE)
    
    class Meta:
        db_table = "subject"
        

class branch(models.Model):
    branch_id = models.IntegerField(primary_key=True)
    branch_name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    class Meta:
        db_table = "branch"
        
class staff(models.Model):
    staff_id = models.IntegerField(primary_key=True)
    staff_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    qualification = models.CharField(max_length=100,default="")
    house= models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    pincode = models.IntegerField()
    staff_type = models.CharField(max_length=100,default="")
    branch_id = models.ForeignKey('branch',on_delete=models.CASCADE)
    class Meta:
        db_table = "staff"
        
class complaint(models.Model):
    complaint_id = models.IntegerField(primary_key=True)
    complaint = models.TextField()
    date= models.DateField()
    status = models.CharField(max_length=100,default="pending")
    STUDENT= models.ForeignKey('student',on_delete=models.CASCADE)
    BRANCH= models.ForeignKey('branch',on_delete=models.CASCADE)
    class Meta:
        db_table = "complaint"


        
class fee(models.Model):
    fee_id = models.AutoField(primary_key=True)
    amount = models.FloatField()
    payment_per_month = models.FloatField()
    course_id = models.ForeignKey('course',on_delete=models.CASCADE)
    class Meta:
        db_table = "fee"
   
        
class student(models.Model):
    student_id = models.AutoField(primary_key=True)
    student_image = models.ImageField(upload_to='images/student/',default="")
    student_name = models.CharField(max_length=100)
    dob2 = models.DateField()
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    qualification = models.CharField(max_length=100,default="")
    house= models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    pincode = models.IntegerField()
    batch_id = models.ForeignKey('batch',on_delete=models.CASCADE)
    class Meta:
        db_table = "student"
        
        
class batch(models.Model):
    batch_id = models.AutoField(primary_key=True)
    batch_name = models.CharField(max_length=100)
    course_id = models.ForeignKey('course',on_delete=models.CASCADE)
    branch_id = models.ForeignKey('branch',on_delete=models.CASCADE)
    staff_id = models.ForeignKey('staff',on_delete=models.CASCADE)
    class Meta:
        db_table = "batch"
        

class timetable(models.Model):
    timetable_id = models.AutoField(primary_key=True)
    batch_id = models.ForeignKey('batch', on_delete=models.CASCADE)
    subject_id = models.ForeignKey('Subject', on_delete=models.CASCADE)
    day = models.CharField(max_length=100)
    time = models.CharField(max_length=100)
    staff_id = models.ForeignKey('staff',on_delete=models.CASCADE)
            
    class Meta:
        db_table = "timetable"
        
class eligibility(models.Model):
    question_id = models.AutoField(primary_key=True)
    question = models.TextField()
    option1 = models.CharField(max_length=100)
    option2 = models.CharField(max_length=100)
    option3 = models.CharField(max_length=100)
    option4 = models.CharField(max_length=100)
    answer = models.CharField(max_length=100)
    class Meta:
        db_table = "eligibility"