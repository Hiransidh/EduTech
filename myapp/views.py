from django.shortcuts import render, redirect,HttpResponse
from myapp.models import *
from datetime import datetime
import datetime

from django.core.files.storage import FileSystemStorage
# Create your views here.


def login1(request):
    return render(request, 'login.html')

def login_post(request):
    if request.method =='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        data =login.objects.all()
        flag = 0
       
        for i in data:
            if i.email == username and i.password == password:
                type = i.category
           
                flag = 1
                if type == 'admin':
                    request.session['admin'] = username
                    return HttpResponse('''<script>alert('Login Succesfull');window.location="/admin_home/"</script>''')
                elif type == 'Branch Staff':
                    request.session['Branch Staff'] = username
                    return HttpResponse('''<script>alert('Login Succesfull');window.location="/branch_home/"</script>''')
                elif type == 'Course Coordinator':
                    request.session['Course Coordinator'] = username
                    return HttpResponse('''<script>alert('Login Succesfull');window.location="/coordinator_home/"</script>''')
                elif type == 'Teacher':
                    request.session['Teacher']= username
                    return HttpResponse('''<script>alert('Login Succesfull');window.location="/teacher_home/"</script>''')
                elif type == 'Mentor':
                    request.session['Mentor'] = username
                    return HttpResponse('''<script>alert('Login Succesfull');window.location="/mentor_home/"</script>''')
                elif type == 'Student':
                    request.session['Student'] = username
                    return HttpResponse('''<script>alert('Login Succesfull');window.location="/student_home/"</script>''')
                else:
                    return HttpResponse('''<script>alert('Invalid User');window.location="/login/"</script>''')
def logout(request):
    # Clear session data
    request.session.clear()
    # Redirect to login page
    return redirect('/login/')

# def login1_post(request):
#    if request.method=='POST':
#         uname=request.POST.get('email')
#         paword=request.POST.get('password')

#         data=login.objects.all()
#         flag=0

#         for i in data:
#             if uname==i.username and paword==i.password:
#                 type=i.category
#                 flag=1
#                 if type=="Admin":
#                     request.session['adm']=uname
#                     return HttpResponse('''<script>alert('Login Succesfull');window.location="/login/"</script>''')

#                 # elif type=="User":
#                 #     request.session['use']=uname
#                 #     return redirect("/user_home")
#                 elif type=="Unit":
#                     request.session['unit']=uname
#                     return HttpResponse('''<script>alert('Login Succesfull');window.location="/unit_login/"</script>''')

#                 else:
#                     return HttpResponse("Invalid Category")
#         if flag==0:
#             return HttpResponse("InvalidUser")

def student_reg(request):
    data = branch.objects.all()
    data1 = course.objects.all()
    return render(request, 'student_reg.html', {'data': data, 'data1': data1})

def student_reg_post(request):
    data = student()
    data.student_image = request.FILES['student_image']
    data.student_name = request.POST.get('student_name')
    data.dob2 = request.POST.get('dob')
    data.email = request.POST.get('email')
    data.phone = request.POST.get('phone')
    data.qualification = request.POST.get('qualification')
    data.house = request.POST.get('house')
    data.street = request.POST.get('street')
    data.city = request.POST.get('city')
    data.state = request.POST.get('state')
    data.pincode = request.POST.get('pincode')
    branch_id = request.POST.get('branch')
    branch_instance = branch.objects.get(branch_id=branch_id)
    data.branch_id = branch_instance
    course_id = request.POST.get('course')
    course_instance = course.objects.get(course_id=course_id)
    data.course_id = course_instance
    data.save()
    data3=student.objects.last()
    request.session['std']=data3.student_id
    return redirect('/attendtest/')
## ---------- Admin -----------


def admin_home(request):
    return render(request, 'Admin/admin_home.html')

def eligibility_view(request):
    return render(request, 'Admin/eligibility.html')

def eligibility_post(request):
    data = eligibility()
    data.question = request.POST.get('question')
    data.answer = request.POST.get('answer')
    data.option1 = request.POST.get('option1')
    data.option2 = request.POST.get('option2')
    data.option3 = request.POST.get('option3')
    data.option4 = request.POST.get('option4')
    data.save()
    return render(request, 'Admin/eligibility.html')

