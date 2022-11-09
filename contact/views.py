from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail

# Create your views here.
 
def index(request):
    if request.method == "POST":
        subject = request.POST.get('subject')
        email = request.POST.get('email')
        msg = request.POST.get('msg')
        print(subject, email, msg)

        return HttpResponse("Email will be sent")
    send_mail(
            subject,anyangnancy@gmail.com,msg
            [email]
        )
                  
    return render(request, 'contact/form.html')

