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
    path('logout/', views.logout),
    path('student_reg/', views.student_reg),
    
    # --------- Admin ---------
    
    path('admin_home/', views.admin_home),
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
    path('add_fees/',views.add_fees),
    path('add_fees_post/',views.add_fees_post),
    path('view_fees/',views.view_fees),
    
    #----------- Branch -----------
    
    path('branch_home/', views.branch_home),
    path('add_student/', views.add_student),
    path('add_student_post/', views.add_student_post),
    path('view_student/', views.view_student),
    path('view_student2/<int:id>', views.view_student2),
    path('view_staff1/', views.view_staff1),
    path('view_fee1/', views.view_fee1),
    path('view_fee2/<int:id>', views.view_fee2),
    
    #----------- Course Coordinator ---------
    
    path('coordinator_home/', views.coordinator_home),
    path('add_class/', views.add_class),
    path('add_class_post/', views.add_class_post),
    path('view_class/', views.view_class),
    
    #----------- Mentor ---------
    
    path('mentor_home/', views.mentor_home),
    path('add_timetable/', views.add_timetable),
    path('add_timetable_post/', views.add_timetable_post),
    path('view_timetable/', views.view_timetable),
    
    
    #----------- Teacher ---------
    path('teacher_home/', views.teacher_home),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
   