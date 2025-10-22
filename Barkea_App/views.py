from django.shortcuts import render, redirect
from .models import Reach_out
from .forms import ContactForm
from .forms import ReservationForm
from .models import Vilat
from .models import About
from .models import Footer
from django.contrib import messages
from django.core.mail import EmailMessage
from django.conf import settings

def home_view(request):
    footer= Footer.objects.first()
    vilat = Vilat.objects.all()
    return render(request, 'barkea_home.html',{'vilat': vilat, 'footer': footer})


def about_view(request):
    footer= Footer.objects.first()
    vilat = Vilat.objects.all()
    about = About.objects.first()
    return render(request, 'barkea_about.html' ,{'vilat': vilat , 'about':about, 'footer': footer})


def contact_view(request):
    footer= Footer.objects.first()
    vilat = Vilat.objects.all() 
    reach_out = Reach_out.objects.first()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact=form.save()
            
            #SEND_EMAIL
            email = EmailMessage(
                subject=f'Mesazh i ri nga: {contact.name}',
                body=f'Ju keni nje mesazh te ri nga: {contact.name} ({contact.email}):\n\n{contact.message}',
                from_email=settings.EMAIL_HOST_USER,
                to=['ralfdushkaj@gmail.com'],
                reply_to=[contact.email],
            )
            email.send(fail_silently=False)
            
            messages.success(request, 'Mesazhi juaj u dergua me sukses!')
            return redirect('contact')
        else:
            messages.error(request, 'Te gjithe fushat duhet te plotesohen!')
    else:
        form = ContactForm()
    return render(request, 'barkea_contact.html' ,{'reach_out': reach_out, 'form': form, 'vilat': vilat , 'footer': footer})


def vila_view(request, vila_slug):
    footer = Footer.objects.first()
    vila = Vilat.objects.get(slug=vila_slug)
    vilat = Vilat.objects.all()
    return render(request, 'vilat.html', {'vila': vila, 'vilat': vilat, 'footer': footer})

def events_view(request):
    footer= Footer.objects.first()
    vilat = Vilat.objects.all()

    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation=form.save()

             #SEND_EMAIL
            email = EmailMessage(
                subject=f'Reservim i ri nga: {reservation.name}',
                body=f'Ju keni nje reservim te ri nga {reservation.name} ({reservation.email}):\n\nData e rezervimit: {reservation.date}\nMesazhi: {reservation.comment}\nNumri i telefonit: {reservation.phone}',
                from_email=settings.EMAIL_HOST_USER,
                to=['ralfdushkaj@gmail.com'],
                reply_to=[reservation.email],
            ) 
            email.send(fail_silently=False)

            messages.success(request, 'Reservimi juaj u dergua me sukses!')
            return redirect('events')
        else:
            messages.error(request, 'Te gjithe fushat duhet te plotesohen!')
    else:
        form = ReservationForm()
    return render(request, 'events.html' ,{'vilat': vilat, 'footer': footer, 'form': form})



   