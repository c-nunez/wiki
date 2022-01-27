from django.urls import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render
from markdown2 import Markdown
from django import forms
from . import util
import secrets


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })
    
def entry(request, entry): 
    markdowner = Markdown()
    entryPage = util.get_entry(entry)
    if entryPage is None:
        return render(request, "encyclopedia/noentry.html", {
            "entryTitle": entry
        })
    else:
        return render(request, "encyclopedia/entry.html", {
            "entry": markdowner.convert(entryPage),
            "entryTitle": entry
        })
        
def search(request):
    value = request.GET.get('q')
    if(util.get_entry(value) is not None):
        return HttpResponseRedirect(reverse("entry", kwargs= {
            'entry': value
        }))
    else:
        subStringEntries = []
        for entry in util.list_entries():
            if value.upper() in entry.upper():
                subStringEntries.append(entry)
        return render(request, "encyclopedia/index.html", {
            "entries": subStringEntries,
            "search": True,
            "value": value
        })

def new(request):
    return render(request, "encyclopedia/newpage.html")

def random(request):
    entries = util.list_entries()
    randomEntry = secrets.choice(entries)
    return HttpResponseRedirect(reverse("entry", kwargs={
        'entry': randomEntry
        }))