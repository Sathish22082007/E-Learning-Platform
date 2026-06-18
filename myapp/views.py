from django.shortcuts import render,redirect
from .models import ContactDetails
from .models import AdminProfiles
from .models import StaffInstructorProfile
from datetime import date
from .models import StudentProfile
from .models import Course
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from .models import CheckoutOrder
from .models import EnrolledCourse
from .forms import CustomerForm
from .models import Customer


# Create your views here.
def index(request):
    courses = Course.objects.all()
    return render(request,"index.html",{'courses':courses})
def about(request):
    return render(request,"about.html")

def courses(request):
    courses = Course.objects.all()
    return render(request,"courses.html",{'courses':courses})
def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        contact=ContactDetails.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message
        )
        contact.save()

    return render(request,"contact.html")
def login(request):
    
    return render(request,"login.html")
def HTML(request):
    return render(request,"HTML.html")
def admindashboard(request):
    admin_id = request.session.get('admin_id')
    if not admin_id:
        return redirect('/admin')  # Force login if session not found

    try:
        admin = AdminProfiles.objects.get(id=admin_id)
    except AdminProfiles.DoesNotExist:
        return redirect('/admin')  # Invalid session, redirect to login

    if request.method == 'POST':
        course_name = request.POST.get('course_name')
        course_details = request.POST.get('course_details')
        course_duration = request.POST.get('course_duration')
        course_price = request.POST.get('course_price')
        professor_name = request.POST.get('professor_name')
        course_category = request.POST.get('course_category')
        course_rating = request.POST.get('course_rating')
        course_image = request.FILES.get('course_image')

        Course.objects.create(
            course_name=course_name,
            course_details=course_details,
            course_duration=course_duration,
            course_price=course_price,
            professor_name=professor_name,
            course_category=course_category,
            course_rating=int(course_rating),
            course_image=course_image,
        )

       
        return redirect('/admindashboard')  # Stay on same page after course is added

    staff = StaffInstructorProfile.objects.all()
    student = StudentProfile.objects.all()
    courses = Course.objects.all()

    return render(request, "admindashboard.html", {
        'admin': admin,
        'staff': staff,
        'student': student,
        'courses': courses
    })


