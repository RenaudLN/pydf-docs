---
name: fields.List
description: fields.List is the base field representation for list of scalar and nested pydantic models.
endpoint: /api/list_field
package: dash_pydantic_form
icon: fluent:apps-list-detail-20-regular
order: 5
---

.. toc::

### Introduction

`fields.List` allows to render lists nested models in a form, with the option to add and remove items.

.. exec::docs.list_field.demo

### Render type

By default `fileds.List` renders each list item in an accordion item. 2 other renders are available: `modal` and `list`.

.. admonition::Note
    :icon: fluent:info-16-regular
    For 'accordion' and 'modal' renders, the label of the item will synchronise with the item's
    'name' field if it exists.

.. exec::docs.list_field.render_type
    :code: false

### List of str/number/datetimes

.. admonition::
    New in 0.1.18

The `List` also allows to render lists of scalar value (str, int, float, date, time, datetime).

.. exec::docs.list_field.scalar_list

### API

#### fields.List

.. kwargs::fields.List
