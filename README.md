# Description
A script to extract specific data in multiple pcap files.
It has filtered following:
* Repeat dst IP in each pcap file
* Local destination IP
* Microsoft IP for dst

You can sort the logs by specified name.
The output result will be under the path of your pcap directory.

# Manual
* Drag your pcap directory and this scrip into your VM. 
* Edit this script by replacing the `path` with your **pcap directory path** in VM without slash or space at the end.
* Note if your local ip starts with `192.168.137.xxx` as mine or modify it in `filter`.
* Add all your **file names** in the variable `fileName` array with the order you want. If there are many for the same kind of category files such as **Gaming1**, **Gaming2**, ..., just leave one **Gaming** in the array.
* Execute this scipt by `python ip.py`, that will come out a directory **output** under your pacp directory. Under **output** directory, **category_ip_sorted** file is the final result.

# Note
If you want to execute this script for more than once to the same directory path, remember to remove the output *directory* of **output** to make sure it will not be out of expectations.

# Reference
* [Removing duplicate lines from a file in Python](https://gist.github.com/dideler/4688053)
