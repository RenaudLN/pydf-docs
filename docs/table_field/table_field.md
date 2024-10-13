---
name: fields.Table
description: fields.Table is the base field representation for list of nested pydantic models.
endpoint: /api/table_field
package: dash_pydantic_form
icon: fluent:table-freeze-row-24-regular
order: 7
---

.. toc::

### Introduction

`fields.Table` allows to render lists nested models in a form, with the option to add and remove items.

.. exec::docs.table_field.demo

### Interactive

.. exec::docs.table_field.interactive
    :code: false

### Dynamic options

You can define dynamic options on select-like sub-fields of Table fields to dynamically update the options based on the current row content. To do so, you need to define a javascript function on a sub-namespace of `dash_clientside`, similar to how you would use Dash's `ClientsideFunction`. The function will get 3 arguments:
* All the dropdown options
* The current row data
* The cell editor params

.. exec::docs.table_field.dynamic_options

.. source::docs/table_field/dynamic_options.js

### API

#### fields.Table

.. kwargs::fields.Table
