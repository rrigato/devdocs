# Development Standards
This documentation provides an overview of development best practices across python, sql, continuous integration

## Table of contents

- [Python](#python)
    * [Python Documentation](#python-documentation)
- [Paragraphs](#paragraphs)
- [Headings](#headings)
    * [Atx Style](#atx-style)
    * [Setext style](#setext-style)
    * [Header IDs](#header-ids)

## Python

### Python Documentation
Follow the [numpy docstring format](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_numpy.html) for each function/class. Ex:

```
def new_function(markdown_path):
    '''One sentance that describes what the function does

        Parameters
        ----------
        markdown_path : str
            path to the markdown file

        Returns
        -------

        Raises
        ------
        AE : AssertionError
            Raises an assertion error if the
            stder is not empty
    '''
```

## Paragraphs

Paragraphs in Showdown are just **one or more lines of consecutive text** followed by one or more blank lines.

```md
On July 2, an alien mothership entered Earth's orbit and deployed several dozen
saucer-shaped "destroyer" spacecraft, each 15 miles (24 km) wide.

On July 3, the Black Knights, a squadron of Marine Corps F/A-18 Hornets,
participated in an assault on a destroyer near the city of Los Angeles.
```

The implication of the “one or more consecutive lines of text” is that Showdown supports
“hard-wrapped” text paragraphs. This means the following examples produce the same output:

```md
A very long line of text
```

```md
A very
long line
of text
```

If you DO want to add soft line breaks (which translate to `<br>` in HTML) to a paragraph,
you can do so by adding 3 space characters to the end of the line (`  `).

You can also force every line break in paragraphs to translate to `<br>` (as Github does) by
enabling the option **`simpleLineBreaks`**.

## Headings

### Atx Style

You can create a heading by adding one or more # symbols before your heading text. The number of # you use will determine the size of the heading. This is similar to [**atx style**][atx].

```md
# The largest heading (an <h1> tag)
## The second largest heading (an <h2> tag)
…
###### The 6th largest heading (an <h6> tag)
```

The space between `#` and the heading text is not required but you can make that space mandatory by enabling the option **`requireSpaceBeforeHeadingText`**.

You can wrap the headings in `#`. Both leading and trailing `#` will be removed.
