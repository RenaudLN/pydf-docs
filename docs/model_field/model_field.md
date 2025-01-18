---
name: fields.Model
description: fields.Model is the base field representation for nested pydantic models.
endpoint: /api/model_field
package: dash_pydantic_form
icon: oui:nested
order: 4
---

.. toc::

### Introduction

`fields.Model` allows to render nested models in a 'sub-form'.
It accepts similar arguments to `ModelForm`, on top of the regular fields inputs:
* `fields_repr`
* `form_layout`

.. exec::docs.model_field.demo

### Render type

`fields.Model` can either be rendered as an accordion item or as an openable Modal.

.. exec::docs.model_field.render_type
    :code: false

### API

#### fields.Model

.. kwargs::fields.Model
