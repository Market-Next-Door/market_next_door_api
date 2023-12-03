from django.db import models

class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone = models.CharField(max_length = 10)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    location = models.CharField(max_length=255)
    date_created = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.first_name + " " + self.last_name

class Vendor(models.Model):
    market = models.ForeignKey('Market', on_delete=models.CASCADE, null=True) # will need 'null=False' later
    vendor_name = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    location = models.CharField(max_length=255)
    date_created = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.vendor_name

class Item(models.Model):
    item_name = models.CharField(max_length=50)
    vendor = models.ForeignKey(Vendor, on_delete=models.CASCADE, null=False)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    size = models.IntegerField(null=True)
    quantity = models.IntegerField(default=1)
    availability = models.BooleanField(default=False)
    description = models.TextField(max_length=255)
    date_created = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='files/images', null=True, blank=True) 

    def __str__(self):
        return self.item_name

class Market(models.Model):
    market_name = models.CharField(max_length=50)
    location = models.CharField(max_length =100)
    details = models.CharField(max_length=100)
    startdate = models.DateField(null=True)
    enddate = models.DateField(null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.market_name

class Preorder(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=False)
    item = models.ManyToManyField(Item, through='PreorderItem')
    ready = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class PreorderItem(models.Model):
    preorder = models.ForeignKey(Preorder, on_delete=models.CASCADE, null=False)
    item = models.ForeignKey(Item, on_delete=models.CASCADE, null=False)
    quantity = models.IntegerField(default=1)
    date_created = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
