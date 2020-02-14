from .models import Project,Review

from rest_framework import serializers
from django.db.models import Avg
class ProjectSerializer(serializers.ModelSerializer):
    reviews = serializers.SerializerMethodField()
    class Meta:
        model = Project
        fields = (
            'id',
            'title',
            'image',
            'reviews',
        )
    def get_reviews(self,obj):
        return ReviewSerializer(obj.projects.all(),many=True).data

class ReviewSerializer(serializers.ModelSerializer):
    avarage = serializers.SerializerMethodField()
    class Meta:
        model = Review
        fields = (
            'id',
            'usablity',
            'creativity',
            'design',
            'avarage'
        )
    def get_avarage(self,obj):
        avg = (obj.usablity + obj.creativity + obj.design )
        # print(avg)
        avg1 = avg / 3
        return avg1
class ReviewCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = (
            'id',
            'projects',
            'usablity',
            'creativity',
            'design'
        )