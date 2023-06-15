
## Deployment Steps
These are simple steps will help you to deploy the project with docker.

### Step 1: Clone the repository
If you haven't cloned the repo, clone it then move to the repo folder.
```shell
git clone https://github.com/MLBenchPvtLtd/web_novel_django.git
```
then
`cd web_novel_django`

### Step 2: Setup environment
You need to create virtual environment 
```shell
python -m venv venv
```
and activate in using 
```shell
venv\Scripts\activate
```

### Step 3: Install requirements
go to src folder using `cd src` and run command
```shell
pip install -r requirments.txt
```

### Step 4: Apply migrations
Apply migration using following command
```shell
Python manage.py migrate
```

### Step 5: Run Project
run the project using following command
```
Python manage.py runserver
```
## Or Using docker
```shell
cd deploy\live\
```
and 
```shell
docker-compose build
docker-compose up -d 
```

