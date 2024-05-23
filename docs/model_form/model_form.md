---
name: ModelForm
description: Use the ModelForm to automatically create a form for a Pydantic model.
endpoint: /api/model_form
package: dash_pydantic_form
icon: fluent:form-24-regular
order: 1
---

.. toc::

### Basic auto-generated form

You can create a form from a pydantic model by simply wrapping it with `ModelForm`.
Default input types will be inferred from the model type annotation.

The `ModelForm` then allows you to retrieve all the form data in a single dash Input/State.

.. exec::docs.model_form.basic_auto_form
    :code: true


### Customise fields display

You can customise each input field, e.g.:
* Changing from Select to RadioItems
* Updating the field label and description
* Passing additional parameters to the DMC inputs

.. exec::docs.model_form.custom_fields_repr

### Edit an existing object

`ModelForm` accepts an instance of a pydantic model which will show a form pre-filled with the object values.

.. exec::docs.model_form.model_instance

### Nested models

`ModelForm` accepts pydantic models with the following types of nested models:
* Pydantic models
* List of pydantic models
* Discriminated model union with `str` discriminator

.. exec::docs.model_form.nested_models

### Conditionally visible fields

You can make parts of the form conditionally visible, depending on other inputs present in the form.

The available operators fo conditional visibility are `==`, `!=`, `in`, `not in`, `array_-_contains` and `array_contains_any`.

.. exec::docs.model_form.conditionally_visible

### Read-only form display

In some cases you may want to display the contents of a form in a read-only way.
ModelForm allows you to keep the structure of the form and render the contents of each field for viewing.
The displayed result will respect sections and conditionally visible fields.

.. exec::docs.model_form.read_only

### API

#### ModelForm

.. kwargs::ModelForm
