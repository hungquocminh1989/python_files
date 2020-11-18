<?php
    require __DIR__ . '/lib/dbo.php';
    
	function create_domain_data($product_list){
		global $dbo;
		
		$domain_url = $_POST['txt_domain'];
		$woo_api_key = $_POST['txt_key'];
		$woo_api_secret = $_POST['txt_secret'];
		$facebook_page_id = $_POST['txt_fbpageid'];
		
		$r = $dbo->rawQuery("
			SELECT * FROM wp_domain WHERE domain_url = '$domain_url'
		");
		if(count($r) > 0){
			$dbo->rawQuery("
				UPDATE wp_domain 
				SET 
					woo_api_key = '$woo_api_key'
					, woo_api_secret = '$woo_api_secret'
					, facebook_page_id = '$facebook_page_id'
				WHERE domain_url = '$domain_url'
			");
		}
		else{
			$dbo->rawQuery("
				INSERT INTO wp_domain (domain_url, woo_api_key, woo_api_secret, facebook_page_id)
				VALUES ('$domain_url', '$woo_api_key', '$woo_api_secret', '$facebook_page_id');
			");
		}
		$r = $dbo->rawQuery("
			SELECT id FROM wp_domain WHERE domain_url = '$domain_url'
		");
		$wp_domain_id = $r[0]['id'];
		
		if(count($product_list) > 0){
			foreach ($product_list as $k => $row){
				create_product_data($wp_domain_id, $row);
			}
		}
	}
	
	function create_product_data($wp_domain_id, $row){
		global $dbo;
		
		$product_id = $row->id;
		$product_name = $row->name;
		$product_description = $row->description;
		$product_price = $row->price;
		$product_images = '';
		$product_images_arr = [];
		foreach ($row->images as $img){
			$product_images_arr[] = $img->src;
		}
		$product_images = implode('|||', $product_images_arr);
		
		$r = $dbo->rawQuery("
			SELECT * FROM wp_product WHERE product_id = '$product_id' AND del_flg = 0
		");
		if(count($r) > 0){
			$dbo->rawQuery("
				UPDATE wp_product 
				SET 
					product_name = '$product_name'
					, product_description = \"$product_description\"
					, product_price = '$product_price'
					, product_images = '$product_images'
				WHERE product_id = '$product_id'
			");
		}
		else{
			$dbo->rawQuery("
				INSERT INTO wp_product (wp_domain_id, product_id, product_name, product_description, product_price, product_images)
				VALUES ('$wp_domain_id', '$product_id', '$product_name', \"$product_description\", '$product_price', '$product_images');
			");
		}
	}