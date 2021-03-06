from django.db import models


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    """ fitment's include Brake upgrades, engine parts, seats etc """
    fitment = models.CharField(max_length=254, blank='universal')
    """
    Vehicle - if product is listed universal
    is it still specific to a model
    """
    vehicle = models.BooleanField(default=False, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name


class Fitment(models.Model):
    """ 
    This model I created in error when I first did my database,
    I tried to remove it, but almost lost my whole database,
    So I was too scared to try remove it again
    """

    fitment = models.CharField(max_length=254, blank='universal')

    def __str__(self):
        return self.fitment
