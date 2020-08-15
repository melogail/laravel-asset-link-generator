[![contributions welcome](https://img.shields.io/badge/contribution-welcome-brightgreen)](https://github.com/melogail/laravel-asset-link-generator/issues)  ![version 0.1](https://img.shields.io/badge/version-0.1-orange)
# Laravel blade ```asset()``` link generator using python
## Description:
This small python program is useful for PHP framework "Laravel" developers. It helps to wrap the paths of ```src="/path"``` 
and ```href="/path"``` for ```HTML``` attributes into blade template ```{{asset("/path")}}```.


### Example:

Change from:
```php
<img src="../assets/imags/my-image.jpg" />
<a href="../assets/pdfs/my-file.pdf">Download PDF</a>
<script src="../assets/js/script.js"></script>
```

to:

```php
<img src="{{asset("imags/my-image.jpg")}}" />
<a href="{{asset("pdfs/my-file.pdf")}}">Download PDF</a>
<script src="{{asset("js/script.js")}}"></script>
```

It saves time of manually changing ```HTML``` paths in attributes.

### How it works:
First you have to have `Python` programming language installed `globally` on your machine to make run the program. You
can download `Python` from [https://python.org](https://www.python.org/downloads/).

Follow the installation instructions and make sure you setup `Python` path globally to access python anywhere from your 
machine.

#### Running the program
The program uses the `cmd` on Windows or `terminal` on MAC and Linux operating systems. follow the steps to run the program
successfully.
- Its better to add the program file `assets_change.py` file in the same directory of your views files `resources/views`
where the blade files you want to change lives in. But you can run the program anywhere of your machine as long as you 
have global access to `Python`.
- Open the `cms` or `terminal` window in the same directory where you have the program inside `./asset_change.py` and type
the following command
```
python asset_change.py <your-file-path.blade.php> <common-asset-pattern>
``` 
<b>Your file path: </b> is the path of your blade file.

<b>Common asset pattern: </b> is a common pattern specified for all your links ex: `frontend/js/script.js` and 
`frontend/css/style.css`, here you can find `frontend/` is common among your paths.
* Press `Enter` or `Return` button to run the code.
***
###Fix your code arrangement
The downside here is that your `HTML` code will not be arranged with tabs and spaces, the solution for this issue is to
use any online `HTML` formatter websites like the one in the this [link](https://www.freeformatter.com/html-formatter.html)
