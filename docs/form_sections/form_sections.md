---
name: Sections
description: Use Sections to add sections and steps to your form.
endpoint: /api/sections
package: dash_pydantic_form
icon: fluent:align-space-evenly-vertical-24-regular
order: 2
---

.. toc::

### Introduction

You can add sections to your form wit `Sections`

.. exec::docs.form_sections.introduction

### Render types

By default they will be rendered in an accordion but you can also choose tabs or steps.

.. exec::docs.form_sections.section_renders
    :code: false

### Extra fields

By default fields not defined in any of the sections will be rendered after the sections.
You can choose to have them appear at the top or not at all instead.

You can also define some fields to exclude from the form via `excluded_fields`.

.. exec::docs.form_sections.extra_fields
    :code: false

### API

#### Sections

.. kwargs::Sections

#### FormSection

.. kwargs::FormSection
