from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=100)
    banner = models.ImageField(upload_to="banners_category/")

    def __str__(self):
        return self.title


class SubCategory(models.Model):
    title = models.CharField(max_length=100)
    banner = models.ImageField(upload_to="banners_sub_category/")

    def __str__(self):
        return self.title


class Product(models.Model):
    title = models.CharField(max_length=254, null=True, blank=True)
    picture = models.ImageField(upload_to="images_products/")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title
