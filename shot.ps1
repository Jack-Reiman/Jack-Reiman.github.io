param([string]$url="http://localhost:4321/",[string]$out="shot.png",[string]$size="1600,900")
$e='C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'
if(!(Test-Path $e)){$e='C:\Program Files\Google\Chrome\Application\chrome.exe'}
& $e --headless=new --disable-gpu --enable-unsafe-swiftshader --window-size=$size --virtual-time-budget=20000 "--screenshot=$PWD\$out" $url 2>&1 | Out-Null
Test-Path $out
