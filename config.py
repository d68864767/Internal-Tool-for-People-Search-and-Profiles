# config.py

import os

class Config(object):
    """Base config, uses staging database server."""
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'this-really-needs-to-be-changed'
    ELASTICSEARCH_URL = 'http://localhost:9200'
    GPT_INDEX_URL = 'http://localhost:5000'
    DATA_WAREHOUSE_URL = 'http://localhost:5432'

class ProductionConfig(Config):
    """Uses production database server."""
    DEBUG = False
    ELASTICSEARCH_URL = os.getenv('ELASTICSEARCH_URL')
    GPT_INDEX_URL = os.getenv('GPT_INDEX_URL')
    DATA_WAREHOUSE_URL = os.getenv('DATA_WAREHOUSE_URL')

class DevelopmentConfig(Config):
    """Uses development database server."""
    DEVELOPMENT = True
    DEBUG = True

class TestingConfig(Config):
    """Uses testing database server."""
    TESTING = True
