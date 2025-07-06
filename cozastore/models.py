from django.db import models
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='category_images/')
    is_featured = models.BooleanField(default=False)  # for slider

    def __str__(self):
        return self.name


class Product(models.Model):
    SIZE_CHOICES = [
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
        ('XL', 'Extra Large'),
    ]
    
    COLOR_CHOICES = [
        ('BLK', 'Black'),
        ('BLU', 'Blue'),
        ('WHT', 'White'),
        ('RED', 'Red'),
        ('GRN', 'Green'),
    ]
    
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField()
    featured_image = models.ImageField(upload_to='products/')
    size = models.CharField(max_length=2, choices=SIZE_CHOICES, blank=True, null=True)
    color = models.CharField(max_length=3, choices=COLOR_CHOICES, blank=True, null=True)
    quantity = models.PositiveIntegerField(default=1)
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product_detail', kwargs={'pk': self.pk})
