from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.http import Http404
from django.core.mail import EmailMessage
from django.shortcuts import render, redirect, get_object_or_404
from django.views import View

from books_app.models import Book

# Create your views here.
class Index(View):
    template_name = 'books_app/index.html'

    def get(self, request, *args, **kwargs):
        send_mail(
                "New user registered!",
                "A new user, '%s' just registered on your site. Check the admin dashboard for more info" % request.user.username,
                from_email='phenom.h.acks21@gmail.com',
                recipient_list=[
                    'enoch.isaac22@gmail.com'
                ]
            )

        # I added this
        # email_message = EmailMessage(subject="subject", body="message",from_email="from_email", to=['oscarblessed04@gmail.com'])
        # email_message.send()
        # this worked for sending email
        
        books = Book.objects.filter(plan="level_4")

        context = {
            'books': books
        }
        return render(request, self.template_name, context)

class ReadBook(View):
    model = Book
    template_name = 'books_app/read_book.html'

    def get(self, request, pk, *args, **kwargs):
        book = get_object_or_404(Book, pk=pk)

        context = {
            'book': book
        }
        return render(request, self.template_name, context)

index = Index.as_view()
read_book = ReadBook.as_view()