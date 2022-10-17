<H1>Сalculation of the subnet mask for a range of ip addresses</H1>

To calculate the mask, pass to the script as an argument the name of the file containing the original ranges of ip addresses.<br>
Launch example:<br>
<i>python calcMask.py ip.txt</i>

File format ip.txt:<br>
1.0.1.0-1.0.3.255<br>
1.0.8.0-1.0.15.255<br>
1.0.32.0-1.0.63.255<br>
1.1.0.0-1.1.0.255<br>
...

As a result, a file will appear in the current directory result.txt , with the result of the script in the format:<br>
File format result.txt<br>
1.0.1.0\22<br>
1.0.8.0\21<br>
1.0.32.0\19<br>
1.1.0.0\24<br>
...
