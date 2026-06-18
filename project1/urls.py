"""
URL configuration for project1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from myapp import views
from django.conf import settings
from django.conf.urls.static import static




urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('about',views.about),
    path('courses',views.courses),
    path('contact',views.contact),
    path('login',views.login),
    path('HTML',views.HTML),
    path('admindashboard',views.admindashboard),
    path('admin',views.admin),
    path('register',views.register),
    path('adminlogout',views.adminlogout),
    path('instructordashboard',views.instructordashboard),
    path('studentdashboard',views.studentdashboard),
    path('css',views.css),
    path('test/', views.test_template),
    path('form',views.form),

    path('python',views.python),
    path('add-customer/', views.add_customer, name='add_customer'),
    path('view-customers/', views.view_customers, name='view_customers'),
    path('success/', views.success, name='success'),
    path('cart/<int:id>', views.cart, name="cart"),
    path('checkout/<int:course_id>/', views.checkout, name='checkout'),
    path('deleteprofessor/<int:id>',views.deleteprofessor),
    path('editprofessor/<int:id>/',views.editprofessor),
    path('updateprofessor/<int:id>/', views.updateprofessor, name='updateprofessor'),
    path('editstudent/<int:id>',views.editstudent),
    path('editstudent/update_student/<int:id>',views.update_student),
    path('deletestudent/<int:id>',views.deletestudent),
    path('getstarted/<int:id>',views.getstarted),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


