from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=100)
    banner = models.ImageField(upload_to="banners_category/")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Categoria"
        ordering = ['id']

    def subcategories(self):
        return self.subcategory_set


class SubCategory(models.Model):
    title = models.CharField(max_length=100)
    banner = models.ImageField(upload_to="banners_sub_category/")
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.category.title + " - " + self.title

    class Meta:
        verbose_name = "SubCategoria"
        ordering = ['id']


class Product(models.Model):
    title = models.CharField(max_length=254, null=True, blank=True)
    picture = models.ImageField(upload_to="images_products/")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        # if self.title:
        #     return self.title
        # if self.category:
        #     return "Produto Categoria " + self.category.title
        # if self.subcategory:
        #     return "Produto Categoria " + self.subcategory.category.title + " - Subcategoria - " + self.subcategory.title
        return "Produto " + str(self.id)

    class Meta:
        verbose_name = "Produto"
        ordering = ['-id']