def view_eligibility(request):
    data = eligibility.objects.all()
    return render(request, 'Admin/view_elig_quest.html', {'data': data})

def attendtest(request):
    data = eligibility.objects.all()
    return render(request, 'Admin/attendtest.html', {'data': data})

def option1(request,opid,qid):
    data = eligibility.objects.get(question_id=qid)
    
    if 'test1_id' not in request.session:
        
        print(data.option1)
        print(data.answer)
        if data.option1==data.answer:
            
                        data2=Result()
                        data2.STUDENT_id=request.session['std']
                        data2.impression=1
                        data2.status="active"
                        data2.date=datetime.datetime.now().strftime ("%Y-%m-%d")
                        data2.time= datetime.datetime.now().strftime('%H:%M:%S')
                        data2.save()
                        data3=Result.objects.last()
                        print(data3.test_id)
                        
                        request.session['test1_id']=data3.test_id
    else:
        
        if data.option1==data.answer:
                    
                    result_id=request.session['test1_id'] 
                    
                    data2=Result.objects.get(test_id=result_id)
                    data2.impression=int(data2.impression)+1
                    
                    data2.save()               
            
    data.status="Attended"
    data.save()
    
    data=eligibility.objects.filter(status="Not Attended")
    return render(request,"Admin/attendtest.html",{'data':data})

def option2(request,opid,qid):
    data = eligibility.objects.get(question_id=qid)
    if 'test1_id' not in request.session:
        if data.option2==data.answer:
            
                        data2=Result()
                        
                        data2.STUDENT_id=request.session['std']
                        data2.impression=1
                        data2.status="active"
                        data2.date=datetime.datetime.now().strftime ("%Y-%m-%d")
                        data2.time= datetime.datetime.now().strftime('%H:%M:%S')
                        data2.save()
                        data3=Result.objects.last()
                        print(data3.test_id)
                        
                        request.session['test1_id']=data3.test_id
    else:
        if data.option2==data.answer:
                    result_id=request.session['test1_id'] 
                    
                    
                    
                    
                    data2=Result.objects.get(test_id=result_id)
                    data2.impression=int(data2.impression)+1
                    
                    data2.save()         
                    
    data.status="Attended"
    data.save()
    
    data=eligibility.objects.filter(status="Not Attended")
    return render(request,"Admin/attendtest.html",{'data':data})

def option3(request,opid,qid):
    data = eligibility.objects.get(question_id=qid)
    if 'test1_id' not in request.session:
        if data.option3==data.answer:
            
                        data2=Result()
                        
                        data2.STUDENT_id=request.session['std']
                        data2.impression=1
                        data2.status="active"
                        data2.date=datetime.datetime.now().strftime ("%Y-%m-%d")
                        data2.time= datetime.datetime.now().strftime('%H:%M:%S')
                        data2.save()
                        data3=Result.objects.last()
                        print(data3.test_id)
                        
                        request.session['test1_id']=data3.test_id
    else:
        if data.option3==data.answer:
                    result_id=request.session['test1_id'] 
                    
                    
                    
                    
                    data2=Result.objects.get(test_id=result_id)
                    data2.impression=int(data2.impression)+1
                    
                    data2.save()                        
    data.status="Attended"
    data.save()
    
    data=eligibility.objects.filter(status="Not Attended")
    return render(request,"Admin/attendtest.html",{'data':data})


def option4(request,opid,qid):
    data = eligibility.objects.get(question_id=qid)
    if 'test1_id' not in request.session:
        if data.option4==data.answer:
            
                        data2=Result()
                        
                        data2.STUDENT_id=request.session['std']
                        data2.impression=1
                        data2.status="active"
                        data2.date=datetime.datetime.now().strftime ("%Y-%m-%d")
                        data2.time= datetime.datetime.now().strftime('%H:%M:%S')
                        data2.save()
                        data3=Result.objects.last()
                        print(data3.test_id)
                        
                        request.session['test1_id']=data3.test_id
    else:
        if data.option4==data.answer:
                    print(request.session['test1_id'] )
                    result_id=request.session['test1_id'] 
                    
                    
                    
                    
                    data2=Result.objects.get(test_id=result_id)
                    data2.impression=int(data2.impression)+1
                    
                    data2.save()                       
    data.status="Attended"
    data.save()
    
    data=eligibility.objects.filter(status="Not Attended")
    return render(request,"Admin/attendtest.html",{'data':data})

