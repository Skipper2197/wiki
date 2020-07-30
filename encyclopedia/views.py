from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse 

import markdown2

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def page(request, page):
    if util.get_entry(page):
        content = markdown2.markdown(util.get_entry(page))
    else:
        content = None

    return render(request, "encyclopedia/page.html", {
        "page": page,
        "content": content
    })

def edit(request, page):
    page_content = util.get_entry(page)
    if request.method == "GET":
        return render(request, "encyclopedia/edit.html", {
            "page": page,
            "content" : page_content
        })
    new_content = request.POST["new_content"]
    util.save_entry(page, new_content)
    return HttpResponseRedirect(reverse("page", kwargs={
        "page": page
    }))

