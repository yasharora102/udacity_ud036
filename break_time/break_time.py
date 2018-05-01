from __future__ import print_function
import time
import webbrowser

total_breaks=3
break_count=0
print("This program started on ", time.ctime())
while(break_count<total_breaks):
	time.sleep(10)
	webbrowser.open("https://www.youtube.com/watch?v=J701ucIsrrk")
	break_count+=1