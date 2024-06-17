---
name: fields.Dict
description: fields.Dict is the base field representation for dict of scalar and nested pydantic models.
endpoint: /api/dict_field
package: dash_pydantic_form
icon: lucide:curly-braces
order: 5
---

.. toc::

### Introduction

.. admonition::
    New in 0.2.0

`fields.Dict` allows to render dicts of nested models, with the possibility to add or remove items.

.. exec::docs.dict_field.demo

.. admonition::Note
    :icon: fluent:info-16-regular
    Only string keys are currently supported

### Render type

By default `fileds.List` renders each list item in an accordion item. 2 other renders are available: `modal` and `list`.

.. admonition::Note
    :icon: fluent:info-16-regular
    For 'accordion' and 'modal' renders, the label of the item will synchronise with the item's
    'name' field if it exists.

.. exec::docs.dict_field.render_type
    :code: false

### Dict of str/number/datetimes

The `Dict` also allows to render dicts of scalar value (str, int, float, date, time, datetime).

.. exec::docs.dict_field.scalar_dict

### API

#### fields.Dict

.. kwargs::fields.Dict
