'''
<?php
class FLAG{
	public $file;
}
$a = new FLAG();
$a -> $file = "flag.php";
$a = serialize($a);
print_r($a);
?>

//输出结果为O:4:"FLAG":2:{s:4:"file";N;s:0:"";s:8:"flag.php";}
'''