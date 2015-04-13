from django.shortcuts import render,render_to_response
from django.http import HttpResponse, Http404, HttpResponseRedirect
from mysite.books.models import Book
from django.core.mail import send_mail

# Create your views here.
def search_form(request):
    return render_to_response('search_form.html')

'''
def search(request):
    error = False
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            error = True
        elif len(q) > 20:
            error = True
        else:
            books = Book.objects.filter(title__icontains=q)
            return render_to_response('search_results.html',
            {'books':books, 'query': q})
    return render_to_response('search_form.html', {'error':error})
'''

def search(request):
    errors = [] 
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            errors.append('Enter a search term.')
        elif len(q) > 20:
            errors.append('Please enter at most 20 characters.')
        else:
            books = Book.objects.filter(title__icontains=q)
            return render_to_response('search_results.html',
            {'books':books, 'query': q})
    return render_to_response('search_form.html', {'errors':errors})


def contact(request):
    errors = []
    if request.method == 'POST':
    return render_to_response('contact_form.html', {'errors': errors})
