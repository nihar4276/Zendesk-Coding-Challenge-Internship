Zendesk coding challenge submission by Nihar Rao (niharsrao@gmail.com)

HOW TO RUN:

1) Create python3.8+ virtual env
    
    ` virtualenv -p python3 <venv_name> && source <venv_name>/bin/activate`

2) Perform ` pip install -r requirements.txt` to install the dependencies

3) Set environment variables for username, subdomain and API token. The application/config.py will be using these envrionment variables and will be used in the whole application.
   
   ```
   export subdomain=https://<your_domain_name>.zendesk.com/
   export username=niharsrao@gmail.com
   export token=<your_token>
   ```

4) Run application/index.py and follow the menu options

   `python3 application/index.py`

5) Follow the steps on the application to get all tickets or a single ticket.
6) You can click on the below link to view the below under 2 minutes video to know how to use the application. 
Note: the above steps have been completed in the video.

   [video link](https://drive.google.com/file/d/1bXM-fwdr-Pzoc3sSIbshdBrssRcp3kDB/view?usp=sharing)



DESIGN:

The challenge has been done using CLI and Zendesk's official APIs have been used. The application has been implemented using SOLID design principles. 

1) Get All tickets functionality:

API used:

`GET https://<domain_name>.zendesk.com/api/v2/tickets.json?page[size]=25`

The main part of the application is getting all tickets and paging them in page sizes of 25.
This pagination has been implemented using normal python variables and the 'links' key of the tickets API response.
the 'links' object has 'next' key-value pair that gives the link of the next set of page containing the tickets.

Once we recieve the tickets, the user can select a ticket among the list to view more details about the ticket. 
This functionality is reused and is described below.

2) Get a ticket functionality:

   API used: `'GET https://<domain_name>.zendesk.com/'api/v2/tickets/{ticket_id}.json'`

   The user enters the id of the ticket he wants to view and view use the API to fetch the ticket details. If the ticket_id does not exist we return appropriate error message.
   







   
