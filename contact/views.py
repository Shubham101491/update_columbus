from django.shortcuts import render,redirect
from columbus import settings

# Email data Import
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.contrib import messages
import email.message
import smtplib

def contacts(request):
    if request.method == 'POST':
        name = request.POST['name']
        email_user = request.POST['email']
        mssge = request.POST['message']
        subject = 'Welcome to My World'
        # message = [name, email_user, mssge]
        data_content = {"yourname": name, "user_email": email_user,"Message": mssge}
        email_content = render_to_string('contact/mail.html', data_content)

        msg = email.message.Message()
        msg['Subject'] = 'Welcome to my world'
        msg['From'] = settings.EMAIL_HOST_USER
        msg['To'] = 'shubhamupadhyay1014@gmail.com'
        password = settings.EMAIL_HOST_PASSWORD
        msg.add_header('Content-Type', 'text/html')
        msg.set_payload(email_content)
        s = smtplib.SMTP(settings.EMAIL_HOST + ':' + str(settings.EMAIL_PORT))
        s.starttls()
        s.login(msg['From'], password)
        s.sendmail(msg['From'], [msg['To']], msg.as_string())
        messages.info(request, 'Thankyou for contact us, we will reply you shortly')
       
        return redirect("http://127.0.0.1:8000/contact/contacts")
    return render(request,'contact/contact.html',{"BASE_URL": settings.Base_url})