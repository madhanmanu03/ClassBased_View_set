from django.shortcuts import render
from rest_framework.viewsets import ViewSet
from app.models import *
from rest_framework.response import Response
from app.serializers import *

# Create your views here.

class Product_curd(ViewSet):
    def list(self,request):
        LPO=Product.objects.all()
        JLPO=jasonserializers(LPO,many=True)
        return Response(JLPO.data)

    def retrieve(self,request,pk):
        RLO=Product.objects.get(pk=pk)
        JPOD=jasonserializers(RLO)
        return Response(JPOD.data)

    def create(self,request):
        JD=request.data
        POD=jasonserializers(data=JD)
        if POD.is_valid():
            POD.save()
            return Response({"inserted":"DATA INSERTED"})
        else:
            return Response({"notinserted":"NOT INSERTED"})

    def update(self,request,pk):
        PO=Product.objects.get(pk=pk)
        JD=request.data
        PDO=ProductModelSerializer(PO,data=JD)
        if PDO.is_valid():
            PDO.save()
            return Response({'Update':'Data is Updated'})
        else:
            return Response({'error':'Not ABle To update'})

    def partial_update(self,request,pk):
        PO=Product.objects.get(pk=pk)
        JD=request.data
        PDO=ProductModelSerializer(PO,data=JD,partial=True)
        if PDO.is_valid():
            PDO.save()
            return Response({'Update':'Data is Updated'})
        else:
            return Response({'error':'Not ABle To update'})

    def destroy(self,request,pk):
        Product.objects.get(pk=pk).delete()
        return Response({'deleted':'Data is deleted'})
        
         