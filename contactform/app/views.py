from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings


def index(request):

   if request.method == 'POST':

      #message = request.POST['message']
      d2 = request.POST['date2']
      d1 = request.POST['date1']

      message='Thanks for choosing us.!!'+'\n'+'Your checkin is on '+d2+'\n''and your checkout is on '+d1+'\n'+'Happy Holiday'
      email=request.POST['email']


      send_mail('Dream House-live in luxury',
      message,
       settings.EMAIL_HOST_USER,
       [email],
       fail_silently=False)
   return render(request, 'app/index.html')