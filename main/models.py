from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=200)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title

class Product(models.Model):
    title = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def save(self, *args, **kwargs):
        if self.quantity < 0:
            self.quantity = 0
        elif self.quantity > 100000:
            self.quantity = 100000
        if self.price < 0:
            self.price = 0
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


    def get_category_hierarchy(self):
        hierarchy = []
        category = self.category
        while category:
            hierarchy.append(category.title)
            category = category.parent
        return ' · '.join(reversed(hierarchy))