def finishexam(request):
        
        if 'test1_id' not in request.session:
            data2=eligibility.objects.all()
            for x in data2:
                x.status="Not Attended"
                x.save()
            return render(request,"Admin/result11.html")
        else:
            
            resultid=request.session['test1_id'] 
        
            data=Result.objects.get(test_id=resultid)
            data.status="completed"
            data.save()
            data2=eligibility.objects.all()
            for x in data2:
                x.status="Not Attended"
                x.save()


            
            ss=request.session['test1_id']      
            del request.session['test1_id']   
            

            data7=Result.objects.get(test_id=ss)
            
        if int(data7.impression)>=6:
            return redirect('/eligible/')
        else:
            var = student.objects.get(student_id=request.session['std'])
            var.delete()
            return HttpResponse('''<script>alert('Sorry!! You are not eligible to join the course as you have not secured the minimum mark');window.location="/login/"</script>''')
            
            
        
def eligible(request):
    data = Result.objects.get(STUDENT_id=request.session['std'])
    return render(request,"eligible.html",{'data':data})

def not_eligible(request):
    return render(request,"not_eligible.html") 

def eligibility_test(request):
    data = eligibility.objects.all()
    return render(request, 'eligibility_test.html', {'data': data})


def add_course(request):
    return render(request,'Admin/add_course.html')

# def add_course_post(request):
#     data = course()
#     data.course_id = request.POST.get('course_id')
#     data.course_name = request.POST.get('course_name')
#     data.description = request.POST.get('description')
#     data.course_duration = request.POST.get('course_duration')
#     data.no_of_installments = request.POST.get('no_of_installments')
#     data.save()
#     return render(request, 'Admin/add_course.html')

def add_course_post(request):
    if request.method == 'POST':
        data = course()
        data.course_id = request.POST.get('course_id')
        data.course_name = request.POST.get('course_name')
        data.description = request.POST.get('description')
        data.course_duration = request.POST.get('course_duration')
        data.no_of_installments = request.POST.get('no_of_installments')
        data.save()

        # get the main subject
        subject_name = request.POST.get('subject')
        if subject_name:
            # create a new subject with the main subject and link it to the course
            subject = Subject(name=subject_name, course=data)
            subject.save()

        # get the additional subjects
        i = 0
        while True:
            additional_subject_name = request.POST.get('additional_subjects_' + str(i))
            if additional_subject_name is None:
                break
            # create a new subject with the additional subject and link it to the course
            additional_subject = Subject(name=additional_subject_name, course=data)
            additional_subject.save()
            i += 1

    return render(request, 'Admin/add_course.html')

# def view_course(request):
#     data =course.objects.all()
#     data1 = Subject.objects.filter(course__in=data)
#     return render(request, 'Admin/view_course.html', {'data': data,'data1':data1})

def view_course(request):
    data = course.objects.all()
    course_subjects = []
    for c in data:
        subjects = Subject.objects.filter(course=c)
        subject_names = [subject.name for subject in subjects]
        course_subjects.append((c, subject_names))
    return render(request, 'Admin/view_course.html', {'course_subjects': course_subjects})



def edit_course(request,id):
    data = course.objects.get(course_id=id)
    return render(request, 'Admin/edit_course.html', {'data': data})

def edit_course_post(request):
    id = request.POST.get('course_id')
    data = course.objects.get(course_id=id)
    data.course_name = request.POST.get('course_name')
    data.description = request.POST.get('description')
    data.course_duration = request.POST.get('course_duration')
    data.no_of_installments = request.POST.get('no_of_installments')
    data.save()
    return redirect('/view_course/')

def delete_course(request,id):
    data = course.objects.get(course_id=id)
    data.delete()
    return redirect('/view_course/')

def add_branch(request):
    return render(request, 'Admin/add_branch.html')

