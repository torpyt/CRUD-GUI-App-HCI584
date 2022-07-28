# Developer's Guide

## Overview
* For my project, I created a CRUD GUI  app. My app serves as a part management system for John Deere. The app includes four input fields; part, retailor, customer, and price. Data can be added to a list shown in the GUI. Users can select items in the list and can update or remove them. Users can also clear all input fields with one button. The GUI also includes a scroll bar for easier list navigation. To create this app I used Python (to code), Tkinter (to create the GUI), and Sqlite3 (database).

## Planning specs
### UX Flow
* Please refer to the README file for the UX flow

### Technical Flow
The technicafl flow of my project will look similar to the outline below:
* Import dependencies
    * *from tkinter import* *
    * *from tkinter import messagebox*
    * *from db import Database*

* Define functions for data population, add button, select item, remove button, update button, and clear button.
    * *populate_list*
    * *add_item*
    * *select_item*
    * *remove_item*
    * *update_item*
    * *clear_text*

* Create window (GUI)
* Create input boxes (including text, font, padding, grid alignment)
* Create equipment input
* Create dealer input
* Create customer input
* Create price input
* Create equipment list
* Create scroll bar
* Buttons (including text, font, padding, grid alignment)
* Create add button
* Create remove button
* Create update button
* Create clear button
* Populate data
    * *populate_list()*
* Start program
    * *app.mainloop()*

Please look at the comments in the Run_Part_Manager_App.py for further guidance.

## Future Work
I believe this project could be expanded by enhancing organization features. I don't plan on launching this program after this course, but if I did I would focus on creating better ways to organize the information in the lists. I would also consider a search feature for whent he list gets too long.

