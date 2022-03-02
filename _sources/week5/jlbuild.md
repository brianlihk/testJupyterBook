# Notes jotted while building JupyterLite webpage

## What I have done to develop a Jupyter Lite website
1. I installed Raspbian OS in a raspberry pi hosted in my home, redirected all incoming traffic from port 22 and 80 of my home router to the raspberry pi server to process.
2. I installed jupyter lab into raspberry pi as it is a essential component to build jupyter lite.
3. I installed jupyter lite which is extension of jupyter lab.
4. i use ```jupyter lite init``` to build essential files to build given by jupyter lite.
5. use ```jupyter build``` to build the jupyter lite web from current directory to \_output folder.
6. We can now serve the output file to the internet, and after I played with it, i can say it in 90% like python we used to use in our computer.
7. I installed apache2 and put all output files from jupyter lite to ```/var/www/html/``` so the content server can deliver Jupyter lite to our user.
8. I registered a subdomain under duckdns.org for free, so i make use of it and make a script to update my ip for that subdomain from my raspberry pi automatically each 5 minutes. So I assume user can enter Jupyter Lite with a proper domain than a ipv4 address.

## What i had found while i testing out Jupyter Lite
1. Extra pyWheel file (aka python package) in Jupyter lab could be installed by executing ```!pip install [package name]``` usually, but in Jupyter Lite, this method does not work. We need to use a package called micropip in pyodide to install extra packages.
```{figure} /week5/micropip.png
:name: micropip testing
```
2. Regular approach to retrive external data from website is not working, we need to use other method to download data from the internet, i will drill into that next week.