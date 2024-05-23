---
name: DMC fields
description: Dash pydantic form leverages dash-mantine-components to define fields inputs.
endpoint: /api/dmc_fields
package: dash_pydantic_form
icon: fluent:frame-16-regular
order: 3
---

.. toc::

### Default fields inputs

The following mapping is used for default fields inputs:

* `str`: `dmc.TextInput`
* `bool`: `dmc.Checkbox`
* `Number`: `dmc.NumberInput`
* `date`: `dmc.DateInput`
* `time`: `dmc.TimeInput`
* `Literal`: `dmc.Select`
* `Enum`: `dmc.Select`

### Available DMC inputs

You can customise the input used for a form field via `ModelForm`'s `fields_repr` argument.

The DMC fields ported to dash-pydantic-form are the following:

* `fields.Checkbox` (`dmc.Checkbox`)
* `fields.Checklist` (`dmc.CheckboxGroup`)
* `fields.Color` (`dmc.ColorPicker`)
* `fields.Date` (`dmc.DateInput`)
* `fields.Datetime` (`dmc.DateTimePicker`)
* `fields.Json` (`dmc.JsonInput`)
* `fields.MultiSelect` (`dmc.MultiSelect`)
* `fields.Number` (`dmc.NumberInput`)
* `fields.Password` (`dmc.PasswordInput`)
* `fields.RadioItems` (`dmc.RadioGroup`)
* `fields.Range` (`dmc.RangeInput`)
* `fields.SegmentedControl` (`dmc.SegmentedControl`)
* `fields.Select` (`dmc.Select`)
* `fields.Slider` (`dmc.Slider`)
* `fields.Switch` (`dmc.Switch`)
* `fields.Textarea` (`dmc.Textarea`)
* `fields.Text` (`dmc.TextInput`)
* `fields.Time` (`dmc.TimeInput`)


.. admonition::Warning
    :icon: fluent:info-16-regular
    :color: orange
    `dmc.DateTimePicker` has issues as of 0.14.3, you will need to wrap your form/app with a `dmc.DatesProvider`
    setting the timezone to UTC for it to work properly.

### API

#### Simple inputs

.. kwargs::fields.Text

#### Select-style inputs

.. kwargs::fields.Select
