from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
# Create your models here.
class BaseModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
class Project(BaseModel):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='articles/')
    desc = models.TextField()
    github_link = models.URLField()
    deployed_link = models.URLField()

    def __str__(self):
        return self.title

# class Category(BaseModel):
#     name = models.CharField(max_length=27)

class Review(BaseModel):
    projects = models.ForeignKey(Project,on_delete=models.CASCADE,related_name='projects')
    design = models.IntegerField(default=0,validators=[MinValueValidator(0), MaxValueValidator(10)])
    usablity  = models.IntegerField(default=0,validators=[MinValueValidator(0), MaxValueValidator(10)])
    creativity = models.IntegerField(default=0,validators=[MinValueValidator(0), MaxValueValidator(10)])
    avarage = models.IntegerField(default=0,blank=True,null=True)
    def __str__(self):
        return self.projects.title