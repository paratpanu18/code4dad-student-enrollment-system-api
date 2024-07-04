# code4dad-student-enrollment-system-api


### Overview
This repository hosts the API for a comprehensive Object-Oriented Programming project developed by the 'code4dad' group using Python FastAPI.

### Project Inspiration
The 'Student Enrollment System API' is inspired by the registration system at King Mongkut's Institute of Technology Ladkrabang (KMITL), which lacks user-friendliness. Our goal is to enhance the user experience through this project.

### Features
The API provides the following functionalities:
-   Enroll students in courses
-   Drop students from courses
-   Change course sections
-   Additional features to improve the enrollment process

### User Roles
The system supports three primary user roles:

1.  **Student**:
    -   Ability to enroll in and drop courses
    -   View and manage their current course enrollments
    -   Request section changes

2.  **Teacher**:
    -   Manage course sections and student enrollments
    -   Approve or deny student section change requests
    -   View enrollment statistics and reports for their courses

3.  **Admin**:
    -   Oversee the entire enrollment system
    -   Manage users (students, teachers) and course offerings
    -   Ensure the smooth operation of the system and address any issues

## Installation
The project can be easily installed using Docker

1. Build docker image.
```bash
$ docker build -t <docker-image-name> .
```

2. Start Docker
```bash
$ docker run -d --name <container-name> -p 8088:8088 <docker-image-name>
```
> You can change the port as you want to.

## Usage
After start a Docker Container and Forwarding container's port, visit the following URL to checkout a docs.
```
localhost:8088/docs
```
> Protocol may require for some browser.

In case you want to try our project with better experience, you may visit Frontend source code [here](https://github.com/Pipatpong-P23/code4dad-student-enrollment-system-frontend).

## Contributor
As the Head Backend Developer, I want to extend a big thank you and my best wishes to all the contributors who have put in so much time and effort into this project.

| **No.** 	| **Name** 	|
|:---:	|:---:	|
| 1 	| Paratpanu Pechsaman 	|
| 2 	| Pipatpong Pnapruake 	|
| 3 	| Prompipat Thongtub 	|
| 4 	| Pearapat Kumsing 	|