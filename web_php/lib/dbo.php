<?php	
	define('DB_HOST', '');
	define('DB_PORT', '');
	define('DB_NAME', '');
	define('DB_USER', '');
	define('DB_PASS', '');
	
	$dbo = new MysqliDb (
		Array (
		    'host' => DB_HOST,
		    'username' => DB_USER,
		    'password' => DB_PASS,
		    'db'=> DB_NAME,
		    'port' => DB_PORT,
		    'charset' => 'utf8'
    	)
    );
