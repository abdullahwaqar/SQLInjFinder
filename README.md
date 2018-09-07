# SQLInjFinder
This program finds vulnerabilities for SQL Injection.

# Run
```
python main.py -h                                                      
usage: main.py [-h] dork result_count

positional arguments:
  dork          ex: inurl:".php?id="
  result_count

optional arguments:
  -h, --help    show this help message and exit
```
### Example

```
python main.py inurl:".php?id=" 5
```

# Screenshot
![screenshot](https://raw.githubusercontent.com/abdullahwaqar/SQLInjFinder/master/asset/Screenshot_2018-09-07_11-47-54.png)
