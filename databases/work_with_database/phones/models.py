from django.db import models


class Phone(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=150)
    price = models.IntegerField()
    image = models.ImageField(blank=True, null=True)
    release_date = models.DateTimeField()
    lte_exists = models.BooleanField()
    slug = models.SlugField(unique=True)

    def __str__(self):
        return str(self.name) + ": $" + str(self.price)
