from django.shortcuts import render
from catalog.models import Book, BookInstance, Author, Genre
from django.views import generic

# Create your views here.
def index(request):
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    num_instances_available = BookInstance.objects.filter(status__exact = 'a').count()
    num_authors = Author.objects.count() # all() is implied by default
    num_genres = Genre.objects.count()
    num_genres_adventure = Book.objects.filter(genre__name = 'adventure').count()

    context = {
        'num_books': num_books,
        'num_instances': num_instances, 
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
        'num_genres': num_genres,
        'num_genres_adventure': num_genres_adventure,
    }

    return render(request, 'index.html', context=context)

class BookListView(generic.ListView):
    model = Book
    paginate_by = 10
    #context_object_name = 'my_book_list'
    #queryset = Book.objects.filter(genre__name = 'adventure')
    #template_name = 'books/my_book_list.html'

class BookDetailView(generic.DetailView):
    model = Book

class AuthorListView(generic.ListView):
    model = Author
    paginate_by = 10

class AuthorDetailView(generic.DetailView):
    model = Author