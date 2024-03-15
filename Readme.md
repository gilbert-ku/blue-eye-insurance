# Blue Eye Insurance Agency API Documentation
Introduction
Blue Eye Insurance Agency (BEIA) API is designed to assist developers in creating applications that facilitate insurance agents in receiving client information through field forms. It provides an admin authentication mechanism to help agents manage their applications securely. The API is built using Python Flask, RESTful API principles, Blueprint for modular design, and JWT for authentication.

### Authentication
BEIA API uses JWT (JSON Web Token) for authentication. Administrators must log in to manage the application. Passwords are hashed using Werkzeug for security. Tokens expire after 2 hours to ensure security.

### Endpoints
The endpoints of the BEIA API include URLs and HTTP methods (GET, POST, DELETE). POST requests for receiving client form feedback do not require authentication, while other endpoints require authentication and a valid token to operate. Administrators can retrieve or delete all responses or responses by ID.

### Request and Response
Incoming data is verified using parsers, and standard Flask request objects are utilized. Responses are formatted as JSON objects using Flask's jsonify method. Additionally, the datetime library is used to handle date and time conversions.

### Error Handling
Error handling is implemented using try-except blocks, ensuring graceful handling of errors and rollback functions where necessary.

### Folder Structure
The folder structure of the BEIA API is organized as follows:
![Screenshot from 2024-03-15 12-41-34](https://github.com/gilbert-ku/blue-eye-insurance-backed/assets/125896467/9ec17304-71db-45d8-9c79-cdbc02a331be)

### Installation and Setup
To set up and run the BEIA API locally, follow these steps:

### Clone the repository.
Navigate to the project directory.
##### Install dependencies using pipenv: 
pipenv install.
##### Set up the database migrations: 
flask db init, flask db migrate, flask db upgrade.
##### Run the application: 
python run.py.
##### Usage
To use the BEIA API, make HTTP requests to the appropriate endpoints using valid authentication tokens where required. Refer to the API documentation for detailed endpoint descriptions and usage instructions.

### License
This project is licensed under the MIT License.
Copyright (c) [2024]

Permission is at this moment granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.



Contact
For inquiries, suggestions, or support, please contact 
#### [gilbert45ku@gmail.com].