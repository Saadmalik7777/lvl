from django.shortcuts import render
import datetime
# Create your views here.

def home(request):
    isActive = True
    if request.method == 'POST':
        check = request.POST.get("check")
        print(check)
        if check is None: isActive = False
        else: isActive = True 
            
 
    date = datetime.datetime.now()
    name = "learncodewithdurgash"
    list_of_programs =[
        'WAP to check even or odd',
        'WAP to check prime numbers',
        'WAP to print all primry numbers from  1 to 100',
        'WAP to print pascals triangle',
    ]
    student = {
        'student_name' : "Rahul",
        'student_college' : "xyz",
        'student_city' : "lahore"
    }
    data = {
        'date' : date,
        'isActive' : isActive,
        'name' : name,
        'list_of_programs' : list_of_programs,
        'student_data' : student
    }
    return render(request ,'home.html',data)
def about(request):
    return render(request ,'about.html')
def services(request):
    return render(request ,'servicies.html')