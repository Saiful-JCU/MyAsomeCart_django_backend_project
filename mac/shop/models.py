from django.db import models

# Create your models here.

class product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    description = models.CharField(max_length=330)
    category = models.CharField(max_length= 50, default="")
    subcategory = models.CharField(max_length= 50, default= "")
    price = models.FloatField(default= 0)
    image = models.ImageField(upload_to= 'shop/images', default= "")
    publication_date = models.DateField() 


# i use str function for return the name of the product instead of the object nmber.
    def __str__(self) :
        return self.product_name