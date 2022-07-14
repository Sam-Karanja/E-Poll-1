# E-Poll

## Authors/Collaborators
- Florence Wangechi
- Mary Atieno
- Gladys Wambura 
- Faith Okong'o

## Description 
- This is a Simple,secure and transparent voting system. With our lives increasingly shifting online, it’s only logical that voting would transition to a digital platform, too. Common features include single-vote verification, which ensures members don’t inadvertently vote more than once; ballot tracking, which monitors the exact moment a ballot is processed; a secure network to protect the entire process from nominations to tabulation; and secret ballots, which keep ballots private. 

![image](https://user-images.githubusercontent.com/97955649/178937516-f3c5196e-f466-4ca8-896a-1a81cae65df8.png)

![image](https://user-images.githubusercontent.com/97955649/178937950-bd3ff0aa-9455-4cd4-95d3-4c5539139402.png)

## User Story
####  Voter view
* Voter can register
* Voter can login
* Voter can see available candidates on the voter dashboard
* Voter can vote his/her candidate of choice
* Voter can submit and view their ballot/voting history

####  Admin view
* Admin can Register and Login.
* Admin can add a position and a candidate.
* Admin can see the ballots and followup on the voting

## Behavior Driven Development

| Input                    | Behaviour                       | Output                                       |
| -------------------------| ------------------------------  | -------------------------------------------- |
| Voter Login              | Input the email and password               | Redirect you to the voterDashboard               |
| Admin login                    | Input the email and password           | Redirect you to the AdminDashboard                 |
| Voter can vote          | select the candidates of their choice    | cast/submit the vote                     | 
| Admin can add candidate and position      | filling a form    | The blog post will be deleted and not appear on the page                  |
| Admin can see the voting process       | gets instant results    | Ballot is casted               |
| Voter can only vote once         | voter can view their ballot    | Voter can logout   



## Technologies Used
* Python 
* Django 
* PostgreSQL 
* SQLAlchemy
* HTML5  
* CSS3
* Javascript
* Bootstrap   

## Requirements
* This program requires python3.+  installed, a guide on how to install python on various platforms can be found [here](https://www.python.org/)
* Once python is installed, install the folowing external libraries provided in the requirements.txt file using pip
* Example: 
    * **`pip install django`**


    ## Installation and Set-up
To view the app, open the live site link provided below on the README.
Here is a run through of how to set up the application:
* **Step 1** : Clone this repository using **`git clone https://github.com/FloWambui/E-Poll.git**, or downloading a ZIP file of the code.
* **Step 2** : The repository, if downloaded as a .zip file will need to be extracted to your preferred location and opened
* **Step 3** : Go to the project root directory and install the virtualenv library using pip an afterwards create a virtual environment. Run the following commands respectively:
    * **`pip install virtualenv`**
    * **`virtualenv venv`**
    * **`source venv/bin/activate`**
        * Note that you can exit the virtual environment by running the command **`deactivate`**
* **Step 4** : Go to config.py and set the SQLALCHEMY_DATABASE_URI to your own, you may use Postgres or any other SQL databse client.
* **Step 5** : Download the all dependencies in the requirements.txt using **`pip install -r requirements.txt`**
    * Create a file in your root directory called .env and store a generated SECRET key like so **`export SECRET_KEY="<your-key>"`**
    * On the same file write down the command **`python3 manage.py server`** * 
    * Open your preferred browser and view the app by opening the link **http://127.0.0.1:8000/ or run the command python3 manage.py runserver**.


## Contacts 
**florencewambui@gmail.com**
**maryatieno@gmail.com**
**gladyswahito7@gmail.com**
**okongofaith3@gmail.com**


## live link 



## License
#### [*GNU License*](LICENSE)
