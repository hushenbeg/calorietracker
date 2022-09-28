from unicodedata import name
from django.shortcuts import render, redirect
from .models import Food, Consume
# Create your views here.

def index(request):

    user = request.user

    if request.method == 'POST':
        food_consumed = request.POST.get('food_consumed')
        if food_consumed:
            consume_food = Food.objects.get(name=food_consumed)
            consume = Consume(user=user, food_consumed=consume_food)
            consume.save()
            foods = Food.objects.all()

    else:


        foods = Food.objects.all()
    
    
    consumed_food = Consume.objects.filter(user=user)


    return render(request, 'caloricountapp/index.html', {'foods':foods, 'consumed_food':consumed_food})


def delete_consume(request, id):
    consumed_food = Consume.objects.get(id=id)
    if request.method == 'POST':
        consumed_food.delete()
        return redirect('/')
    
    return render(request, 'caloricountapp/delete.html',{'consumed_food':consumed_food})
