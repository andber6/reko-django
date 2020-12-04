from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Post
from django.shortcuts import render


def home(request):
    context = {
        'posts': Post.objects.all()
    }
    return render(request, 'feed/feed.html', context)


#def feed(request):
#    """ A view to show feed """
#
#    items = items.objects.all()
#    query = None
#
#    if request.GET:
#        if 'q' in request.GET:
#            query = request.GET['q']
#            if not query:
#                messages.error(
#                    request, "You didn't enter any search criteria!")
#                return redirect(reverse(''))
#
#            queries = Q(name__icontains=query) | Q(
#                description__icontains=query)
#            feed = items.filter(queries)
#
#    context = {
#        'items': items,
#        'search_term': query,
#    }
#
#    return render(request, 'feed/feed.html', context)