def add_branch_post(request):
    data = branch()
    data.branch_id = request.POST.get('branch_id')
    data.branch_name = request.POST.get('branch_name')
    data.location = request.POST.get('location')
    data.email = request.POST.get('email')
    data.phone = request.POST.get('phone')
    data.save()
    return render(request, 'Admin/add_branch.html')

def view_branch(request):
    data = branch.objects.all()
    return render(request, 'Admin/view_branch.html', {'data': data})

def edit_branch(request,id):
    data = branch.objects.get(branch_id=id)
    return render(request, 'Admin/edit_branch.html', {'data': data})

def edit_branch_post(request):
    id = request.POST.get('branch_id')
    data = branch.objects.get(branch_id=id)
    data.branch_name = request.POST.get('branch_name')
    data.location = request.POST.get('location')
    data.email = request.POST.get('email')
    data.phone = request.POST.get('phone')
    data.save()
    return redirect('/view_branch/')

def delete_branch(request,id):
    data = branch.objects.get(branch_id=id)
    data.delete()
    return redirect('/view_branch/')

def add_staff(request):
    data=branch.objects.all()
    return render(request, 'Admin/add_staff.html',{'data':data})

def add_staff_post(request):
    data = staff()
    data.staff_id = request.POST.get('staff_id')
    data.staff_name = request.POST.get('staff_name')
    data.email = request.POST.get('email')
    data.phone = request.POST.get('phone')
    data.qualification= request.POST.get('qualification')
    data.house = request.POST.get('house')
    data.city = request.POST.get('city')
    data.state = request.POST.get('state')
    data.pincode = request.POST.get('pincode')
    data.staff_type = request.POST.get('staff_type')
    data.branch_id_id = request.POST.get('branch_name')
    data.save()
    
    data2=login()
    data2.email=request.POST.get('email')
    data2.password=request.POST.get('phone')
    data2.category=request.POST.get('staff_type')
    data2.save()
    
    return render(request, 'Admin/add_staff.html')

def view_staff(request):
    data = staff.objects.all()
    return render(request, 'Admin/view_staff.html', {'data': data})

def delete_staff(request,id):
    data = staff.objects.get(staff_id=id)
    data.delete()
    return redirect('/view_staff/')

def edit_staff(request,id):
    data = staff.objects.get(staff_id=id)
    return render(request, 'Admin/edit_staff.html', {'data': data})

def edit_staff_post(request):
    id = request.POST.get('staff_id')
    data = staff.objects.get(staff_id=id)
    data.staff_name = request.POST.get('staff_name')
    data.email = request.POST.get('email')
    data.phone = request.POST.get('phone')
    data.qualification= request.POST.get('qualification')
    data.house = request.POST.get('house')
    data.city = request.POST.get('city')
    data.state = request.POST.get('state')
    data.pincode = request.POST.get('pincode')
    data.staff_type = request.POST.get('staff_type')
    data.save()
    return redirect('/view_staff/')

def view_complaint(request):
    data = complaint.objects.all()
    return render(request, 'Admin/view_complaint.html', {'data': data})

def add_fees(request):
    data = course.objects.all()
    return render(request, 'Admin/add_fees.html', {'data': data})


def add_fees_post(request):
    data= fee()
    data.course_id_id=request.POST.get('course_name')
    data.amount=float(request.POST.get('amount'))  # Convert 'amount' to an integer
    data.payment_per_month= float(data.amount/data.course_id.no_of_installments)
    data.save()
    return render(request, 'Admin/add_fees.html')

def view_fees(request):
    data = fee.objects.all()
    
    return render(request, 'Admin/view_fees.html', {'data': data})

    # inst = []
    # for i in data:
    #     course = i.course_id
    #     course_duration = course.course_duration
    #     no_of_installments = course.no_of_installments
    #     amount = i.amount 
    #     inst.append(round(float(amount / no_of_installments), 0))
    # inst_str = ', '.join(str(x) for x in inst)
    # inst = []
    # for i in data:
    #     d1=i.amount/i.course_id.no_of_installments
    #     inst.append(round(d1))
        
    
    
