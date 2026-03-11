from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import User,Bid,Skill,Task
from .serializers import UserSerializer,BidSerializer,SkillSerializer,TaskSerializer

# Create your views here.

class SkillViewSet(viewsets.ModelViewSet):
    queryset= Skill.objects.all()
    serializer_class = SkillSerializer
    
class UserViewSet(viewsets.ModelViewSet):
    queryset= User.objects.all()
    serializer_class = UserSerializer
    
class TaskViewSet(viewsets.ModelViewSet):
    queryset= Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]
    
    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)
        
    
class BidViewSet(viewsets.ModelViewSet):
    queryset= Bid.objects.all()
    serializer_class = BidSerializer
    permission_classes = [IsAuthenticated]
    
    def perform_create(self, serializer):
        serializer.save(bidder=self.request.user)
        
    @action(detail=True,methods=['post'])
    def accept_bid(self,request,pk=None):
        bid = self.get_object()
        task =bid.task
        if task.created_by != request.user:
            return Response({'error':'Only task creator can accept bids'})
        
        bid.status = 'ACCEPTED'
        bid.save()
        
        task.status = 'IN_PROGRESS'
        bid.save()
        
        Bid.objects.filter(task=task).exclude(id=bid.id).update(status='REJECTED')
        
        return Response({'message':"Bid accepted"})
        
    
  