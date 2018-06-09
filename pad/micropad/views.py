from django.shortcuts import render
from .models import File, Folder
from .forms import FileForm

language = {
    ".txt": "plaintext",
    ".ts": "type",
    ".js": "java",
    ".json": "json",
    ".bat": "bat",
    ".cs": "coffee",
    ".c": "c",
    ".cpp": "cpp",
    ".csp": "csp",
    ".css": "css",
    ".fs": "fsharp",
    ".go": "go",
    ".handlebars": "handlebars",
    ".html": "html",
    ".htm": "html",
    ".ini": "ini",
    ".java": "java",
    ".less": "less",
    ".lua": "lua",
    ".md": "markdown",
    ".msdax": "msdax",
    ".mysql": "mysql",
    ".objc": "objective-c",
    ".pgsql": "pgsql",
    ".php": "php",
    ".postiats": "postiats",
    ".powershell": "powershell",
    ".pug": "pug",
    ".py": "python",
    ".r": "r",
    ".razor": "razor",
    ".redis": "redis",
    ".redshift": "redshift",
    ".ruby": "ruby",
    ".rust": "rust",
    ".sb": "sb",
    ".scss": "scss",
    ".sol": "sol",
    ".sql": "sql",
    ".st": "st",
    ".swift": "swift",
    ".vb": "vb",
    ".xml": "xml",
    ".yaml": "yaml",
    ".yml": "yaml"
}


def get_language(ext):
    return language[ext]


def folder_list(request, path):
    ctx = {
        'path': path,
    }
    return render(request, 'micropad/folder-list.html', ctx)


def editor(request, path, name, ext):
    last_father = ""

    try:

        file = File.objects.get(name=name)
    except File.DoesNotExist:
        file = {'text': "insert your code"}



    ctx = {
        'language': get_language(ext),
        'file': file
    }

    return render(request, 'micropad/editor.html', ctx)


def postForm(request, path, name, ext):

    if path is not None:
        folders = path.split('/')
        print(folders)

        for idx, folder in enumerate(folders):
            try:
                get_folder = Folder.objects.get(name=folder)
            except Folder.DoesNotExist:
                if idx == 0:
                    get_folder = Folder.objects.create(name=folder)
                else:
                    get_folder = Folder.objects.create(name=folder, folder=Folder.objects.get(name=last_father))

            last_father = folder

    try:
        archive = File.objects.get(name=name)
    except File.DoesNotExist:
        archive = File.objects.create(text=request.POST['text'], name=name, uri=path+name+ext, folder=Folder.objects.get(name=last_father))

    ctx = {
        'language': get_language(ext),
        'file': archive
    }

    return render(request, 'micropad/editor.html', ctx)
