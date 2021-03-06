# NYC Open Parking and Camera Violation Dashboard
![PARKING](https://user-images.githubusercontent.com/52837649/97363669-51f43380-1879-11eb-834f-933fe1cf5630.gif)

## Description
In this project, the NYC Open Parking and Camera Violation Dashboard, I applied what I have learned about EC2, Docker, Elasticsearch and Kibana to a real-world dataset powered by NYC Open Data. This dataset has 56.9 million rows and 19 columns. Each row is an open parking and camera violations issued in New York city traced back from 2016 to now. The columns include the violation type, the violation time, the fine amount, and the penalty amount among other violation details.

I wrote a python script that runs in docker to consume data from the Socrata Open Data API and then pushes that information into an Elasticsearch cluster provisioned via AWS.  After loading all the data into an Elasticsearch instance, I visualized and analyzed the data with Kibana. 



## Table of Contents

* [TechUsed](#TechUsed)

* [Usage](#usage) 

* [Questions](#Questions)


## TechUsed
Docker, Elasticsearch, Kibana, Python, Terminal

## Usage
Step 1: Build the docker image 
```
docker build -t bigdata1:1.0 project01/
```

Step 2: Enter into project01 folder
```
cd project01/
```

Step 3: Run the docker container 
```
docker run -v ${PWD}:/app -e DATASET_ID=“XXX” -e APP_TOKEN=“XXX” -e ES_HOST=“XXX” -e ES_USERNAME=“XXX” -e ES_PASSWORD=“XXX” bigdata1:1.0 --page_size=1000 --num_pages=1000 
```
## Questions
For questions about the project, please contact wuyaheng or directly at wuyaheng2016@gmail.com

