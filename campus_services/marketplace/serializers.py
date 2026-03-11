from rest_framework import serializers
from .models import User,Bid,Task,Skill

class SkillSerializer(serializers.ModelSerializer):
    class Meta:
        model : Skill
        fields = '__all__'
        
        
class UserSerializer(serializers.ModelSerializer):
    
    skills = serializers.PrimaryKeyRelatedField(queryset=Skill.objects.all(),many=True)
    class Meta:
        model : User
        fields = '__all__'
        
class TaskSerializer(serializers.ModelSerializer):
    
    class Meta:
        model : Task
        fields = '__all__'
        read_only_fields = ['created_by']
        
class BidSerializer(serializers.ModelSerializer):
    
    class Meta:
        model : Bid
        fields = '__all__'
        read_only_fields = ['bidder']
       