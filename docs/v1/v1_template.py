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
        width: 25%;
        min-height:100%;
        position:fixed;
        height:100%;
        font-size: 12px;
    }}


    #docs-wrapper {{
        right: 75%;
        margin-left: 25%;
        font-size: 22px;
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
    </style>
    <script>
    /**********************
    *The purpose of this script is to
    *move the table of contents to the left panel of
    *the output html
    ***********************/
    $('#tableofcontents').nextElementSibling
    </script>
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

    <div id= "docs-wrapper" class="column theme theme-high-contrast">

            <div id="showdownjs-output" class="content">
                {showdown_output}
            </div>
    </div>
</body>

</html>
"""
