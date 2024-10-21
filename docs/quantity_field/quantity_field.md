---
name: fields.Quantity
description: Use the Quantity to automatically create a form for a field with value and unit.
endpoint: /api/quantity
package: dash_pydantic_form
icon: fluent-mdl2:quantity
order: 9
---

.. toc::

### Basic quantity field

Use this field when you need to record a value and a unit together.
You can choose whether the field auto-converts between units with `auto_convert`.
If left to `None` the field will try to do auto-conversion based on the unit options.
If only one unit option is passed, the unit select is not rendered, and instead default prefix and placeholder are added.

.. exec::docs.quantity_field.basic
    :code: true


### API

#### fields.Markdown

.. kwargs::fields.Quantity
