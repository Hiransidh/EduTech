from django.shortcuts import render, redirect,HttpResponse
from myapp.models import *
from datetime import datetime
from django.http import JsonResponse

from django.core.files.storage import FileSystemStorage
from datetime import datetime
from dateutil.relativedelta import relativedelta
 
def login1(request):
    data = branch.objects.all()
    data2 = fee.objects.all()
    return render(request, 'login.html',{'data':data,'data2':data2})

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

def back_to_login(request):
    var = student.objects.get(student_id=request.session['Student'])
    var.delete()
    return redirect('/login/')

def enquiry_(request):
    return render(request, 'enquire.html')

def enquiry_post(request):
    data = enquiry()
    data.name = request.POST.get('name')
    data.email = request.POST.get('email')
    data.date = datetime.now()
    data.enquiry = request.POST.get('message')
    data.save()
    return render(request, 'login.html')


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
    data.status = 'pending'
    
    if student.objects.filter(email=request.POST.get('email')).exists():
        return HttpResponse('''<script>alert('Email already exists');window.location="/login/"</script>''')
    else:
        data.save()
        data3=student.objects.last()
        request.session['Student']=data3.student_id
        return redirect('/attendtest/')

def payment1(request):
    data=student.objects.get(student_id=request.session['Student'])
    data2=fee.objects.get(course_id_id=data.course_id_id)
    return render(request, 'payment.html', {'data': data2})  


from datetime import datetime

def process_payment(request):
    data = student_fee_payment()
    var = student.objects.get(student_id=request.session['Student'])
    data.student_id_id = var.student_id
    
    data3 = fee.objects.get(course_id_id=data.student_id.course_id_id)
    
    data2 = bank.objects.get(bank_id=1)
    if data2.card_number == request.POST.get('card_number') and data2.cvv == request.POST.get('cvv') and data2.exp_date == request.POST.get('exp_date'):
        
        if data2.amount>=float(request.POST.get('amount')):
            data.paid_amount = request.POST.get('amount')
            data.student_id = var
            data.course_id = var.course_id
            data.payment_date = datetime.now()
            data.due_date = datetime.now()
            data.instalment_no = 1
            data.status = 'paid'
            data.save()
            data5=course.objects.get(course_id=var.course_id_id)
            n1=int(data5.no_of_installments)
            n2=int(data5.course_duration)
            n3=int(n2/n1)
            print("jjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjjj")
            print(n3)
            c=1
            for x in range(n3-1):
                data11=student_fee_payment.objects.last()
                date_after_month = data11.due_date+ relativedelta(months=n3)
                print('Today: ',datetime.today().strftime('%d/%m/%Y'))
                print('After Month:', date_after_month.strftime('%d/%m/%Y'))
                


                data = student_fee_payment()
                data.paid_amount = request.POST.get('amount')
                data.student_id_id = var.student_id
                data.course_id = var.course_id
                data.payment_date ="0001-01-01"
                data.due_date = date_after_month.strftime('%Y-%m-%d')
                data10=student_fee_payment.objects.last()
                data.instalment_no =int(data10.instalment_no)+1
                data.status = ''
                data.save()
                
            
        else:
            return HttpResponse('''<script>alert('Insufficient Balance');window.location="/login/"</script>''')
    
    else:
        return HttpResponse('''<script>alert('Invalid Card Details');window.location="/login/"</script>''')
    
    data2.amount = data2.amount - float(request.POST.get('amount'))
    data2.save()
    lo= login()
    lo.email = var.email
    lo.password = var.phone
    lo.category = 'pending'
    lo.save()
    
    return HttpResponse('''<script>alert('Payment Successfull');window.location="/login/"</script>''')
    



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


