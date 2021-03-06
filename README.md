# Sub Scraper for Youtube
Currently optimized for videos with closed captions, made for kids, and with unrestricted license.

## Instructions for use
#### Setup
Clone repo, and follow instructions to set up youtube API developer key and ___ file in the repo.
Add developer information to ___ (main.py for now, future config file). 

#### Get Subs
In main.py set max search quantity to the desired number of videos, add search terms to searchTerms list (separated by 
commas, searches for videos related to all terms), add a destination folder name (to primaryTopic, will create a new
folder if necessary), and video directory list file title. Then run main.py, authenticating the service in the terminal.

If there is a next page token error, there were fewer videos fitting the search terms then requested. Change the search
quantity to the highest list length as printed in the terminal and try again.



### To-Do
- [ ] Clean up comments and to-do items
- [ ] Move all optional parameters to end and pass through functions
- [ ] Write summary of what happens, and print info to terminal
- [ ] Add instructions for accessing youtube API
- [ ] Hide API key and json file
- [ ] Muiltiple searches with different terms and remove duplicate videos from ID list