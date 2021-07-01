# Sub Scraper for Youtube
Currently set for videos with closed captions, made for kids, and with unrestricted license.

## Instructions for use
#### Setup
Clone repo, and follow instructions to set up youtube API developer key 
(https://developers.google.com/youtube/v3/getting-started).
Add developer key to main.py (for now, future config file). 

#### Get Subs
In main.py set max search quantity to the desired number of videos, add search terms to searchTerms list (separated by 
commas, searches for videos related to all terms), add a destination folder name (to primaryTopic, will create a new
folder if necessary), and video directory list file title. Then run main.py, authenticating the service in the terminal. 
Copy the link, authorize access to your google account, then copy the authorization code back to the terminal (this 
sadly is necessary every time the program is run).

If there is a next page token error, there were fewer videos fitting the search terms then requested. Change the search
quantity to the highest list length as printed in the terminal and try again. This creates a list of videos with the 
right topic, but not necessarily with subs -- so when downloading subs the number of vids may be smaller.

When downloading subs, .vtt files will appear in the main project directory, then they will get processed and moved to 
a subfolder. In the subfolder, the assets folder contains the sub files in csv format, the text folder contains the 
consolidated subs, and the vids.csv has header information for all the videos used.


### To-Do
- [ ] Clean up comments and to-do items
- [ ] Move all optional parameters to end and pass through functions
- [ ] Write summary of what happens, and print info to terminal
- [ ] Add instructions for accessing youtube API
- [ ] Hide API key and json file
- [ ] Muiltiple searches with different terms and remove duplicate videos from ID list