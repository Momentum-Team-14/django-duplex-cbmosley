from django.shortcuts import render, get_object_or_404, redirect
from .models import Snippet
from .forms import SnippetForm
from django.contrib.auth.decorators import login_required
# Create your views here.


def list_snippets(request):
    snippets = Snippet.objects.all()
    return render(request, 'snippets/snippet_home.html', {"snippets": snippets})


def snippet_detail(request, pk):
    snippet = get_object_or_404(Snippet, pk=pk)
    return render(request, "snippets/snippet_detail.html", {"snippet": snippet})


@login_required
def create_snippet(request):
    if request.method == "POST":
        form = SnippetForm(request.POST)
        if form.is_valid():
            snippet = form.save(commit=False)
            snippet.author = request.user
            snippet.save()
            return redirect('list_snippets')
    else:
        form = SnippetForm()
    return render(request, 'snippets/create_snippet.html', {'form': form})


@login_required
def snippets_edit(request, pk):
    snippet = get_object_or_404(Snippet, pk=pk)
    if request.method == "POST":
        form = SnippetForm(request.POST, instance=snippet)
        if form.is_valid():
            snippet = form.save()
            return redirect('snippet_detail', pk=snippet.pk)
    else:
        form = SnippetForm(instance=snippet)
    return render(request, 'snippets/create_snippet.html', {'form': form})


@login_required
def delete_snippet(request, pk):
    snippet = get_object_or_404(Snippet, pk=pk)
    snippet.delete()
    return redirect('list_snippets')
    # return render(request, 'snippets/snippet_home.html', {"snippet": snippet})


# for user profile
@login_required
def user_profile(request):
    snippets = Snippet.objects.filter(users=request.user) | Snippet.objects.filter(author=request.user)
    return render(request, 'snippets/user_profile.html', {"snippets": snippets})

def copy_snippet(request, pk):
    snippet = get_object_or_404(Snippet, pk=pk)
    snippet.pk=None
    snippet.author = request.user
    snippet.save()
    return redirect('snippet_detail', pk=snippet.pk)