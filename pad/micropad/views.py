from django.shortcuts import render
from . import models


def editor(request, path, name, ext):
    ctx = {
        'path': path,
        'name': name,
        'extension': ext,
    }
    return render(request, 'micropad/editor.html', ctx)

def folder_list(request, path):
    ctx = {
        'path': path,
    }
    return render(request, 'micropad/folder-list.html', ctx)
