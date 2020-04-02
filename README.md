# zoom meetings bot

### automate entering and exiting zoom meeting. can be placed on an external computer or raspberry pi

### This script:
- enters the zoom meeting automatically with the given link or meeting id.
- enters using your specified name in non audio video mode
- exits the zoom meeting after a specified time



## Quick start
- This needs chrome/chromium installed in the regular default location of the system.
- You'll need chromedriver for this to work along with selenium. Visit https://chromedriver.chromium.org/downloads to get the chromedriver for your version of chrome/chromium and os except raspberry pi. 
- If running on raspberry pi, visit https://launchpad.net/ubuntu/trusty/+package/chromium-chromedriver for the chromedriver and find the newest version for armhf, install both the release and update deb packages and then run

>  `$ sudo apt upgrade -y`. 
 
 This will install the chromedriver in the location 

> `/usr/lib/chromium-browser/chromedriver`

- Install selenium using `pip install selenium`
- Clone the repo: `git clone https://github.com/grajat90/zoombot.git`.
- [Download from Github](https://github.com/grajat90/zoombot/archive/master.zip).


## Usage

> `$ python zoom_bot.py [zoom invite url/Meeting-ID] [Entering Name] [duration] [chromedriver location] -h`
 
 - [entering name] : The name displayed on entering the meeting
 - [duration] : duration after which the bot leaves the meeting (in minutes). Defaults to 50 mins.
 - [chromedriver location] : path to the chromedriver file (defaults to the current directory of python script)
- -h : headless mode, i.e., bot doesn't show a chrome window works in the background and exits the process once done. always include this tag at the absolute end only.

Examples:

> `$ python zoom_bot.py 123456789 john smith 45 -h`

> `$ python zoom_bot.py https://us04web.zoom.us/j/123456789 john smith /usr/lib/chromium-browser/chromedriver`

** The order of arguments must be retained**
***

 


