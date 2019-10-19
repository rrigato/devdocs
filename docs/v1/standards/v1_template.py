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
    #left-panel {
        width: 25%;
        min-height:100%;
        position:absolute;
        height:100%;
        font-size: 12px;
    }
    /*****************
    *
    *
    ******************/
    #docs-wrapper {
        right: 75%;
        margin-left: 25%;
        font-size: 22px;
    }
    .alert.is-info{
        margin-top: 0;
        height:100%;

    }
    </style>
</head>
<body>
<div id="left-panel">
    <div class="alert is-info">
  <p class="alert-title"><span class="docon docon-status-error-outline"></span> Info</p>
  <p>Test note: this side panel will eventually be updated with the index</p>
</div>
</div>

    <div id= "docs-wrapper" class="column theme theme-high-contrast">

            <div class="content">
                {showdown_output}
            </div>
    </div>
</body>

</html>
"""
