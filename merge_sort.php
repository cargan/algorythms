<?php

$data = array(7, 2, 4, 3, 8, 1, 6, 5);
$length = count($data);

$left = array_slice($data, 0, $length / 2); 
$right = array_slice($data, $length / 2); 

print_r($left);
print_r($right);

for ($i=0; $i<count($left); $i++) {
	print_r($left[$i]);
}
