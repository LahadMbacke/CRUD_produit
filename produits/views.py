from django.shortcuts import redirect, render
from produits.models import Produit
from produits import form  
from produits.form import ProdForm  

# Create your views here.

#Fonction pour Enregistrer les produits
def prod(request):  
   if request.method =="POST":
       form = ProdForm(request.POST)
       if form.is_valid():
           form.save()
           return redirect("/lister")
   else:
       form = ProdForm()
       return render(request,"index.html",{'form':form})


#Fonction pour lister les produits
def lister(request):
    produits = Produit.objects.all()
    return render(request,"listPro.html",{"produits":produits})


#Fonction pour modifier les produits
def modif(request, id):  
    produit = Produit.objects.get(id=id)  
    return render(request,'modif.html', {'produit':produit})


#Fonction pour persister la modification d'un produits
def update(request, id):  
    produit = Produit.objects.get(id=id)  
    form = ProdForm(request.POST, instance = produit)  
    if form.is_valid():  
        form.save()  
        return redirect("/lister")  
    return render(request, 'modif.html', {'produit': produit})  


def delete(request, id):  
    produit = Produit.objects.get(id=id)  
    produit.delete()  
    return redirect("/lister")  

             