# pad-cal
Attempting to make an open source remake of PadGuide through crowdsourcing. 

Ignore bs4-test.py for the time being. I am hoping to implement this into a Django backend.

    bs4-test.py

    An... attempt... at writing a parser for dungeon pages on padx.
    
    Their HTML code is terribly strange and difficult to parse efficiently.


 Current capabilities :

    1. Parse dungeon data : Titles, Stamina cost, floors, etc
    2. Parse encounter info (HP, ATK, DEF)
    3. Parse Skills of encounters (but not their thresholds yet)

Requirements :

    1. A link to the dungeon page
    2. BeautifulSoup4
    3. Python 3
    4. html5lib or lxml


Here is some example output
    
![alt text](https://github.com/rohilthopu/pad-cal/blob/master/Screenshots/Screen%20Shot%202018-06-29%20at%201.20.29%20AM.png)
