from django.shortcuts import render, redirect
from .models import Contact
from .forms import ContactForm
#from django.contrib import messages

# Create your views here.

def listcontacts(request):
    contacts = Contact.objects.all()
    return render(request, 'contacts/listcontacts.html', {'contacts': contacts})


def addcontacts(request):
    form = ContactForm(request.POST or None)
    #if request.user.is_authenticated:
    if request.method == "POST":
        if form.is_valid():
            addcontacts = form.save()
            #messages.success(request, "Record saved!")
            return redirect('listcontacts')
    return render(request, 'contacts/addcontacts.html', {"form": form})
    #else:
        #messages.success(request, "Must be logged in!")
        #return redirect('listcontacts')


def updatecontacts(request, pk):
    #if request.user.is_authenticated:
    contact = Contact.objects.get(id=pk)
    form = ContactForm(request.POST or None, instance=contact)
    if form.is_valid():
        form.save()
        #messages.success(request, "Record updated!")
        return redirect('listcontacts')
    return render(request, 'contacts/updatecontacts.html', {"contact": contact, "form": form})       
    #else:
        #messages.success(request, "Must be logged in!")
        #return redirect('home')



def deletecontacts(request, pk):
    #if request.user.is_authenticated:
    contact = Contact.objects.get(id=pk)
    if request.method == "POST":
        contact.delete()
        #messages.success(request, "Record deleted!")
        return redirect('listcontacts')
    return render(request, 'contacts/deletecontacts.html', {'contact': contact})
    #else:
        #messages.success(request, "Must be logged in to do that!")
        #return redirect('home')