from datetime import datetime
def option1(request,opid,qid):
    data = eligibility.objects.get(question_id=qid)
    
    if 'test1_id' not in request.session:
        
        print(data.option1)
        print(data.answer)
        if data.option1==data.answer:
            
                        data2=Result()
                        data2.STUDENT_id=request.session['Student']
                        data2.impression=1
                        data2.status="active"
                        data2.date=datetime.now().strftime ("%Y-%m-%d")
                        data2.time= datetime.now().strftime('%H:%M:%S')
                        data2.save()
                        data3=Result.objects.last()
                        print(data3.test_id)
                        
                        request.session['test1_id']=data3.test_id
    else:
        
        if data.option1==data.answer:
                    print(request.session['test1_id'] )
                    result_id=request.session['test1_id'] 
                    
                    data2=Result.objects.get(test_id=result_id)
                    data2.impression=int(data2.impression)+1
                    
                    data2.save()               
            
    data.status="Attended"
    data.save()
    
    data=eligibility.objects.filter(status="Not Attended")
    return render(request,"Admin/attendtest.html",{'data':data})

from datetime import datetime
def option2(request,opid,qid):
    data = eligibility.objects.get(question_id=qid)
    if 'test1_id' not in request.session:
        if data.option2==data.answer:
            
                        data2=Result()
                        
                        data2.STUDENT_id=request.session['Student']
                        data2.impression=1
                        data2.status="active"
                        data2.date=datetime.now().strftime ("%Y-%m-%d")
                        data2.time= datetime.now().strftime('%H:%M:%S')
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


from datetime import datetime
def option3(request,opid,qid):
    data = eligibility.objects.get(question_id=qid)
    if 'test1_id' not in request.session:
        if data.option3==data.answer:
            
                        data2=Result()
                        
                        data2.STUDENT_id=request.session['Student']
                        data2.impression=1
                        data2.status="active"
                        data2.date=datetime.now().strftime ("%Y-%m-%d")
                        data2.time= datetime.now().strftime('%H:%M:%S')
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

from datetime import datetime
def option4(request,opid,qid):
    data = eligibility.objects.get(question_id=qid)
    if 'test1_id' not in request.session:
        if data.option4==data.answer:
            
                        data2=Result()
                        
                        data2.STUDENT_id=request.session['Student']
                        data2.impression=1
                        data2.status="active"
                        data2.date=datetime.now().strftime ("%Y-%m-%d")
                        data2.time= datetime.now().strftime('%H:%M:%S')
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
            var = student.objects.get(student_id=request.session['Student'])
            var.delete()
            return HttpResponse('''<script>alert('Sorry!! You are not eligible to join the course as you have not secured the minimum mark');window.location="/login/"</script>''')
            
            
        
def eligible(request):
    data = Result.objects.get(STUDENT_id=request.session['Student'])
    return render(request,"eligible.html",{'data':data})

def not_eligible(request):
    return render(request,"not_eligible.html") 

def eligibility_test(request):
    data = eligibility.objects.all()
    return render(request, 'eligibility_test.html', {'data': data})



## ---------- Admin -----------


def admin_home(request):
    if 'admin' not in request.session:
        return render(request, 'login.html')
    else:
        return render(request, 'Admin/admin_home.html')

def admin_logout(request):
    del request.session['admin']
    return redirect('/login/')

def view_std_req(request):
    data = student.objects.filter(status='pending')
    return render(request, 'Admin/view_student_req.html', {'data': data})

def approve_student(request,id):
    data = student.objects.get(student_id=id)
    data.status = 'approved'
    data2=login.objects.get(email=data.email)
    data2.category='Student'
    data.save()
    data2.save()
    return redirect('/view_std_req/')

def reject_student(request,id):
    data = student.objects.get(student_id=id)
    data.status = 'rejected'
    data2=login.objects.get(email=data.email)
    data2.category='rejected'
    data2.save()
    data.save()
    var = student.objects.get(student_id=id)
    var.delete()
    vae = login.objects.get(email=data.email)
    vae.delete()
    return redirect('/view_std_req/')
    
def view_approved_student(request):
    data = student.objects.filter(status='approved')
    return render(request, 'Admin/view_approved_std.html', {'data': data})


