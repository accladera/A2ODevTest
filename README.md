
# Hi, I'm Carolina! 👋

## Test for Web App Developers

This is a project that includes both the backend and frontend. The backend is developed using Django REST Framework and the frontend using React.
## Project Structure

The project is structured as follows:

```
Project_Name 'A2ODevTest'/
│
├── backend 'a2oDevBack'/
│   └── app
│
└── frontend 'a2oDev'/
    ├── public/
    ├── src/
    └── ...
```

- **backend/**: Contains the backend code developed in Django REST Framework.
- **frontend/**: Contains the frontend code developed in React.

## Getting Started

To run the project locally, follow these steps:

Clone the project

```bash
  git clone https://github.com/accladera/A2ODevTest.git
```

## Prerequisites

Before you begin, make sure you have Docker installed on your machine. If you haven't installed Docker yet, please follow the [official installation instructions](https://docs.docker.com/get-docker/) for your operating system.


## Running the Project

### Running React JS Frontend 

To run the Docker container and access the React app, follow these steps:

* Pull the Docker image from Docker Hub by executing the following command:

    ```bash
    docker pull accladeram/a2odev
    ```

* Once the image is downloaded, run the container with the following command:

    ```bash
    docker run -d -it --name frontend -p 3000:3000 accladeram/a2odev
    ```

   This command will start the container in detached mode and map port 3000 of the container to port 3000 of your host machine.

* Access the React app in your web browser by navigating to the following URL:

    ```
    http://localhost:3000
    ```

   You should see the React app running inside the Docker container rendered in your web browser.

#### Stopping the Container

When you're done using the React app, you can stop the Docker container with the following command:

```bash
docker stop frontend
```

### Running Django REST Framework Backend

To run the Docker container and access the Django REST API, follow these steps:

* Pull the Docker image from Docker Hub by executing the following command:

    ```bash
    docker pull accladeram/a2odevback
    ```

* Once the image is downloaded, run the container with the following command:

    ```bash
    docker run -d -it --name backend -p 8000:8000 accladeram/a2odevback
    ```

   This command will start the container in detached mode and map port 8000 of the container to port 80000 of your host machine.

* Access the API in your web browser by navigating to the following URL:

    ```
    http://localhost:8000
    ```

## API Reference

#### Process Exercise

```http
  POST /api/exercise/process/
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `data` | `Json` | **Required**.|
| `data.index` | `integer` | Problem index.  |
| `data.input` | `string` | Problem input data |


### Feedback and Contact
Your feedback is valuable to me. If you have any questions, suggestions, or would like to discuss this project further, feel free to reach out to me at accladera@gmail.com

Thank you for taking the time to review my submission!
