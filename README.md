Сalculation of the subnet mask for a range of ip addresses

To calculate the mask, pass to the script as an argument the name of the file containing the original ranges of ip addresses. 
Launch example:
python calcMask.py ip.txt

File format ip.txt:
1.0.1.0-1.0.3.255
1.0.8.0-1.0.15.255
1.0.32.0-1.0.63.255
1.1.0.0-1.1.0.255
...

As a result, a file will appear in the current directory result.txt , with the result of the script in the format:
File format result.txt
1.0.1.0\22
1.0.8.0\21
1.0.32.0\19
1.1.0.0\24