def add_course(request):
    if 'admin' not in request.session:
        return render(request, 'login.html')
    else:
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
    if 'admin' not in request.session:
        return render(request, 'login.html')
    else:
        if request.method == 'POST':
            data = course()
            data.course_id = request.POST.get('course_id')
            data.image = request.POST.get('image')
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
    if 'admin' not in request.session:
        return render(request, 'login.html')
    else:
        data = course.objects.all()
        course_subjects = []
        for c in data:
            subjects = Subject.objects.filter(course=c)
            subject_names = [subject.name for subject in subjects]
            course_subjects.append((c, subject_names))
        return render(request, 'Admin/view_course.html', {'course_subjects': course_subjects})

def getresult(request):
    course_id=request.GET.get('course_id')
    data1 = batch.objects.filter(course_id_id=course_id)
    return JsonResponse(list(data1),safe=False)

    

def edit_course(request,id):
    if 'admin' not in request.session:
        return render(request, 'login.html')
    else:
        data = course.objects.get(course_id=id)
        return render(request, 'Admin/edit_course.html', {'data': data})

def edit_course_post(request):
    if 'admin' not in request.session:
        return render(request, 'login.html')
    else:
        id = request.POST.get('course_id')
        data = course.objects.get(course_id=id)
        data.course_name = request.POST.get('course_name')
        data.description = request.POST.get('description')
        data.course_duration = request.POST.get('course_duration')
        data.no_of_installments = request.POST.get('no_of_installments')
        data.save()
        return redirect('/view_course/')

def delete_course(request,id):
    if 'admin' not in request.session:
        return render(request, 'login.html')
    else:
        data = course.objects.get(course_id=id)
        data.delete()
        return redirect('/view_course/')

def add_branch(request):
    if 'admin' not in request.session:
        return render(request, 'login.html')
    else:
        return render(request, 'Admin/add_branch.html')

def add_branch_post(request):
    if 'admin' not in request.session:
        return render(request, 'login.html')
    else:
        data = branch()
        data.branch_id = request.POST.get('branch_id')
        data.branch_image = request.FILES['branch_image']
        data.branch_name = request.POST.get('branch_name')
        data.location = request.POST.get('location')
        data.email = request.POST.get('email')
        data.phone = request.POST.get('phone')
        data.save()
        return render(request, 'Admin/add_branch.html')

def view_branch(request):
    if 'admin' not in request.session:
        return render(request, 'login.html')
    else:
        data = branch.objects.all()
        return render(request, 'Admin/view_branch.html', {'data': data})

def view_branch2(request,id):
    if 'admin' not in request.session:
        return render(request, 'login.html')
    else:
        data = branch.objects.get(branch_id=id)
        return render(request, 'Admin/view_branch2.html', {'data': data})

def edit_branch(request,id):
    if 'admin' not in request.session:
        return render(request, 'login.html')
    else:
        data = branch.objects.get(branch_id=id)
        return render(request, 'Admin/edit_branch.html', {'data': data})

def edit_branch_post(request):
    if 'admin' not in request.session:
        return render(request, 'login.html')
    else:
        id = request.POST.get('branch_id')
        data = branch.objects.get(branch_id=id)
        data.branch_name = request.POST.get('branch_name')
        data.location = request.POST.get('location')
        data.email = request.POST.get('email')
        data.phone = request.POST.get('phone')
        data.save()
        return redirect('/view_branch/')

def delete_branch(request,id):
    if 'admin' not in request.session:
        return render(request, 'login.html')
    else:
        data = branch.objects.get(branch_id=id)
        data.delete()
        return redirect('/view_branch/')

def add_staff(request):
    if 'admin' not in request.session:
        return render(request, 'login.html')
    else:
        data=branch.objects.all()
        data2 = Subject.objects.all()
        return render(request, 'Admin/add_staff.html',{'data':data, 'data2':data2})

