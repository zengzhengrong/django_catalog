# django_catalog

[![ENV](https://img.shields.io/badge/django-1.7+-green.svg)](https://github.com/pylixm/django-mdeditor)

# Usage
Clone ```catalog```folder and paste into your project directory

Add it to your INSTALLED_APPS:
```
INSTALLED_APPS = [
    ...
    'django_private_chat',
    ...
]
```
Add to the template you want to use
```
{% load catalog_tags %}
```
```
<div id="content">{{ object.content|catalog }}</div>
```
Where template you want to show
```
{% include "catalog/catalog.html" with content=object.content %}
```
# Settings Conf

The default html tags are h4 and h5，If you need to replace it ，use：
```
SET_CATALOG_ID = ('h2','h3')
```
also you can add attribute like this:
```
SET_CATALOG_ATTR = {
     'ul':'class="list-group"',
     'li':'class="list-group-item"'
}
```
