# Development Standards
This documentation provides an overview of development best practices across python, sql, continuous integration

## Table of contents

- [App Requirements](#apprequirements)
    * [Git](#git)
    * [HTML Code Docs](#htmlcodedocs)    
    * [HTML Features Docs](#htmlfeaturesdocs)
    * [Requirements](#requirements)

## App Requirements

### Git
Each project needs to be hosted in a remote git repository.
Remote repo type does not matter, but it needs to trigger continuous integration builds.
Readme is required for each repo and it should match the format for showdown.js markdown builds.

- Each header element will be translated to a header tag in html
    - the id of the header tag in html will correspond to the value of the header in Markdown
    - Ex:
    ```
        ### Markdown Section

        <h3 id="markdownsection">Markdown Section</h3>
    ```
- Markdown file must match the name of the directory

- The description used under the header1 markdown tag will be used in the table of contents for all documentation
    - Attempt to describe the project in less than 50 words


### HTML Code Docs
Auto-documentation of python functions describing inputs, outputs, exceptions

### HTML Features Docs
HTML pages that describes the features/functionality of the application.
This should be treated as a developer guide as an overview of the project

### Requirements
How to install dependencies and requirements for documentation