def add_staff_post(request):
    data = staff()
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
    data.subject = request.POST.get('subject')
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
    data2 = Subject.objects.all()
    return render(request, 'Admin/edit_staff.html', {'data': data, 'data2': data2})

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

def send_reply(request,id):
    data = complaint.objects.get(complaint_id=id)
    return render(request, 'Admin/send_reply.html', {'data': data})

def send_reply_post(request):
    did = request.POST.get('complaint_id')
    data = complaint.objects.get(complaint_id=did)
    data.reply = request.POST.get('reply')
    data.status = 'replied'
    data.save()
    return redirect('/view_complaint/')
     

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

def view_enquiry(request):
    data = enquiry.objects.all()
    return render(request, 'Admin/view_enquiry.html', {'data': data})

def mark_as_replied(request,id):
    data = enquiry.objects.get(enquiry_id=id)
    data.status = 'replied'
    data.save()
    return redirect('/view_enquiry/')

def fee_report(request):
    data = student_fee_payment.objects.all()
    paid = student_fee_payment.objects.filter(status='paid')
    total_paid = sum([p.paid_amount for p in paid])
    unpaid = student_fee_payment.objects.filter(status='')
    total_unpaid = sum([p.paid_amount for p in unpaid])
    print(total_paid)
    print(total_unpaid)
    return render(request, 'Admin/fee_report.html', {'data': data, 'total_paid': total_paid, 'total_unpaid': total_unpaid})


# ------BRANCH--------

def branch_home(request):
    return render(request,'Branch/branch_home.html')

def branch_logout(request):
    del request.session['Branch Staff']
    return render(request, 'login.html')



def view_branch_student(request):
    val = request.session['Branch Staff']
    data = staff.objects.get(email=val)
    data1 = student.objects.filter(branch_id=data.branch_id)
    return render(request, 'Branch/view_student.html', {'data': data1})

def view_student2(request,id):
    data = student.objects.get(student_id=id)
    return render(request, 'Branch/view_student2.html', {'data': data})   

def branch_profile(request):
    branch_staff = staff.objects.get(email=request.session['Branch Staff'])
    branch = branch_staff.branch_id
    return render(request, 'Branch/profile.html', {'branch': branch})

def view_branch_staffs(request):
    branch_staff = staff.objects.get(email=request.session['Branch Staff'])
    data = staff.objects.filter(branch_id=branch_staff.branch_id)
    return render(request, 'Branch/view_staffs.html', {'data': data})

# def view_fees(request):
#     branch_staff = staff.objects.get(email=request.session['Branch Staff'])
#     data = student_fee_payment.objects.filter(course_id=branch_staff.branch_id)
    
#     return render(request, 'Branch/view_fees.html', {'data': data})

def view_fees(request):
    branch_staff = staff.objects.get(email=request.session['Branch Staff'])
    data = student_fee_payment.objects.filter(status='paid')
    
    return render(request, 'Branch/fee.html', {'data': data})    

# ------- Course Coordinator --------

def coordinator_home(request):
    return render(request, 'Coordinator/coordinator_home.html')

def coordinator_logout(request):
    del request.session['Course Coordinator']
    return render(request, 'login.html')

def view_cc_profile(request):
    cc = staff.objects.get(email=request.session['Course Coordinator'])
    return render(request, 'Coordinator/view_profile.html', {'cc': cc})

def add_class(request):
    data = course.objects.all()
    data1 = staff.objects.get(email=request.session['Course Coordinator']).branch_id
    data2 = staff.objects.filter(staff_type='mentor',branch_id=data1)
    return render(request, 'Coordinator/add_class.html', {'data': data, 'data2': data2})

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

# def add_student(request):
#     data3 = course.objects.all()
#     data = batch.objects.fi

#     return render(request,'Coordinator/add_student.html',{'data3':data3,'data':data})

def add_student(request):
    data = course.objects.all()
    # data1 = batch.objects.all()
    # data2 = student.objects.all()
    return render(request, 'Coordinator/add_student.html', {'data': data})
