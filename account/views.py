from columbus import settings
from django.shortcuts import render, redirect,HttpResponse, get_object_or_404
from django.contrib.auth.models import User, auth
from category.models import user_type, User_category
from account.forms import register
from django.contrib import messages
from account.models import user_register
import smtplib
import email.message
from django.core.mail import send_mail
from django.template.loader import render_to_string


def registerpost(request):
    form = register
    if request.method == 'POST':
        first_name = request.POST['fullname']
        email = request.POST['email']
        otp = User.objects.make_random_password(
            length=4, allowed_chars='123456789')
        # if User.objects.filter(username=email).exists():
        #     messages.info(request, 'Username already exists')
        #     return redirect("basic_app/loginregister")
        # elif User.objects.filter(email=email).exists():
        #     messages.info(request, 'Email already exists')
        #     return redirect("basic_app/loginregister")
        # else:
        print(request.POST)
        form_data = register(request.POST)
        if form_data.is_valid():
            dj_user = User.objects.create_user(first_name=first_name,
                                               username=email, email=email, password=otp)
            dj_user.save()

            data_profile = form_data.save(commit=False)
            data_profile.user = dj_user
            data_profile.otp = otp
            data_profile.save()
            form_data.save_m2m()
            messages.info(request, 'success')

        else:
            messages.info(request, form_data.errors)
        return redirect("http://127.0.0.1:8000/account/registerpost")
    else:    
        form = register()
        return render(request,"account/login-register.html",{'form':form})

def userlogin(request):
    if request.method == 'POST':
        email_user = request.POST['email']
        if User.objects.filter(username=email_user).exists():
            user = get_object_or_404(User, username=email_user)
            get_user_data = get_object_or_404(user_register, user=user)
            data_content = {"username": user.first_name,
                            "user_otp": get_user_data.otp}
            email_content = render_to_string(
                'account/email_otp.html', data_content)
            # email_content = "<h1>hello <h1>"
            msg = email.message.Message()

            msg['Subject'] = 'Welcome to my world'
            msg['From'] = settings.EMAIL_HOST_USER
            msg['To'] = email_user
            password = settings.EMAIL_HOST_PASSWORD
            msg.add_header('Content-Type', 'text/html')
            msg.set_payload(email_content)
            s = smtplib.SMTP(settings.EMAIL_HOST + ':' +
                             str(settings.EMAIL_PORT))
            s.starttls()
            s.login(msg['From'], password)
            s.sendmail(msg['From'], [msg['To']], msg.as_string())
            # messages.info(request, 'Email  exists')
            return redirect("http://127.0.0.1:8000/account/login_otp/"+get_user_data.user_code)
        else:
            messages.info(request, 'Email not exists')
            return redirect("http://127.0.0.1:8000/account/registerpost")
    else:
        return render(request, "account/login-register.html")
        
def login_otp(request, user_code):
    # print(user_code)
    user_data = None
    if user_register.objects.filter(user_code=user_code).exists():
        user_data = get_object_or_404(user_register, user_code=user_code)
    # return render(request, "basic_temp/login-otp.html")
    if request.method == 'POST':
        get_otp_in_list = request.POST.getlist('one')
        print(get_otp_in_list)
        #  changing value into string
        get_otp = "".join(get_otp_in_list)
        # print(user_data.user.email)
        print(get_otp)

        if user_register.objects.filter(user_code=user_code).filter(password=get_otp).exists():
            username = str(user_data.user.username)
            password = str(get_otp)
            user = auth.authenticate(username=username, password= password)
            if user is not None:
                auth.login(request, user)
                # user_register.objects.create(user=request.user)
                # print(user.first_name)
                # return render(request, "user/dashboard_temp/dashboard.html")
                return redirect("http://127.0.0.1:8000/dashboard/dashboard")
            else:
                messages.info(request, 'invalid credentials')
                return HttpResponse("userlogin")
            # return render(request, "web/home/dashboard.html")

        else:
            messages.info(request, 'otp is wrong')
    return render(request, "account/login-otp.html",{"user_data": user_data})
