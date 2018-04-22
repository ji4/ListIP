# Brief
It has filterd repeatted IPs in each category, local destination IPs, and sort by specified name so far.

That will come out a result file.

# Manual
* Drag your pcap directory and this scrip into your VM. 
* Edit this script by replacing the `path` with your **pcap directory path** in VM without slash and space at the end.
* Note if your local ip starts with `192.168.137.xxx` as mine or modify it in `filter`.
* Add all your **file names** in the variable `fileName` array with the order you want.
* Run this scipt, that will come out a file **category_ip_sorted** as the result in the same directory as this script. Add **.txt** at the end of file name if needed.
* Copy the content and paste it into the Excel file in Windows.
* Copy the IP column and paste it in **ip_list1** text file in VM and go on your work.

# Note
If you want to execute this script for more than once to the same directory path, remember to remove the output *file* **category_ip_sorted** and *directory* of **ip** to make sure there will be no expectations.
