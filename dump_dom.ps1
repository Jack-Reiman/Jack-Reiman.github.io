param([string]$url="http://localhost:4321/", [string]$out="dom.html")
$e='C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe'
if (!(Test-Path $e)) { $e='C:\Program Files\Google\Chrome\Application\chrome.exe' }
& $e --headless=new --disable-gpu --enable-unsafe-swiftshader --window-size=1600,900 --virtual-time-budget=20000 --dump-dom $url > $out
(Get-Content $out).Length