def get_batch(request):
    print("hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh")
    course_id=request.GET.get('course_id')
    data1 = batch.objects.filter(course_id_id=course_id).values('batch_id','batch_name')
    return JsonResponse(list(data1),safe=False)

def add_mock_test(request):
    data = course.objects.all()
    return render(request, 'Coordinator/add_mock_test.html', {'data': data})

def add_mock_test_post(request):
    data = mock_question()
    data.course_id_id = request.POST.get('course')
    data.question = request.POST.get('question')
    data.option1 = request.POST.get('option1')
    data.option2 = request.POST.get('option2')
    data.option3 = request.POST.get('option3')
    data.option4 = request.POST.get('option4')
    data.answer = request.POST.get('answer')
    data.level = request.POST.get('level')
    data.save()
    return render(request, 'Coordinator/add_mock_test.html')

def view_mock(request):
    data = mock_question.objects.all()
    
    unique_course =[]
    seen_course = set()
    for i in data:
        if i.course_id not in seen_course:
            seen_course.add(i.course_id)
            unique_course.append(i)
    return render(request, 'Coordinator/view_mock.html', {'data': unique_course})

def view_mock2(request,id):
    request.session['cc']=id
    data = mock_question.objects.filter(course_id_id=id)
    return render(request, 'Coordinator/view_mock2.html', {'data': data})


def filter_level(request):
    level = request.POST.get('filter_level')
    if level == 'all':
        var = mock_question.objects.filter(course_id_id=request.session['cc'])
    else:
        var = mock_question.objects.filter(level=level).filter(course_id_id=request.session['cc'])
    return render(request, 'Coordinator/view_mock2.html', {'data': var})     
    # var = mock_question.objects.filter(level=level)
    # return render(request, 'Coordinator/view_mock2.html', {'data': var})
    

# ------MENTOR--------

def mentor_home(request):
    return render(request, 'Mentor/mentor_home.html')

def mentor_logout(request):
    del request.session['Mentor']
    return render(request, 'login.html')

def view_mentor_profile(request):
    data = staff.objects.get(email=request.session['Mentor'])
    return render(request, 'Mentor/profile.html', {'data': data})

def add_timetable(request):
    data = staff.objects.get(email=request.session['Mentor']).branch_id
    data1 = staff.objects.filter(staff_type='teacher')
    data4 = staff.objects.get(email=request.session['Mentor']).staff_id
    data3 = batch.objects.get(staff_id=data4)
    
    return render(request, 'Mentor/add_timetable.html', {'data1': data1, 'data3': data3})
    
def add_timetable_post(request):
    data = timetable()
    data.batch_id_id = request.POST.get('batch')
    data.day = request.POST.get('day')
    data.period1 = request.POST.get('period_1')
    data.period2 = request.POST.get('period_2')
    data.period3 = request.POST.get('period_3')
    data.period4 = request.POST.get('period_4')
    data.period5 = request.POST.get('period_5')
    
    data.save()
    return render(request, 'Mentor/add_timetable.html')

def view_timetable(request):
    data2 = staff.objects.get(email=request.session['Mentor']).staff_id
    data3 = batch.objects.get(staff_id=data2)
    data = timetable.objects.all()
    return render(request, 'Mentor/view_timetable.html', {'data': data,'data3':data3})

def edit_timetable(request,id):
    data = timetable.objects.get(timetable_id=id)
    data1= staff.objects.get(email=request.session['Mentor']).staff_id
    data3 = batch.objects.get(staff_id=data1)
    data4 = Subject.objects.filter(course=data3.course_id)
    
    return render(request, 'Mentor/edit_timetable.html', {'data': data, 'data4': data4,})
    
