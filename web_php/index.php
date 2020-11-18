<!doctype html>
<html lang="en">
    <head>
        <!-- Required meta tags -->
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
        <!-- Bootstrap CSS -->
        <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css" integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" crossorigin="anonymous">
        <title>Hello, world!</title>
    </head>
    <body>
        <div class="container">
            <div class="row">
                <div class="col-sm-12">
                    <form action="./products.php" method="post">
                        <div class="form-group">
                            <label for="txt_domain">Domain</label>
                            <input type="text" class="form-control" id="txt_domain" name="txt_domain" placeholder="http://example.com/" value="http://demo2.thanhtran.info/">
                        </div>
                        <div class="form-group">
                            <label for="txt_key">Woo api key</label>
                            <input type="text" class="form-control" id="txt_key" name="txt_key" placeholder="ck_XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX" value="ck_6e57c4432fdbdf71cb27cd9847a2b87f662e7a22">
                        </div>
                        <div class="form-group">
                            <label for="txt_secret">Woo api secret</label>
                            <input type="text" class="form-control" id="txt_secret" name="txt_secret" placeholder="cs_XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX" value="cs_92da46966ea74747225ae230ea455f9c622b4da3">
                        </div>
						<div class="form-group">
                            <label for="txt_fbpageid">Page id</label>
                            <input type="text" class="form-control" id="txt_fbpageid" name="txt_fbpageid" placeholder="" value="">
                        </div>
                        <button type="submit" class="btn btn-primary">Load products</button>
                    </form>
                </div>
            </div>
        </div>
        <!-- Optional JavaScript -->
        <!-- jQuery first, then Popper.js, then Bootstrap JS -->
        <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>
        <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
    </body>
</html>