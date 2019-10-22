from django.shortcuts import render
from rest_framework.views import APIView
from django.http import HttpResponse,JsonResponse
import json
from .models import *
from .serializer import *

# Create your views here.

def home(request):
    context = {
        
    }
    return render(request,'index.html',context)

def game(request):
    context = {
        
    }
    return render(request,'game1.html',context)

def mobile(request):
    context = {
        
    }
    return render(request,'mobile.html',context)

class CardList(APIView):
    def get(self,request):
        member = Cards.objects.all()
        serializer = CardSerialiser(member, many=True)
        return JsonResponse(serializer.data,safe=False)
    def post(self):
        pass

class PlayerList(APIView):
    def get(self,request):
        member = Player.objects.all()
        serializer = PlayerSerialiser(member, many=True)
        return JsonResponse(serializer.data,safe=False)
    def post(self):
        pass

def plus1(request):
    dict = {}
    if request.is_ajax:
        add_pts = request.GET.get("val")
        cur_pts = Player.objects.filter(name="Player1")[0].points
        final_pts = int(cur_pts) + int(add_pts)
        Player.objects.filter(name="Player1").update(
            points = final_pts,
        )
        dict = {"val":add_pts}
    else:
        return HttpResponse("Something Wrong Happened.")
    return JsonResponse(json.dumps(dict),safe=False)