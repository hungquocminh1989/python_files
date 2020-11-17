<!doctype html>
<?php
require __DIR__ . '/vendor/autoload.php';

use Automattic\WooCommerce\Client;

$woocommerce = new Client(
    $_POST['txt_domain'], 
    $_POST['txt_key'], 
    $_POST['txt_secret'],
    [
        'version' => 'wc/v3',
    ]
);
$product_list = $woocommerce->get('products',['page'=> 1,'per_page' => 100]);
//echo '<pre>';
//var_dump($product_list);
//die();
?>

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
	  <table class="table">
		  <thead>
			<tr>
			  <th scope="col">No.</th>
			  <th scope="col">Product Name</th>
			  <th scope="col">Description</th>
			  <th scope="col">Price</th>
			  <th scope="col">Image</th>
			</tr>
		  </thead>
		  <tbody>
			<?php foreach ($product_list as $k => $row){?>
			<tr>
			  <th scope="row"><?php echo $k + 1;?></th>
			  <td><?php echo $row->name;?></td>
			  <td><?php echo $row->description;?></td>
			  <td><?php echo $row->price;?></td>
			  <td>
				<?php foreach ($row->images as $img){?>
				<img src="<?php echo $img->src;?>" alt="<?php echo $img->name;?>" class="img-thumbnail">
				<?php }?>
			  </td>
			</tr>
			<?php }?>
		  </tbody>
		</table>
	</div>

    <!-- Optional JavaScript -->
    <!-- jQuery first, then Popper.js, then Bootstrap JS -->
    <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.9/umd/popper.min.js" integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" crossorigin="anonymous"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js" integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" crossorigin="anonymous"></script>
  </body>
</html>