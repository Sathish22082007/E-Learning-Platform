from django.db import models

# Create your models here.
class ContactDetails(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} - {self.subject}"
class AdminProfiles(models.Model):
    adminname = models.CharField(max_length=100)
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)  # store hashed passwords if for real login
    email = models.EmailField(unique=True)
    contact = models.CharField(max_length=15)
    creationdate = models.DateTimeField(auto_now_add=True)
    updationdate = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username    
    
class StaffInstructorProfile(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    contact = models.CharField(max_length=15)
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], null=True, blank=True)
    dob = models.DateField(null=True, blank=True)
    age = models.PositiveIntegerField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    qualification = models.CharField(max_length=255, null=True, blank=True)
    expertise = models.CharField(max_length=255, null=True, blank=True)  # subjects or areas of expertise
    joining_date = models.DateField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    password = models.CharField(max_length=100)  # For production use hashed passwords

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.username})"    
    
class StudentProfile(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    contact = models.CharField(max_length=15)
    gender = models.CharField(max_length=10, choices=[('Male', 'Male'), ('Female', 'Female'), ('Other', 'Other')], null=True, blank=True)
    dob = models.DateField(null=True, blank=True)
    age = models.PositiveIntegerField(null=True, blank=True)
    qualification = models.CharField(max_length=255, null=True, blank=True)
    password = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.username})"
    

class CheckoutOrder(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    country = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=10)
    address = models.TextField()
    payment_method = models.CharField(max_length=20)
    
    # Optional payment fields
    card_number = models.CharField(max_length=20, blank=True, null=True)
    expiry = models.CharField(max_length=10, null=True, blank=True)
    cvv = models.CharField(max_length=5, blank=True, null=True)
    
    upi_id = models.CharField(max_length=100, blank=True, null=True)
    bank_name = models.CharField(max_length=100, blank=True, null=True)
    account_number = models.CharField(max_length=20, blank=True, null=True)

    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} - {self.payment_method} - {self.timestamp.strftime('%Y-%m-%d')}"


class Course(models.Model):
    CATEGORY_CHOICES = [
        ('programming', 'Programming'),
        ('design', 'Design'),
        ('business', 'Business'),
        ('marketing', 'Marketing'),
        ('other', 'Other'),
    ]

    RATING_CHOICES = [
        (1, '⭐ 1 Star'),
        (2, '⭐⭐ 2 Stars'),
        (3, '⭐⭐⭐ 3 Stars'),
        (4, '⭐⭐⭐⭐ 4 Stars'),
        (5, '⭐⭐⭐⭐⭐ 5 Stars'),
    ]

    course_name = models.CharField(max_length=255)
    course_details = models.TextField()
    course_duration = models.CharField(max_length=100)
    course_price = models.CharField(max_length=50)
    professor_name = models.CharField(max_length=255)
    course_category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    course_rating = models.IntegerField(choices=RATING_CHOICES)
    course_image = models.ImageField(upload_to='course_images/')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.course_name

class EnrolledCourse(models.Model):
    student = models.ForeignKey(StudentProfile, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    enrolled_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student.username} enrolled in {self.course.course_name}"
# models.py

class Customer(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name
