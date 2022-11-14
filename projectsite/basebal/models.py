from django.db import models

class BaseModel(models.Model):
    create_at = models.DateTimeField(
        auto_now_add=True, db_index=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Position(BaseModel):
    description =models.CharField(max_length=100)

class Person(BaseModel):
    
    # firstname=models.CharField(max_length=100)
    # email = models.EmailField(null=True, blank=True, max_length=100)
    # heigth = models.DecimalField(max_digits=10, decimal_places=5, null=True)
    # latitude = models.DecimalField(max_digits=22, decimal_places=16, null=True, blank=True)
    # isActive= models.BooleanField(default=False, verbose_name="Zoning Fee")
    # birthdate= models.DateField(default=TIME_ZONE.now, blank=true)
    # coach =models.ForeignKey(Person, on_delete=models.CASCADE)

# Create your models here.
