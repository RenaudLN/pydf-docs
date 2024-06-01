---
name: fields.ModelList
description: fields.ModelList is the base field representation for list of nested pydantic models.
endpoint: /api/model_list_field
package: dash_pydantic_form
icon: fluent:apps-list-detail-20-regular
order: 5
---

.. toc::

### Introduction

`fields.ModelList` allows to render lists nested models in a form, with the option to add and remove items.

.. exec::docs.model_list_field.demo

### Render type

By default `fileds.ModelList` renders each list item in an accordion item. 2 other renders are available: `modal` and `list`.

.. admonition::Note
    :icon: fluent:info-16-regular
    For 'accordion' and 'modal' renders, the label of the item will synchronise with the item's
    'name' field if it exists.

.. exec::docs.model_list_field.render_type

### List of str/number/datetimes

The `ModelList` also allows to render lists of scalar value (str, int, float, date, time, datetime).

.. exec::docs.model_list_field.scalar_list

### API

#### fields.ModelList

.. kwargs::fields.ModelList
