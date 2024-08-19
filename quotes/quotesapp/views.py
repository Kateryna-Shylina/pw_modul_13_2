from django.shortcuts import render, redirect, get_object_or_404
from .forms import TagForm, AuthorForm, QuoteForm
from .models import Tag, Authors, Qoutes


# Create your views here.
def main(request):
    authors = Authors.objects.prefetch_related('qoutes_set__tags').all()
    return render(request, 'quotesapp/index.html', {'authors': authors})

def tag(request):
    if request.method == 'POST':
        form = TagForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='quotesapp:main')
        else:
            return render(request, 'quotesapp/tag.html', {'form': form})

    return render(request, 'quotesapp/tag.html', {'form': TagForm()})


def author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='quotesapp:main')
        else:
            return render(request, 'quotesapp/author.html', {'form': form})

    return render(request, 'quotesapp/author.html', {'form': AuthorForm()})


def quote(request):
    tags = Tag.objects.all()

    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            new_quote = form.save()

            choice_tags = Tag.objects.filter(name__in=request.POST.getlist('tags'))
            for tag in choice_tags.iterator():
                new_quote.tags.add(tag)

            return redirect(to='quotesapp:main')
        else:
            return render(request, 'quotesapp/quote.html', {"tags": tags, 'form': form})

    return render(request, 'quotesapp/quote.html', {"tags": tags, 'form': QuoteForm()})


def detail(request, author_id):
    author = get_object_or_404(Authors, pk=author_id)
    quotes = Qoutes.objects.filter(author=author)
    return render(request, 'quotesapp/detail.html', {"author": author, "quotes": quotes})


