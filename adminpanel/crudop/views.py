from django.shortcuts import render
from . import myforms
from django.core.files.storage import FileSystemStorage
# importing database modules
from .dbmodels.product import Product
from .dbmodels.productdao import ProductDAO

# Create your views here.
def upload(request):
    if request.method=="GET":
        django_form=myforms.UploadForm()
        return render(request, 'upload.html', {'f':django_form})
    elif request.method=="POST":
        django_form=myforms.UploadForm(request.POST, request.FILES)
        if django_form.is_valid():
            #receiving the cleaned data
            name=django_form.cleaned_data['name']
            writer=django_form.cleaned_data['writer']
            genre=django_form.cleaned_data['genre']
            rate=django_form.cleaned_data['rate']
            review=django_form.cleaned_data['review']
            upldate=django_form.cleaned_data['upldate']
            image=django_form.cleaned_data['image']

            #uploading the file to media folder
            fs=FileSystemStorage()
            filename=fs.save(image.name,image)
            imageurl=fs.url(filename)

            p=Product(-1,name,writer,genre,rate,review,upldate,imageurl)
            dao=ProductDAO()
            try:
                dao.upload(p)

                #reinitializing django form
                django_form=myforms.UploadForm()
                return render(request, 'upload.html', {'f':django_form,'success':True})
            except:
                return render(request, 'upload.html', {'f':django_form,'success':False})
        else:
            return render(request, 'upload.html', {'f':django_form})

def show(request):
    dao=ProductDAO()
    prodlist=dao.showall() #list of product objects
    return render(request, 'show.html', {'data':prodlist})

def update(request, pid):
    if request.method=='GET':
        dao=ProductDAO()
        p=dao.findprod(pid)

        django_form=myforms.UpdateForm(initial={'pid':p.getId(), 'name':p.getName(), 'writer':p.getWriter(), 'genre':p.getGenre(), 'rate':p.getRate(),'review':p.getReview(), 'upldate':p.getUpldate()})
        return render(request, 'update.html',{'f':django_form})

    elif request.method=='POST':
        django_form=myforms.UpdateForm(request.POST)
        if django_form.is_valid():
            id=django_form.cleaned_data['pid']
            name=django_form.cleaned_data['name']
            writer=django_form.cleaned_data['writer']
            genre=django_form.cleaned_data['genre']
            rate=django_form.cleaned_data['rate']
            review=django_form.cleaned_data['review']
            upldate=django_form.cleaned_data['upldate']

            p=Product(id, name, writer, genre, rate, review, upldate, '')
            dao=ProductDAO()
            try:
                dao.update(p)
                return render(request,'update.html',{'f':django_form,'success':True})
            except:
                return render(request,'update.html',{'f':django_form,'success':False})
        else:
            return render(request, 'update.html',{'f':django_form})

def delete(request):
    if request.method=='POST':
        pid=request.POST['pid']
        dao=ProductDAO()
        try:
            p=dao.delete(pid)
            prodlist=dao.showall() #list of product objects
            return render(request, 'show.html', {'data':prodlist,'success':True})
        except:
            prodlist=dao.showall() #list of product objects
            return render(request,'show.html',{'data':prodlist,'success':False})