def edit_timetable_post(request):
    id = request.POST.get('batch')
    data = timetable.objects.get(timetable_id=id)
    data.day = request.POST.get('day')
    data.period1 = request.POST.get('period_1')
    data.period2 = request.POST.get('period_2')
    data.period3 = request.POST.get('period_3')
    data.period4 = request.POST.get('period_4')
    data.period5 = request.POST.get('period_5')
    data.save()
    return redirect('/view_timetable/')

def delete_timetable(request,id):
    data = timetable.objects.get(timetable_id=id)
    data.delete()
    return redirect('/view_timetable/')
    
    
# ------TEACHER--------

def teacher_home(request):
    return render(request, 'Teacher/teacher_home.html')

def teacher_logout(request):
    del request.session['Teacher']
    return render(request, 'login.html')

def view_teacher_profile(request):
    data = staff.objects.get(email=request.session['Teacher'])
    return render(request, 'Teacher/profile.html', {'data': data})

def add_notes(request):
    data = staff.objects.get(email=request.session['Teacher'])
    data2 = course.objects.all()
    return render(request, 'Teacher/add_notes.html', {'data': data, 'data2': data2})

def add_notes_post(request):
    data = notes()
    data.staff_id_id = request.POST.get('staff')
    data.course_id_id = request.POST.get('course')
    data.name = request.POST.get('name')
    data.notes = request.FILES['note']
    data.date = datetime.now()
    
    data.save()
    return render(request, 'Teacher/add_notes.html')
    

def view_notes(request):
    val = request.session['Teacher']
    data = staff.objects.get(email=val)
    data1 = notes.objects.filter(staff_id=data.staff_id)
   
    return render(request, 'Teacher/view_notes.html', {'data1': data1})

def view_all_notes(request):
    data = notes.objects.all()
    return render(request, 'Teacher/view_all_notes.html', {'data': data})

def add_video(request):
    data = staff.objects.get(email=request.session['Teacher'])
    data2 = course.objects.all()
    return render(request, 'Teacher/add_video.html', {'data': data, 'data2': data2})

def add_video_post(request):
    data = videos()
    data.staff_id_id = request.POST.get('staff')
    data.course_id_id = request.POST.get('course')
    data.name = request.POST.get('name')
    data.url = request.POST.get('url')
    data.date = datetime.now()
    
    data.save()
    return render(request, 'Teacher/add_video.html')

def view_videos(request):
    val = request.session['Teacher']
    data = staff.objects.get(email=val)
    data1 = videos.objects.filter(staff_id=data.staff_id)
    return render(request, 'Teacher/view_videos.html', {'data1': data1})

def view_all_videos(request):
    data = videos.objects.all()
    return render(request, 'Teacher/view_all_videos.html', {'data': data})


# ------STUDENT--------

def student_home(request):
    data = student.objects.get(email=request.session['Student'])
    return render(request, 'Student/student_home.html', {'data': data})

def std_logout(request):
    del request.session['Student']
    return render(request, 'login.html')


def std_view_notes(request):
    val = request.session['Student']
    data = student.objects.get(email=val)
    data1 = notes.objects.filter(course_id=data.course_id)
    return render(request, 'Student/view_notes.html', {'data1': data1})

def std_view_videos(request):
    val = request.session['Student']
    data1 = student.objects.get(email=val)
    data = videos.objects.filter(course_id=data1.course_id)
    return render(request, 'Student/view_videos.html', {'data': data})

def select_level(request):
    return render(request, 'Student/select_level.html')

def select_level_post(request):
    data = request.POST.get('level')
    request.session['level']=data
    if data == 'easy':
        var = mock_question.objects.filter(level='easy')
        return render(request, 'Student/select_level1.html', {'data': var})
    elif data == 'medium':
        var = mock_question.objects.filter(level='medium')
        return render(request, 'Student/select_level1.html', {'data': var})
    elif data == 'hard':
        var = mock_question.objects.filter(level='hard')
        return render(request, 'Student/select_level1.html', {'data': var})
    else:
        return HttpResponse("<script>alert('Invalid Level');window.location='/student_home/';</script>")


