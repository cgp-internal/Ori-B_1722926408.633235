FastAPI Project
================

This is a basic FastAPI project.

 Installation and Running
-------------------------

### Install dependencies

Run the following command in your terminal:

```
bash run.sh
```

This script will install the required dependencies listed in `requirements.txt` and start the FastAPI server with Uvicorn.

### Access the API

Once the server is running, you can access the API by navigating to `http://localhost:8000/` in your web browser.

### Endpoints

Currently, there is only one endpoint available:

* `/hello`: Returns a static "hello world" message.

To access this endpoint, navigate to `http://localhost:8000/hello` in your web browser.

### Project Structure

The project structure is as follows:

* `main.py`: The entry point of the application.
* `models/`: Directory for database models.
* `routes/`: Directory for API routes.
* `routes/hello.py`: Defines the `/hello` endpoint.
* `requirements.txt`: Lists project dependencies.
* `run.sh`: Bash script to install dependencies and start the server.
* `.gitignore`: Lists files and directories to ignore in version control.