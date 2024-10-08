from django.shortcuts import render,redirect
from django.contrib import messages
# from student.models import UploadedFile
from Login_page.models import RegisterStudent

# Create your views here.
def homePage(request):
    print("working")
    return render(request,'student\\home.html')

def search(request):
    return render(request,'student\\search.html')

def resources(request):
    return render(request,'student\\resources.html')

def group_file(request):
    return render(request,'group\\file.html')

def group_groups(request):
    return render(request,'group\\groups.html')

def code(request):
    return render(request, 'uploads\\code.html')

# Folder View Page
def document_view(request):
    return render(request, 'uploads\\document.html')

# Additional View Page
def additional_view(request):
    return render(request, 'uploads\\additional.html')

# Database View Page
def database_view(request):
    return render(request, 'uploads\\database.html')

#View Details Page
# def view_details(request):
#     return render(request, 'uploads\\view.html')

from django.shortcuts import render, redirect, get_object_or_404
from .models import CodeFile, DatabaseFile, DocumentFile, AdditionalFile
from .forms import CodeFileForm, DatabaseFileForm, DocumentFileForm, AdditionalFileForm

def upload_file(request, file_type):
    if request.method == "POST":
        form = None
        if file_type == 'code':
            form = CodeFileForm(request.POST, request.FILES)
        elif file_type == 'database':
            form = DatabaseFileForm(request.POST, request.FILES)
        elif file_type == 'document':
            form = DocumentFileForm(request.POST, request.FILES)
        elif file_type == 'additional':
            form = AdditionalFileForm(request.POST, request.FILES)
        
        if form and form.is_valid():
            form.save()
            return redirect('view_files', file_type=file_type)
    
    form = CodeFileForm() if file_type == 'code' else DatabaseFileForm() if file_type == 'database' else DocumentFileForm() if file_type == 'document' else AdditionalFileForm()
    return render(request, 'uploadss\\upload_file.html', {'form': form, 'file_type': file_type})

def view_files(request, file_type):
    file_models = {
        'code': CodeFile,
        'database': DatabaseFile,
        'document': DocumentFile,
        'additional': AdditionalFile,
    }
    files = file_models[file_type].objects.all()
    return render(request, 'uploadss\\view_files.html', {'files': files, 'file_type': file_type})

def edit_file(request, file_type, file_id):
    file_models = {
        'code': CodeFile,
        'database': DatabaseFile,
        'document': DocumentFile,
        'additional': AdditionalFile,
    }
    file_instance = get_object_or_404(file_models[file_type], id=file_id)
    form = None
    
    if request.method == "POST":
        if file_type == 'code':
            form = CodeFileForm(request.POST, request.FILES, instance=file_instance)
        elif file_type == 'database':
            form = DatabaseFileForm(request.POST, request.FILES, instance=file_instance)
        elif file_type == 'document':
            form = DocumentFileForm(request.POST, request.FILES, instance=file_instance)
        elif file_type == 'additional':
            form = AdditionalFileForm(request.POST, request.FILES, instance=file_instance)

        if form and form.is_valid():
            form.save()
            return redirect('view_files', file_type=file_type)

    form = CodeFileForm(instance=file_instance) if file_type == 'code' else DatabaseFileForm(instance=file_instance) if file_type == 'database' else DocumentFileForm(instance=file_instance) if file_type == 'document' else AdditionalFileForm(instance=file_instance)
    
    return render(request, 'uploadss\\edit_file.html', {'form': form, 'file': file_instance, 'file_type': file_type})
