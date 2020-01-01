HTML_TEMPLATE = """
<html>
<head>
    <!--
        Microsoft documentation theme,
        inspired by this codepen:
        https://codepen.io/jdanyow/pen/drVONG
    -->
    <link rel="stylesheet" href="https://static.docs.com/ui/latest/site/en-us/styles/site-ltr.css">
    <style>



        /***************
        *Info panel on the
        *left side of the page
        *with table of contents
        ****************/
        #left-panel {{
            width: 20%;
            min-height:100%;
            position:fixed;
            height:100%;
            font-size:large;
            background-color: lightgray;
            display: inline;
        }}

        #docs-wrapper {{
            right: 80%;
            margin-left: 20%;
            font-size: x-large;
        }}

    /***************
    *Hiding the left info table of contents
    *if the width of the screen is 550px or
    *less
    ****************/
    @media screen and (max-width: 550px) {{

        #left-panel {{
            display: none;
        }}
        #docs-wrapper {{
            right: 100%;
            margin-left: 0%;
        }}
    }}
    /*
    *Title and body of table of contents
    *inherit font size from left-panel
    */
    .is-info{{
        font-size:inherit;
    }}



    /*****************
    *Just the html output by showdownjs
    *
    ******************/
    #showdownjs-output{{
        margin-left: 2%;
        margin-top: 2%;
    }}
    .alert.is-info{{
        margin-top: 0;
        height:100%;

    }}
    /*
        Used to make code block more readable
    */
    code{{
        font-size:x-large;
        /*
            Using important here isnt great, but the
            code block in the import template is using it as
            well plus there isnt an easy way to add a class to
            showdown
            Making the line-height:1.6 really improves readability
        */
        line-height:1.6 !important;
    }}

    #alert-override{{

        font-color: black;
        margin-left:5%;
        margin-top:8%;

    }}
    </style>


</head>
<body>
<div id="left-panel">
    <div id="alert-override" >
  <p class="alert-title">
    <!--Info symbol-->
    <span class="docon docon-status-error-outline"></span>
    {project_name} Table of Contents
  </p>
  <p id="list-table-of-contents">
    <!--Table of contents will be placed here-->
  </p>
</div>
</div>

    <div id= "docs-wrapper" class="column theme theme-dark">

            <div id="showdownjs-output" class="content">
                {showdown_output}
            </div>
    </div>
    <!--
    Custom Footer to provide some room at bottom of page
    Potientially add a watermark/copyright in the future
    -->
    <div id="markdown-footer" class="column theme theme-dark">
        <br>
        <br>
    </div>
</body>

    <script>
    /**********************
    *The purpose of this script is to
    *move the table of contents to the left panel of
    *the output html
    *
    *nextElementSibling = gets the ul which corresponds
    *to the h3 (## in markdown) with the value table of contents
    ***********************/
    document.getElementById("list-table-of-contents").innerHTML = (

    document.getElementById(
        "tableofcontents").nextElementSibling.innerHTML
    );
    </script>

</html>
"""
