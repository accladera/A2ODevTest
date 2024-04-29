
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



## Running the Project

Below are the steps to run both the backend and frontend.


### Django REST Framework Backend

Make sure you have Python3 and pip installed on your system.
* **Install Python3 and pip**:
   Make sure you have Python3 and pip installed on your system. You can download and install Python from the official website if you haven't already.

* **Navigate to the project directory**:
   Go to the `a2oDevBack/` directory where your Django project is located.

* **Create a virtual environment**:
   Inside the project directory, create a virtual environment. You can name it `venv` or anything you prefer:
   ```
   virtualenv venv
   ```

* **Activate the virtual environment**:
   Activate the virtual environment. The commands might vary depending on your operating system:
   - On Unix-based systems (Linux or macOS):
     ```
     source venv/bin/activate
     ```
   - On Windows:
     ```
     venv\Scripts\activate
     ```

* Install project dependencies by running the following command:

   ```
   pip install -r requirements.txt
   ```

* Apply database migrations by running the following command:

   ```
   python manage.py migrate
   ```

* Start the Django development server by running the following command:

   ```
   python manage.py runserver 8000
   ```

   The backend will be available at `http://localhost:8000`.

### React Frontend

Make sure you have Node.js and npm installed on your system.
* Navigate to the `a2oDev/` directory.
* Install project dependencies by running the following command:

   ```
   npm install
   ```

* Start the React development server by running the following command:

   ```
   npm start
   ```

   The frontend will be available at `http://localhost:3000`.

### Front End Web App

This project is built using the following technologies:

- **React:** Utilized as the primary JavaScript library for building the user interface.
- **react-router-dom:** Employed for handling navigation within the application.
- **Fetch API:** Used for asynchronous communication with the server, enabling AJAX requests.

### Back End Web App

This project is built using the following technologies:

- **Django:** Utilized as the primary framework for backend development.
- **Django Rest Framework (DRF):** Employed for building powerful and flexible RESTful APIs in Django.
- **corsheaders** Used to enable Cross-Origin Resource Sharing (CORS) handling in Django.
### Additional Notes

Ensure you have the following installed on your machine before running the above commands:
- Node.js version 20.11.1
- npm version 10.2.4
- python version python 3.9

### Feedback and Contact
Your feedback is valuable to me. If you have any questions, suggestions, or would like to discuss this project further, feel free to reach out to me at accladera@gmail.com

Thank you for taking the time to review my submission!