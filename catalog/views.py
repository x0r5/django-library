from django.shortcuts import render
from catalog.models import Book, BookInstance, Author

# Create your views here.
def index(request):
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    num_instances_available = BookInstance.objects.filter(status__exact = 'a').count()
    num_authors = Author.objects.count() # all() is implied by default

    context = {
        'num_books': num_books,
        'num_instances': num_instances, 
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
    }

    return render(request, 'index.html', context=context)