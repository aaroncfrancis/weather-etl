<h1>ETL Weather Project</h1>

<h2>Setup</h2>
This project is an ETL (Extract, Transform, Load) project that involves extracting weather data from an API for a list of cities and their country codes, transforming the data using pandas, and loading it into a MySQL database hosted on AWS RDS. The project is written in Python and utilizes various libraries such as pandas, requests, json, datetime, MySQL, AWS, csv, and sqlalchemy.

<h2>Extract</h2>
The data is extracted from a weather API for a list of cities and their country codes using the provided API, libraries, and Python's requests module. The extracted data is in raw format and contains information such as temperature, humidity, weather condition, and other relevant weather data.

<h2>Transform</h2>
The extracted data is transformed using pandas, a popular data manipulation library in Python. The transformation involves cleaning the raw data, adding datetime in UTC format, and performing any necessary data formatting or calculations to prepare the data for loading into the MySQL database.

<h2>Load</h2>
The extracted data is loaded into the MySQL database hosted on AWS RDS using SQLAlchemy, a powerful Python library for working with databases. The load function appends the extracted data to the main database, allowing for continuous data ingestion as new data becomes available.

<h2>DAG Setup</h2>
The ETL process is orchestrated using a Directed Acyclic Graph (DAG) in the main.py file. The DAG includes separate tasks for extracting, transforming, and loading the data. The tasks are organized in a workflow that specifies the order in which they should be executed. Airflow could be integrated using Docker but it was not more efficient than running a scheduler.py file that will call main.py on my local machine at every time interval (t). 

<h2>Libraries Used</h2>
The project utilizes various Python libraries such as pandas for data manipulation, requests for making API calls, json for handling JSON data, datetime for working with dates and times, MySQL for connecting to the MySQL database, AWS for interacting with AWS RDS, csv for reading and writing CSV files, and sqlalchemy for interacting with the database using an ORM (Object Relational Mapping) approach.

<h2>How to Run</h2>
To run the ETL weather project, follow these steps:
<ol>
<li>
Set up an AWS RDS instance with MySQL as the database engine and note down the database connection details.
</li>
<li>
Update the configurations in the main.py file, including the API endpoint, database connection details, and scheduling options for the DAG.
</li>
<li>
Install the necessary Python libraries using pip or conda, including pandas, requests, json, datetime, MySQL, AWS, csv, and sqlalchemy.
</li>
<li>
Run the main.py file using a Python interpreter or setup the scheduler.py with your own local file path. I recommend simply running main.py for your ease of use.
</li>
<li>
</ol>

<h2>Conclusion</h2>
This ETL weather project demonstrates a comprehensive understanding of ETL development concepts and showcases the use of various Python libraries for extracting, transforming, and loading data from an API to a MySQL database hosted on AWS RDS. The project includes a DAG in Apache Airflow for orchestrating the ETL process and utilizes libraries such as pandas, requests, json, datetime, MySQL, AWS, csv, and sqlalchemy for performing the required data manipulation tasks.
