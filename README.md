# Sub Scraper for Youtube
Currently set for videos with closed captions, made for kids, and with unrestricted license.

## Instructions for use
#### Setup
Clone repo, and follow instructions to set up youtube API developer key 
(https://developers.google.com/youtube/v3/getting-started).
Create file called APIKey.txt and add api developer key. 

#### Get Subs
In main.py set max search quantity to the desired number of videos (which may end up being smaller since some found 
videos don't have subs, add search terms to searchTerms list (separated by commas, searches for videos related to all 
terms), add a destination folder name (to primaryTopic, will create a new folder if necessary), and video directory 
list file title. Then run main.py. When downloading subs, .vtt files will appear in the main project directory, 
then they will get processed and moved to a subfolder. 
In the subfolder, the assets folder contains the sub files in csv format, the text folder contains the 
consolidated subs, and the vids.csv has header information for all the videos used.


### To-Do
- [ ] Clean up comments and to-do items
- [ ] Move all optional parameters to end and pass through functions
- [ ] Write summary of what happens, and print info to terminal
- [x] Add instructions for accessing youtube API
- [x] Hide API key and json file
- [ ] Muiltiple searches with different terms and remove duplicate videos from ID list