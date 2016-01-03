<!DOCTYPE html>
<html lang="en">
  <head>
    <meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>MagicSuggest Tutorial</title>
    <link href="lib/bootstrap/css/bootstrap.min.css" rel="stylesheet">
    <link href="lib/magicsuggest/magicsuggest.css" rel="stylesheet">
    <link rel="stylesheet" type="text/css" href="css/style.css">
  </head>
  <body>
    <div class="container">
        <h1>Hello, world!</h1>
        <form action="subscribe.php" method="post">
            <div class="form-group">
                <label>First name</label>
                <input class="form-control" name="firstname"/>
            </div>
            <div class="form-group">
                <label>Last name</label>
                <input class="form-control" name="lastname"/>
            </div>
            <div class="form-group">
                <label>Countries</label>
                <input id="ms" class="form-control" name="countries[]"/>
            </div>
            <input type="submit" class="btn btn-success pull-right" value="Submit"/>
        </form>
    </div>


    <!-- jQuery (necessary for Bootstrap's JavaScript plugins) -->
    <script src="lib/jquery/jquery-1.11.1.min.js"></script>
    <!-- Include all compiled plugins (below), or include individual files as needed -->
    <script src="lib/bootstrap/js/bootstrap.min.js"></script>
    <script src="lib/magicsuggest/magicsuggest.js"></script>
    <script src="js/script.js"></script>
  </body>
</html>