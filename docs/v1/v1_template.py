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
    ****************/
    #left-panel {{
        width: 20%;
        min-height:100%;
        position:fixed;
        height:100%;
        font-size:large;
    }}
    /*
    *Title and body of table of contents
    *inherit font size from left-panel
    */
    .is-info{{
        font-size:inherit;
    }}
    

    #docs-wrapper {{
        right: 80%;
        margin-left: 20%;
        font-size: x-large;
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
        //Using important here isnt great, but the
        //code block in the import template is using it as
        //well plus there isnt an easy way to add a class to
        //showdown
        line-height:1.6 !important;
    }}
    </style>


</head>
<body>
<div id="left-panel">
    <div class="alert is-info">
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
