from django.shortcuts import render
from rest_framework import viewsets
from .serializers import BanksSerializer,BranchesSerializer
from .models import Banks,Branches
from django.db.models import Q

class BanksViewSet(viewsets.ModelViewSet):
    queryset=Banks.objects.all().order_by('id')
    serializer_class= BanksSerializer

class BranchesViewSet(viewsets.ModelViewSet):
    # queryset=Branches.objects.all().order_by('ifsc')
    serializer_class=BranchesSerializer
    def get_queryset(self):
        name=self.request.query_params.get("q")
        limit=int(self.request.query_params.get("limit"))    
        offset=int(self.request.query_params.get("offset"))
        if not name:
            queryset=Branches.objects.all().order_by('ifsc')[offset:limit]
        else:
             queryset=Branches.objects.filter(Q(ifsc__icontains=name)|Q(bank_id__icontains=name)|Q(branch__icontains=name)|Q(address__icontains=name)|Q(city__icontains=name)|Q(district__icontains=name)|Q(state__icontains=name)).order_by('ifsc')[offset:limit]
        return queryset
       

class BranchAutocompleteViewSet(viewsets.ModelViewSet):
    serializer_class=BranchesSerializer
    def get_queryset(self):
        branchName=self.request.query_params.get("q")     
        limit=int(self.request.query_params.get("limit"))    
        offset=int(self.request.query_params.get("offset"))
        queryset=Branches.objects.filter(branch__icontains=branchName).order_by('ifsc')[offset:limit]
        return queryset
