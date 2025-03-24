from django.db import models    # THIS IMPORT THE DJANGO  BUILT IN MODELS/ MODULES  FOR  DATABASE SCHEMA  USING ORM (OBJECT RELATIONAL MODEL)


class Product(models.Model): # THIS IS CLASS PRODUCT (CLASS) INHERITS THE FROM MODELS.MODEL EACH CLASS REPRESENT IN THE DATABASE
    name = models.CharField(max_length=300)
    price = models.IntegerField()
    desc = models.TextField(max_length=400)
    img =models.ImageField(upload_to='product/')
    stock =models.PositiveBigIntegerField()
    

    def __str__(self):
       return f"product: {self. name}" # THIS  ___ str___ METHOD 