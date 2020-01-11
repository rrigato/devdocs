APPS_HTML_TEMPLATE = """
<html>
<!-- Html template inspired from this codepen open source
example Developed By Yasser Mas:
https://codepen.io/shaban07/pen/BxwqyR
-->
<head>

    <meta name="viewport"
    content="width=device-width, initial-scale=1">
<!--
    Linking to external libraries and css/js files locally
-->
    <link rel="stylesheet" type="text/css" href="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/css/bootstrap.min.css">
    <link rel="stylesheet" type="text/css" href="apps_template.css">

    <script type="text/javascript"
    src="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js"></script>
    <script
      src="https://code.jquery.com/jquery-3.4.1.min.js"></script>
    <script type="text/javascript" src="apps_template.js"></script>
</head>
<body>
<div class="container">
      <div class="header_wrap">
        <div class="num_rows">

				<div class="form-group"> 	<!--		Show Numbers Of Rows 		-->
			 		<select class  ="form-control" name="state" id="maxRows">

                        <!--
                            Provides the options of how many rows
                            to view at a time
                        -->
						 <option value="10">10</option>
						 <option value="15">15</option>
						 <option value="20">20</option>
						 <option value="50">50</option>
						 <option value="70">70</option>
						 <option value="100">100</option>
            <option value="5000">Show ALL Rows</option>
						</select>

			  	</div>
        </div>
        <div class="tb_search">
<input type="text" id="search_input_all" onkeyup="FilterkeyWord_all_table()" placeholder="Search.." class="form-control">
        </div>
      </div>
<table class="table table-striped table-class" id= "table-id">


<thead>
<tr>
		<th>Project Name</th>
		<th>Project Description</th>
		<th>Date</th>
	</tr>
  </thead>
<tbody>

	<tr>
		<td>Griffith Flowers</td>
		<td>Ut.tincidunt@tellus.ca</td>

		<td>Sep 12, 2015</td>
	</tr>


    <tbody>
</table>

<!--		Start Pagination -->
			<div class='pagination-container'>
				<nav>
				  <ul class="pagination">
				   <!--	Here the JS Function Will Add the Rows -->
				  </ul>
				</nav>
			</div>
      <div class="rows_count">Showing 11 to 20 of 91 entries</div>

</div> <!-- 		End of Container -->


</body>

</html>

"""
