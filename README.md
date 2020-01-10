# cashcog
Expenses Management Application. The API streams expenses data, temporarily stores it in Kafka, and then validates and loads it into the database.
A user can query all loaded expenses, fetch a single expense, filter based on provided parameters, or update a single expense. 

## How to install locally
1. Create a local folder and then navigate inside it.
2. Open a terminal in this location and then initialize git using `git init`
3. Clone the online repository using the following command `git clone https://github.com/JumaKahiga/cashcog.git`
4. Create a virtual environment using the following command `python3 -m venv cashcog_env`
5. Activate the virtual environment using `source cashcog_env/bin/activate`
6. Navigate inside the project using `cd lms-lectures` and then install required modules using `pip install -r requirements.txt`
7. Create a `.env` file following the format outlined in the `env_example` file.
8. Setup and start Kafka and Zookeper using the following [tutorial](https://kafka.apache.org/quickstart)
9. Make sure to change the `Bootstrap_Servers` in `utilities/kafka_functions.py` and `utilities/load_data.py` to `localhost:9092`
9. On Postman, Insomnia, or your preferred API client, visit the endpoints listed in the Endpoints section below.

## How to run on Docker
1. Create a local folder and then navigate inside it.
2. Open a terminal in this location and then initialize git using `git init`
3. Clone the online repository using the following command `git clone https://github.com/JumaKahiga/cashcog.git`
4. Create a virtual environment using the following command `python3 -m venv cashcog_env`
5. Activate the virtual environment using `source cashcog_env/bin/activate`
6. Navigate inside the project using `cd lms-lectures`
7. Create a `.env` file following the format outlined in the `env_example` file.
8. Install Docker using the packages and instructions provided [here](https://docs.docker.com/v17.09/engine/installation/)
9. Build the app's Docker containers using `make install`. If successful, you will see API server running on your terminal. Please note that this build automatically loads seed data into the database. 
10. On Postman, Insomnia, or your preferred API client, visit the endpoints listed in the Endpoints section below.


## Endpoints
NB: This is a GraphQL API and thus there is only one endpoint i.e. `http://localhost:5000/api`

### Mutation example
1. Update expense:
	```
	mutation{updateExpense(
	  uuid: "ananyyu178", approved: false){
	    expense{
	      uuid
	      description
	      createdAt
	      amount
	      currency
	      approved
	    }
	    message
	}}
	```

### Queries examples
1. Query all expenses
	```
	query{expenses{
	  uuid
	  description
	  createdAt
	  amount
	  currency
	  approved
	}}
	```

2. Query a single expense
	```
	query{expense(uuid: "0f98af45-a429-4ce3-9c27-d67f0aa45e81b"){
	    uuid
	    description
	    createdAt
	    amount
	    currency
	    approved
	}}
	```

3. Filter expenses
	```
	query{filterExpenses(employeeId: "ff0e8a22-3e37-4c78-90fe-7b990f5c05b0"){
	  edges{
	    node{
	      uuid
	      description
	      createdAt
	      amount
	      currency
	    }
	  }
	}
	}
	```