def mockoption1(request,opid,qid):
    data = mock_question.objects.get(question_id=qid)
    
    if 'test1_id' not in request.session:
        
        print(data.option1)
        print(data.answer)
        if data.option1==data.answer:
            
                        data2=mockresult()
                        data2.STUDENT_id = student.objects.get(email=request.session['Student']).student_id
                        data2.impression=1
                        data2.status="active"
                        data2.date=datetime.now().strftime ("%Y-%m-%d")
                        data2.time= datetime.now().strftime('%H:%M:%S')
                        data2.save()
                        data3=mockresult.objects.last()
                        print(data3.test_id)
                        
                        request.session['test1_id']=data3.test_id
    else:
        
        if data.option1==data.answer:
                    print(request.session['test1_id'] )
                    result_id=request.session['test1_id'] 
                    
                    data2=mockresult.objects.get(test_id=result_id)
                    data2.impression=int(data2.impression)+1
                    
                    data2.save()               
            
    data.status="Attended"
    data.save()
    
    data=mock_question.objects.filter(status="Not Attended").filter(level=request.session['level'])
    return render(request,"Student/select_level1.html",{'data':data})

from datetime import datetime
def mockoption2(request,opid,qid):
    data =mock_question.objects.get(question_id=qid)
    if 'test1_id' not in request.session:
        if data.option2==data.answer:
            data2=mockresult()
                        
            data2.STUDENT_id = student.objects.get(email=request.session['Student']).student_id
            data2.impression=1
            data2.status="active"
            data2.date=datetime.now().strftime ("%Y-%m-%d")
            data2.time= datetime.now().strftime('%H:%M:%S')
            data2.save()
            data3=mockresult.objects.last()
            print(data3.test_id)
                        
            request.session['test1_id']=data3.test_id
    else:
        if data.option2==data.answer:
            result_id=request.session['test1_id']
            data2=mockresult.objects.get(test_id=result_id)
            data2.impression=int(data2.impression)+1
            data2.save()         
                    
    data.status="Attended"
    data.save()
    
    data=mock_question.objects.filter(status="Not Attended").filter(level=request.session['level'])
    return render(request,"Student/select_level1.html",{'data':data})


from datetime import datetime
def mockoption3(request,opid,qid):
    data = mock_question.objects.get(question_id=qid)
    if 'test1_id' not in request.session:
        if data.option3==data.answer:
            data2=mockresult()            
            data2.STUDENT_id= data2.STUDENT_id = student.objects.get(email=request.session['Student']).student_id
            data2.impression=1
            data2.status="active"
            data2.date=datetime.now().strftime ("%Y-%m-%d")
            data2.time= datetime.now().strftime('%H:%M:%S')
            data2.save()
            data3=mockresult.objects.last()
            print(data3.test_id)
                        
            request.session['test1_id']=data3.test_id
    else:
        if data.option3==data.answer:
            result_id=request.session['test1_id'] 
            data2=mockresult.objects.get(test_id=result_id)
            data2.impression=int(data2.impression)+1
            data2.save()                        
    data.status="Attended"
    data.save()
    
    data=mock_question.objects.filter(status="Not Attended").filter(level=request.session['level'])
    return render(request,"Student/select_level1.html",{'data':data})
from datetime import datetime
def mockoption4(request,opid,qid):
    data = mock_question.objects.get(question_id=qid)
    if 'test1_id' not in request.session:
        if data.option4==data.answer:
            data2=mockresult()
            data2.STUDENT_id= data2.STUDENT_id = student.objects.get(email=request.session['Student']).student_id
            data2.impression=1
            data2.status="active"
            data2.date=datetime.now().strftime ("%Y-%m-%d")
            data2.time= datetime.now().strftime('%H:%M:%S')
            data2.save()
            data3=mockresult.objects.last()
            print(data3.test_id)
            request.session['test1_id']=data3.test_id
            
    else:
        if data.option4==data.answer:
            print(request.session['test1_id'] )
            result_id=request.session['test1_id'] 
            data2=mockresult.objects.get(test_id=result_id)
            data2.impression=int(data2.impression)+1
            data2.save()                       
    data.status="Attended"
    data.save()
    
    data=mock_question.objects.filter(status="Not Attended").filter(level=request.session['level'])
    return render(request,"Student/select_level1.html",{'data':data})

