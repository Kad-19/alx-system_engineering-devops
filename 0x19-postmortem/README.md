
<h2> <b>Sever Requests Failure Report </b></h2> </br> 
It was reported last month that all of our services were unavailable and that all requests sent to our server were receiving a 500 error. One of our server's configuration files, web_stack_debugging_1, was the root problem.
<h2> <b>TimeLine</b></h2> </br> 
The mistake was discovered on June 2 at 2:00 PM (GMT+3). Notify a member of our staff via Telegram. In order to conduct more investigation and identify the source of the issue, our engineering team on call swiftly logs into the server. The issue was resolved on June 2nd, 5:00 p.m. (GMT+3).
<h2> <b>Root Cause and Resolution </b></h2> </br> 
Because the configuration of the program (Nginx) that serves the server pages is viewed as a directory rather than a symbolic link to another config file, the server ceased functioning. The sites-enabled configuration file was promptly removed. Next, a symbolic link to the original configuration file (sites-available) is created from the config file (sites-enabled). There was a server restart. All traffic has returned to 100%.