def admin(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Admin check
        if AdminProfiles.objects.filter(email=email, password=password).exists():
            admin_user = AdminProfiles.objects.get(email=email)
            request.session['admin_id'] = admin_user.id
            request.session['username'] = admin_user.adminname
            request.session['loggedin'] = True
            request.session['dashboard'] = '/admindashboard'
            return redirect("/admindashboard")

        # Instructor check
        elif StaffInstructorProfile.objects.filter(email=email, password=password).exists():
            instructor = StaffInstructorProfile.objects.get(email=email)
            request.session['instructor_id'] = instructor.id
            request.session['username'] = instructor.username
            request.session['loggedin'] = True
            request.session['dashboard'] = '/instructordashboard'
            return redirect("/instructordashboard")

        # Student check
        elif StudentProfile.objects.filter(email=email, password=password).exists():
            student = StudentProfile.objects.get(email=email)
            request.session['student_id'] = student.id
            request.session['username'] = student.username
            request.session['loggedin'] = True
            request.session['dashboard'] = '/studentdashboard'
            return redirect("/studentdashboard")

        else:
            return render(request, "admin.html", {'error': 'Invalid credentials'})

    return render(request, "admin.html")

def register(request):
    if request.method == 'POST':
        role = request.POST.get('role')  # get from hidden input

        # Common fields
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        contact = request.POST.get('contact')
        gender = request.POST.get('gender')
        dob = request.POST.get('dob')
        qualification = request.POST.get('qualification')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        age = calculate_age(dob)

        if role == "instructor":
            expertise = request.POST.get('expertise')
            StaffInstructorProfile.objects.create(
                first_name=first_name, last_name=last_name, username=username,
                email=email, contact=contact, gender=gender, dob=dob,
                qualification=qualification, expertise=expertise, password=password, age=age
            )
        elif role == "student":
            StudentProfile.objects.create(
                first_name=first_name, last_name=last_name, username=username,
                email=email, contact=contact, gender=gender, dob=dob,
                qualification=qualification, password=password, age=age
            )
        return redirect("/admin")

    return render(request, "register.html")
        
def adminlogout(request):
    request.session.flush()
    return redirect('/admin')

def instructordashboard(request):
    student=StudentProfile.objects.all()
    instructor_id = request.session.get('instructor_id')
    if instructor_id:
        instructor = StaffInstructorProfile.objects.get(id=instructor_id)
        return render(request, "instructordashboard.html", {'instructor': instructor,'student':student})
    else:
        return redirect('/admin')  # for
    return render(request,"instructordashboard.html")
def studentdashboard(request):
    student_id = request.session.get('student_id')
    if student_id:
        student = StudentProfile.objects.get(id=student_id)
        enrolled_courses = EnrolledCourse.objects.filter(student=student).select_related('course')
        return render(request, "studentdashboard.html", {
            'student': student,
            'enrolled_courses': enrolled_courses
        })
    else:
        return redirect('/admin')

    return render(request,"studentdashboard.html")
def calculate_age(dob_str):
    try:
        dob = date.fromisoformat(dob_str)
        today = date.today()
        return today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
    except Exception:
        return None
def getstarted(request,id):
    courses = Course.objects.get(id=id)


    return render(request,"getstarted.html",{'course':courses})
def css(request):
    return render(request,"css.html")   
def python(request):
    return render(request,"python.html")
@csrf_exempt
def checkout(request, course_id):
    course = get_object_or_404(Course, id=course_id)

    if request.method == 'POST':
        name = request.POST.get('full_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        country = request.POST.get('country')
        state = request.POST.get('state')
        zip_code = request.POST.get('zip_code')
        address = request.POST.get('address')
        payment_method = request.POST.get('payment_method')

        card_number = expiry = cvv = upi_id = bank_name = account_number = None

        if payment_method == 'card':
            card_number = request.POST.get('card_number')
            expiry = request.POST.get('expiry')
            cvv = request.POST.get('cvv')
        elif payment_method == 'upi':
            upi_id = request.POST.get('upi_id')
        elif payment_method == 'netbanking':
            bank_name = request.POST.get('bank_name')
            account_number = request.POST.get('account_number')

        # Save checkout info
        CheckoutOrder.objects.create(
            full_name=name,
            email=email,
            phone=phone,
            country=country,
            state=state,
            zip_code=zip_code,
            address=address,
            payment_method=payment_method,
            card_number=card_number,
            expiry=expiry,
            cvv=cvv,
            upi_id=upi_id,
            bank_name=bank_name,
            account_number=account_number,
            # Optionally: store course reference
        )

        # Save enrollment if student is logged in
        student_id = request.session.get('student_id')
        if student_id:
            student = StudentProfile.objects.get(id=student_id)
            EnrolledCourse.objects.create(student=student, course=course)

        return redirect('success')

    return render(request, 'checkout.html', {'course': course})


def success(request):
    return render(request, 'success.html')
from django.shortcuts import redirect, render

def cart(request,id):
    if not request.session.get('loggedin'):
        return redirect('/admin')  # Redirect to login if not logged in

    # Your cart logic here
    course = Course.objects.get(id=id)
    return render(request, 'cart.html', {'course': course})

def editstudent(request,id):
    student=StudentProfile.objects.get(id=id)
    return render(request,"editstudent.html",{'student':student})
def editprofessor(request, id):
    staff = get_object_or_404(StaffInstructorProfile, id=id)
    return render(request, "editprofessor.html", {'staff': staff})
def deleteprofessor(request,id):
    staff = StaffInstructorProfile.objects.get(id=id)
    staff.delete()
    return redirect("/admindashboard")
def deletestudent(request,id):
    student=StudentProfile.objects.get(id=id)
    student.delete()
    return redirect("/admindashboard")
def update_student(request, id):
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    username = request.POST['username']
    email = request.POST['email']
    contact = request.POST['contact']
    gender = request.POST['gender']
    dob = request.POST['dob']
    age = request.POST['age']
    qualification = request.POST['qualification']
    student = StudentProfile.objects.get(id=id)
    student.first_name=first_name
    student.last_name=last_name
    student.username=username
    student.email=email
    student.contact=contact
    student.age=age
    student.dob=dob
    student.qualification=qualification
    student.gender=gender


    student.save()
    return redirect('/admindashboard')  # redirect after saving
    return render(request, 'update_student.html', {'student': student})

def updateprofessor(request, id):
    
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        contact = request.POST['contact']
        gender = request.POST['gender']
        dob = request.POST['dob']
        age = request.POST['age']
        address = request.POST['address']
        qualification = request.POST['qualification']
        expertise = request.POST['expertise']
        password = request.POST['password']  # Should hash in production
        staff = StaffInstructorProfile.objects.get(id=id)
        staff.first_name=first_name
        staff.last_name=last_name
        staff.username=username
        staff.email=email
        staff.contact=contact
        staff.age=age
        staff.dob=dob
        staff.qualification=qualification
        staff.gender=gender
        staff.address=address
        staff.expertise=expertise
        staff.password=password
        staff.save()
        return redirect('/admindashboard')

    return render(request, 'editprofessor.html', {'staff': staff})
def form(request):
    return render(request,"form.html")
def add_customer(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_customers')  # Make sure this URL exists
    else:
        form = CustomerForm()
    return render(request, 'add_customer.html', {'form': form})

def view_customers(request):
    month = request.GET.get('month')
    if month:
        customers = Customer.objects.filter(date_added__month=month)
    else:
        customers = Customer.objects.all()
    return render(request, 'view_customers.html', {'customers': customers})
def test_template(request):
    return render(request, 'test.html')
