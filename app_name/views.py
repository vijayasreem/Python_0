from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.db import models
from elasticsearch import Elasticsearch
import json

# Create your views here.
def indexing_view(request):
    # Connect to Elasticsearch
    es = Elasticsearch()

    # Retrieve all products from the database
    products = models.Product.objects.all()

    # Create an index for the products
    es.indices.create(index='product_index', ignore=400)

    # Index all products
    for product in products:
        product_data = {
            'name': product.name,
            'price': product.price,
            'description': product.description
        }
        es.index(index='product_index', id=product.id, body=product_data)

    # Automate indexing
    models.signals.post_save.connect(index_product, sender=models.Product)
    models.signals.post_delete.connect(delete_product, sender=models.Product)

    # Execute search query against index
    query = request.GET.get('q')
    if query:
        search_results = es.search(index='product_index', body={
            'query': {
                'match': {
                    'name': query
                }
            }
        })

        # Render search results
        template = loader.get_template('index.html')
        context = {
            'results': search_results
        }
        return HttpResponse(template.render(context, request))
    else:
        return HttpResponse("No search query.")

# Index a product
def index_product(sender, instance, **kwargs):
    # Connect to Elasticsearch
    es = Elasticsearch()

    # Create a new product document
    product_data = {
        'name': instance.name,
        'price': instance.price,
        'description': instance.description
    }

    # Index the document
    es.index(index='product_index', id=instance.id, body=product_data)

# Delete a product
def delete_product(sender, instance, **kwargs):
    # Connect to Elasticsearch
    es = Elasticsearch()

    # Delete the document
    es.delete(index='product_index', id=instance.id)