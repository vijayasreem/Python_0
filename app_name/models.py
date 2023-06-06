from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()
    
    class Meta:
        abstract = True

class SearchIndex(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    index_data = models.TextField()
    
    def index(self):
        # Automatically index the product data
        pass
    
    def delete_index(self):
        # Automatically delete the index data
        pass
    
    def update_index(self):
        # Automatically update the index data
        pass
    
    def search(self):
        # Execute a search query against the search index
        pass