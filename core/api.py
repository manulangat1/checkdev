from .models import Project,Review
from .serializers import ReviewCreateSerializer,ProjectSerializer

from rest_framework import generics

class ProjectList(generics.ListAPIView):
    serializer_class = ProjectSerializer
    queryset = Project.objects.all()
class ReviewCreateList(generics.ListCreateAPIView):
    serializer_class = ReviewCreateSerializer
    queryset = Review.objects.all()