def mockfinishexam(request):
        
        if 'test1_id' not in request.session:
            data2=mock_question.objects.all()
            for x in data2:
                x.status="Not Attended"
                x.save()
            return render(request,"Student/mockresult11.html")
        else:
            
            resultid=request.session['test1_id'] 
        
            data=mockresult.objects.get(test_id=resultid)
            data.status="completed"
            data.save()
            data2=mock_question.objects.all()
            for x in data2:
                x.status="Not Attended"
                x.save()


            
            ss=request.session['test1_id']      
            del request.session['test1_id']   
            
            print("ddddddddddddddddddddd")
            print(ss)
            data7=mockresult.objects.get(test_id=ss)
            
        
            return HttpResponse('''<script>alert('Sorry!! You are not eligible to join the course as you have not secured the minimum mark');window.location="/login/"</script>''')
            
            
        
            
                   
            
        
def send_complaint(request):
    return render(request, 'Student/send_complaint.html')

def send_complaint_post(request):
    data = complaint()
    data.complaint = request.POST.get('complaint')
    data.date = datetime.now()
    data.student_id = student.objects.get(email=request.session['Student'])
    data.branch_id = student.objects.get(email=request.session['Student']).branch_id
    data.save()
    return render(request, 'Student/send_complaint.html')

def view_std_fee(request):
    data = student.objects.get(email=request.session['Student'])
    data1 = student_fee_payment.objects.filter(student_id=data.student_id)
    return render(request, 'Student/view_std_fee.html', {'data1': data1})

def receipt(request,id):
    data = student_fee_payment.objects.get(payment_id=id)
    data1 = fee.objects.get(course_id=data.course_id_id)
    
    return render(request, 'Student/receipt.html', {'data': data, 'data1': data1})

def pay_fee(request, id):
    data = student_fee_payment.objects.get(payment_id=id)
    data.due_date = data.due_date.strftime('%Y-%m-%d')  # Format the date
    return render(request, 'Student/pay_fee.html', {'data': data})

def pay_fee_post(request):
    id = request.POST.get('payment_id')
    data = student_fee_payment.objects.get(payment_id=id)
    var = student.objects.get(email=request.session['Student'])
    data.student_id_id = var.student_id
    
    data3 = fee.objects.get(course_id_id=var.course_id_id)
    
    data2 = bank.objects.get(bank_id=1)
    if data2.card_number == request.POST.get('card_number') and data2.cvv == request.POST.get('cvv') and data2.exp_date == request.POST.get('exp_date'):
            
            if data2.amount>=float(request.POST.get('amount')):
                data.paid_amount = request.POST.get('amount')
                data.student_id = var
                data.course_id = var.course_id
                data.payment_date = datetime.now()
                data.due_date = request.POST.get('due_date')
                data.instalment_no = request.POST.get('instalment_no')
                data.status = 'paid'
                data.save()
            else:
                return HttpResponse('''<script>alert('Insufficient Balance');window.location="/student_home/"</script>''')
            
    else:
        return HttpResponse('''<script>alert('Invalid Card Details');window.location="/student_home/"</script>''')
    
    data2.amount = data2.amount - float(request.POST.get('amount'))
    data2.save()
    return HttpResponse('''<script>alert('Payment Successfull');window.location="/student_home/"</script>''')

def view_std_profile(request):
    data = student.objects.get(email=request.session['Student'])
    return render(request, 'Student/view_profile.html', {'data': data})

def student_logout(request):
    del request.session['Student']
    return render(request, 'login.html')