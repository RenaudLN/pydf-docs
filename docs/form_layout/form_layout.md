---
name: FormLayout
description: Use FormLayout to add sections and steps to your form.
endpoint: /api/form_layout
package: dash_pydantic_form
icon: fluent:align-space-evenly-vertical-24-regular
order: 2
---

.. toc::

### Introduction

You can add control the flow of your form using `FormLayout`.

.. exec::docs.form_layout.introduction

### Built-in layouts

3 form layouts are currently available by default in `dash_pydantic_form`:

* accordion (`AccordionFormLayout`)
* tabs (`TabsFormLayout`)
* steps (`StepsFormLayout`)

These 3 layout accept:
* `sections` which is a list of `FormSection` objects
* `remaining_fields_position` which can be `"top"`, `"bottom"` or `"none"`
* `render_kwargs` which are keyword arguments passed to the dmc Accordion, Tabs and Steps components respectively.

.. exec::docs.form_layout.built_in_layouts
    :code: false

### Custom layouts

.. admonition::
    New in 0.13.0

You can also create your own custom layouts by subclassing `FormLayout`.
You will need to:
* Add a `layout` field of type `Literal` with one value. This is used to discriminate between layout for serialisation/deserialisation.
* Add whatever additional fields you need for the layout.
* Implement the `render` method which takes the following arguments:
    * aio_id (for the form ids)
    * form_id (for the form ids)
    * path (for the form ids)
    * field_inputs, a dictionary of inputs for each field

You can use the `FormLayout` subclasses directly in you ModelForm, or use `FormLayout.load(layout="<layout_name>", **layout_kwargs)`. If you do so, make sure the `FormLayout` subclass is imported in your application.

### API

#### AccordionFormLayout

.. kwargs::AccordionFormLayout

#### TabsFormLayout

.. kwargs::TabsFormLayout

#### StepsFormLayout

.. kwargs::StepsFormLayout

#### FormSection

.. kwargs::FormSection
