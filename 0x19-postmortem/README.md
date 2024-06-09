
<h1> <b>Sever Requests Failure Report </b></h1> </br> 
Last Month, it was reported that all the request made to our server is returning a 500 Error, all our services were down. The root cause was from one of the configuration file of our server web_stack_debugging_1.

<h1> <b>TimeLine</b></h1> </br> 
The error was realized on 28th of May 2:00 pm(GMT). When pager notify one of our team members. Our engineering team On-call quickly login to the server for further analysis and to get to the root of the problem. The problem was solved later by 28th of May 3:00 pm (GMT).

<h1> <b>Root Cause and Resolution </b></h1> </br> 
The server stopped working because the config of the software(Nginx) serving the server pages is seen to be a directory instead of a symoblic link to another config file. The config file(sites-enabled) was quickly deleted. The config file(sites-enabled) is then made a symbolic link to the original config file(sites-available). The server was restarted. 100% of traffic is back.

<h1> <b>Prevention against such problm in future</b></h1> </br> 
Always test and thoroughly check the config files before deployment.
ALways keep an eye on servers to ensure proper running of them.
Always have backup severs to prevent all of our services from being down during an isuue.
