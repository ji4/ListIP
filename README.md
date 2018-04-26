# Brief
It has filterd following:
* Repeatted IP in each category
* Local destination IP
* Microsoft IP

You can sort the logs by specified name.
That will come out a result file for all IP and a directory with each file's IPs.

# Manual
* Drag your pcap directory and this scrip into your VM. 
* Edit this script by replacing the `path` with your **pcap directory path** in VM without slash and space at the end.
* Note if your local ip starts with `192.168.137.xxx` as mine or modify it in `filter`.
* Add all your **file names** in the variable `fileName` array with the order you want. If there are many for the same kind of category files such as **Gaming1**, **Gaming2**, ..., just leave one **Gaming** in the array.
* Run this scipt, that will come out a file **category_ip_sorted** as the result under the path where you execute it. Add **.txt** at the end of file name if you cannot open it.
* Copy the content in the file and paste it into the Excel file in Windows.

# Note
If you want to execute this script for more than once to the same directory path, remember to remove the output *file* **category_ip_sorted** and *directory* of **ip** to make sure it will not be out of expectations.

# Reference
* [Removing duplicate lines from a file in Python](https://gist.github.com/dideler/4688053)
