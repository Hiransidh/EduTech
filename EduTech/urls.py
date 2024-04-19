"""
URL configuration for EduTech project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from myapp import views
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', views.login1),
    path('login_post/', views.login_post),
    path('student_reg/', views.student_reg),
    path('student_reg_post/', views.student_reg_post),
    path('eligibility_test/', views.eligibility_test),
    path('eligible/', views.eligible),
    path('not_eligible/', views.not_eligible),
    path('payment/', views.payment1),
    path('process_payment/', views.process_payment),
    path('back_to_login/', views.back_to_login),
    path('enquiry_/', views.enquiry_),
    path('enquiry_post/', views.enquiry_post),
    path('get_batch/',views.get_batch),
    
    # --------- Admin ---------
    
    path('admin_home/', views.admin_home),
    path('admin_logout/', views.admin_logout),
    path('view_enquiry/', views.view_enquiry),
    path('mark_as_replied/<int:id>', views.mark_as_replied),
    path('eligibility/', views.eligibility_view),
    path('eligibility_post/', views.eligibility_post),
    path('view_eligibility/', views.view_eligibility),
    path('add_course/', views.add_course),
    path('add_course_post/', views.add_course_post),
    path('view_course/', views.view_course),
    path('edit_course/<int:id>', views.edit_course),
    path('edit_course_post/', views.edit_course_post),
    path('delete_course/<int:id>', views.delete_course),
    path('add_branch/', views.add_branch),
    path('add_branch_post/', views.add_branch_post),
    path('view_branch/', views.view_branch),
    path('view_branch2/<int:id>', views.view_branch2),
    path('edit_branch/<int:id>', views.edit_branch),
    path('edit_branch_post/', views.edit_branch_post),
    path('delete_branch/<int:id>', views.delete_branch),
    path('add_staff/', views.add_staff),
    path('add_staff_post/', views.add_staff_post),
    path('view_staff/', views.view_staff),
    path('delete_staff/<int:id>', views.delete_staff),
    path('edit_staff/<int:id>', views.edit_staff),
    path('edit_staff_post/', views.edit_staff_post),
    path('view_complaint/', views.view_complaint),
    path('send_reply/<int:id>', views.send_reply),
    path('send_reply_post/', views.send_reply_post),
    path('add_fees/',views.add_fees),
    path('add_fees_post/',views.add_fees_post),
    path('view_fees/',views.view_fees),
    path('attendtest/',views.attendtest),
    path('option1/<str:opid>/<str:qid>',views.option1),
    path('option2/<str:opid>/<str:qid>',views.option2),
    path('option3/<str:opid>/<str:qid>',views.option3),
    path('option4/<str:opid>/<str:qid>',views.option4),
    path('finishexam/',views.finishexam),
    path('view_std_req/', views.view_std_req),
    path('approve_student/<int:id>', views.approve_student),
    path('reject_student/<int:id>', views.reject_student),
    path('view_approved_student/', views.view_approved_student),
    path('mockoption1/<str:opid>/<str:qid>',views.mockoption1),
    path('mockoption2/<str:opid>/<str:qid>',views.mockoption2),
    path('mockoption3/<str:opid>/<str:qid>',views.mockoption3),
    path('mockoption4/<str:opid>/<str:qid>',views.mockoption4),
    path('mockfinishexam/',views.mockfinishexam),
    
    #----------- Branch -----------
    
    path('branch_home/', views.branch_home),
    path('branch_logout/', views.branch_logout),
    # path('add_student/', views.add_student),
    # path('add_student_post/', views.add_student_post),
    path('view_branch_student/', views.view_branch_student),
    path('view_student2/<int:id>', views.view_student2),
    path('branch_profile/',views.branch_profile),
    path('view_branch_staff/', views.view_branch_staffs),
    path('view_fees/',views.view_fees),
    
    
    
    #----------- Course Coordinator ---------
    
    path('coordinator_home/', views.coordinator_home),
    path('coordinator_logout/', views.coordinator_logout),
    path('view_cc_profile/',views.view_cc_profile),
    path('add_class/', views.add_class),
    path('add_class_post/', views.add_class_post),
    path('view_class/', views.view_class),
    path('add_student/', views.add_student),
    path('add_mock_test/',views.add_mock_test),
    path('add_mock_test_post/',views.add_mock_test_post),
    path('view_mock/',views.view_mock),
    path('view_mock2/<int:id>',views.view_mock2),
    path('filter_level/',views.filter_level),
    
    
    #----------- Mentor ---------
    
    path('mentor_home/', views.mentor_home),
    path('mentor_logout/', views.mentor_logout),
    path('add_timetable/', views.add_timetable),
    path('add_timetable_post/', views.add_timetable_post),
    path('view_timetable/', views.view_timetable),
    path('edit_timetable/<int:id>', views.edit_timetable),
    path('edit_timetable_post/', views.edit_timetable_post),
    path('view_mentor_profile/', views.view_mentor_profile),
    path('delete_timetable/<int:id>', views.delete_timetable),
    
    
    #----------- Teacher ---------
    path('teacher_home/', views.teacher_home),
    path('teacher_logout/', views.teacher_logout),
    path('add_notes/', views.add_notes),
    path('add_notes_post/', views.add_notes_post),
    path('view_notes/', views.view_notes),
    path('view_all_notes/', views.view_all_notes),
    path('add_video/', views.add_video),
    path('add_video_post/', views.add_video_post),
    path('view_videos/', views.view_videos),
    path('view_all_videos/', views.view_all_videos),
    path('view_teacher_profile/', views.view_teacher_profile),
    
    #----------- Student ---------
    path('student_home/', views.student_home),
    path('student_logout/', views.student_logout),
    path('std_view_notes/', views.std_view_notes),
    path('std_view_videos/', views.std_view_videos),
    
    path('send_complaint/', views.send_complaint),
    path('send_complaint_post/', views.send_complaint_post),
    path('view_std_fee/', views.view_std_fee),
    path('receipt/<int:id>', views.receipt),
    path('pay_fee/<int:id>', views.pay_fee),
    path('pay_fee_post/', views.pay_fee_post),
    path('view_std_profile/', views.view_std_profile),
    path('select_level/', views.select_level),
    path('select_level_post/', views.select_level_post),
   
    
    
    
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
   