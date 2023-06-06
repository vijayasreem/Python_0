#!/usr/bin/env python

import os
import sys

# Set environment variables
os.environ['ELASTICSEARCH_URL'] = 'http://localhost:9200'
os.environ['SOLR_URL'] = 'http://localhost:8983'

# Create and configure search engine
from search_engine import SearchEngine
search_engine = SearchEngine()

# Index all products from the database
search_engine.index_all()

# Register the search_engine as a command
from django.core.management.base import BaseCommand
class Command(BaseCommand):
    def handle(self, *args, **options):
        # Run search query against the search index
        search_engine.query(args[0])

# Register the command 
from django.core.management import register_command
register_command('search_engine', Command)

# Automate indexing process
from indexing_process import IndexingProcess
indexing_process = IndexingProcess()

# Run the indexing process
indexing_process.run()