# ------BRANCH--------
def branch_home(request):
    return render(request,'Branch/branch_home.html')

# def add_student(request):
#     data = batch.objects.all()
#     return render(request, 'Branch/add_student.html', {'data': data})

# def add_student_post(request):
    # from datetime import datetime
    
    # data = student()
    # data.student_name = request.POST.get('student_name')
    # data.dob2 = request.POST.get('dob')
    # if data.dob2 > str(datetime.now().date()):
    #     return HttpResponse('Invalid Date of Birth')
    # data.email = request.POST.get('email')
    # data.phone = request.POST.get('phone')
    # data.qualification= request.POST.get('qualification')
    # data.house = request.POST.get('house')
    # data.city = request.POST.get('city')
    # data.state = request.POST.get('state')
    # data.pincode = request.POST.get('pincode')
    # student_image=request.FILES['student_image']
    
    # fs=FileSystemStorage()
    # filename=fs.save(student_image.name,student_image)
    # uploaded_file_url1 = fs.url(filename)
    # data.student_image=uploaded_file_url1
    # data.batch_id_id = request.POST.get('batch_name')
    # data.save()
    # return render(request, 'Branch/add_student.html')

def view_student(request):
    data = student.objects.all()
    return render(request, 'Branch/view_student.html', {'data': data})

def view_student2(request,id):
    data =student.objects.get(student_id=id)
    return render(request, 'Branch/view_student2.html', {'data': data})

def view_staff1(request):
    data = staff.objects.all()
    return render(request, 'Branch/view_staff.html', {'data': data})

def view_fee1(request):
    data = batch.objects.all()
    return render(request, 'Branch/fee.html', {'data': data})

def view_fee2(request,id):
    data = batch.objects.get(batch_id=id)
    
    return render(request, 'Branch/view_classfee.html', {'data': data})


# ------- Course Coordinator --------

def coordinator_home(request):
    return render(request, 'Coordinator/coordinator_home.html')

def add_class(request):
    data = course.objects.all()
    data1 = staff.objects.filter(staff_type='mentor')
    
    
    return render(request, 'Coordinator/add_class.html', {'data': data, 'data1': data1})

def add_class_post(request):
    data = batch()

    data1=staff.objects.get(email=request.session['Course Coordinator'])
    
    data.batch_name = request.POST.get('class_name')
    data.start_time = request.POST.get('start_time')
    data.end_time = request.POST.get('end_time')
    data.course_id_id = request.POST.get('course')
    data.staff_id_id = request.POST.get('mentor')
    data.branch_id_id = data1.branch_id_id
    data.save()
    return render(request, 'Coordinator/add_class.html')

def view_class(request):
    data = batch.objects.all()
    return render(request, 'Coordinator/view_class.html', {'data': data})





# ------MENTOR--------

def mentor_home(request):
    return render(request, 'Mentor/mentor_home.html')

def add_timetable(request):
    data1 = batch.objects.all()
    data2=staff.objects.filter(staff_type='teacher')
    data3 = Subject.objects.all()
    return render(request, 'Mentor/add_timetable.html', {'data1': data1, 'data2':data2,'data3':data3})
    
def add_timetable_post(request):
    data = timetable()
    data.batch_id_id = request.POST.get('batch')
    data.staff_id_id = request.POST.get('teacher')
    data.subject_id_id = request.POST.get('subject')
    data.day = request.POST.get('day')
    data.start_time = request.POST.get('start_time')
    data.end_time = request.POST.get('end_time')
    data.save()
    return render(request, 'Mentor/add_timetable.html')

def view_timetable(request):
    data = timetable.objects.all()
    return render(request, 'Mentor/view_timetable.html', {'data': data})
    
# ------TEACHER--------

def teacher_home(request):
    return render(request, 'Teacher/teacher_home.html')
    

# ------STUDENT--------

def send_complaint(request):
    return render(request, 'Student/send_complaint.html')

def send_complaint_post(request):
    data = complaint()
    data.complaint_id = request.POST.get('complaint_id')
    data.complaint = request.POST.get('complaint')
    data.date = datetime.now()
    data.status = request.POST.get('status')
    data.save()
    return render(request, 'Student/send_complaint.html')