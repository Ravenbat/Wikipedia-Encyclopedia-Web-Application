from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect
import random

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
        
    })
def title(request, entryname):
    ret = util.get_entry(entryname)
    context = {
        "blog_content": ret,
        "entry_title": entryname
    }
    if ret == None:
        raise Http404
    else :
        return render(request, "encyclopedia/entry.html", context)

def create(request):
    return render(request, "encyclopedia/create.html")

def search(request):
    matchingresults = []
    query = request.POST.get('search_query')
    entries = util.list_entries()
    for entry in entries:
        if query == entry:
            return HttpResponseRedirect(entry)
            break
        elif query in entry:
            matchingresults.append(entry)
    context = {
        "search_results" : matchingresults,
        "match" : entry,
        "searchvalue" : query
    }


    return render(request, "encyclopedia/search.html", context)

def save(request):
    entryTitle = request.POST.get('PageName','')
    content = request.POST.get('content','')
    entry = util.get_entry(entryTitle)
    if entry == None:
        util.save_entry(entryTitle, content)
        return HttpResponseRedirect(entryTitle)
    else:
        raise Exception("File Already Exists.")

def random_page(request):
    entries = util.list_entries()
    selected_page = random.choice(entries)
    return title(request, selected_page)

def edit_entry(request, title):
    body = util.get_entry(title)
    context = {
        "EntryTitle": title,
        "EntryBody": body
    }
    return render(request, "encyclopedia/edit.html", context)

def update_entry(request, titlee):
    entrytitle = request.POST.get('edit_title','')
    entrycontent = request.POST.get('edit_body','')
    util.save_entry(entrytitle, entrycontent)
    return title(request,entrytitle)


