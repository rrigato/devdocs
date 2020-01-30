# Development Standards
This documentation provides an overview of development best practices across python, sql, continuous integration

## Table of contents

- [App Requirements](#apprequirements)
    * [CI/CD](#cicd)
    * [Git](#git)
    * [HTML Code Docs](#htmlcodedocs)  
    * [HTML Coverage Docs](#htmlcoveragedocs)        
    * [HTML Features Docs](#htmlfeaturesdocs)
    * [Style](#style)

- [Python](#python)
    * [Code Style](#codestyle)
    * [Python Documentation](#pythondocumentation)
    * [Python Tests](#pythontests)
    * [Requirements](#requirements)

- [SQL](#sql)
    * [SQL Table Creation](#sqltablecreation)
    * [SQL Subqueries](#sqlsubqueries)


## App Requirements


### CI/CD
Remote repo type does not matter, but it needs to trigger continuous integration builds. Deployment Pipeline should have a qa environment where tests are run before rolling out to prod.

Project build status should be included in Readme file.


### Git
Each project needs to be hosted in a remote git repository.
Readme is required for each repo and it should match the format for showdown.js markdown builds.

When a feature is merged into the dev branch a tag should be added using the following convention:

```
    v1.0
    v1.1
    ...
    v1.9
    v2.0
    v2.1
```

### HTML Code Docs
Auto-documentation of python functions describing inputs, outputs, exceptions. Built automatically from function docstrings using  [sphinx](http://www.sphinx-doc.org/en/master/)

### HTML Coverage Docs
Code coverage should be built into html files using the [coverage module](https://coverage.readthedocs.io/en/v4.5.x/)

### HTML Features Docs
HTML pages that describes the features/functionality of the application.
This should be treated as a developer guide as an overview of the project

Built from readme using the following markdown rules from showdownjs library:

- Each header element will be translated to a header tag in html
    - the id of the header tag in html will correspond to the value of the header in Markdown
    Ex:

```
    ### Markdown Section
```

```
    <h3 id="markdownsection">Markdown Section</h3>
```

- Markdown file must match the name of the directory

- The description used under the header1 markdown tag will be used in the table of contents for all documentation
    - Attempt to describe the project in less than 50 words


### Style
Consistency with style conventions should take top priority. Follow the outlined [python](#python) and [sql](#sql) style guidelines outlined below.


## Python

### Code Style

These python code style recommendations are mostly from [PEP8](https://www.python.org/dev/peps/pep-0008/)

Any discrepancies from the PEP8 standard are noted:

- 4 space indents
- function names in lower case with underscores
- Class names are CamelCase
- Packages are one word all lower case
- Imports are in alphabetical order
- """ for docstrings and sqlcode you plan to import
- Only use block comments with ''' in code
- Use single line comments sparingly and only for different environments. Ex:
```
    email_list = ['dev_contact@example.com']
    #email_list = ['prod_contact@example.com']
```

### Python Documentation
Follow the [numpy docstring format](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_numpy.html) for each function/class. Ex:

```
def new_function(arg_one):
    '''One sentance that describes what the function does

        Parameters
        ----------
        arg_one : str
            the first arguement passed to the function

        Returns
        -------
        success_ind : int
            0 if success, 1 if failure

        Raises
        ------
        AE : AssertionError
            Raises an assertion error if best practices are not being followed
    '''
```




## Python Tests

Code Coverage should be 80% or higher.

Write unit, integration and end-to-end tests using the built in [unittest module](https://docs.python.org/3/library/unittest.html)


### Requirements
requirements.txt file describing how to install dependencies and requirements for documentation




# SQL

## SQL Table Creation
Always use subqueries instead of creating temporary tables. The only table created should be the final output table

Always have a primary key on the table.

## SQL Subqueries

Always provide a meaningful alias for the subquery. Ex:

```
(
    --Querying weather data
) WEATHER_DATA
```


Above each subquery provide a block comment which provides an overview of the subquery and the unique columns from the subquery. Ex:

```
-------------------------
--My block comment explaining domain knowledge from
--FOO_FIELDS subquery
--
--PK is COL1 and COL2
--SELECT COUNT(*), COUNT(DISTINCT COL1 || COL2)

--100, 100
-------------------------
(
    SELECT COL1, COL2, etc..
    FROM FOO
)FOO_FIELDS
```
