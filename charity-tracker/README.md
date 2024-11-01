# KindnessCounts Charity Tracker

![Python](https://img.shields.io/badge/python-3.9-blue)
![Flask](https://img.shields.io/badge/flask-2.0.1-green)


Welcome to the **KindnessCounts** project! This web application allows users to track visitor counts while supporting various charitable causes. For every 100 visitors, a donation will be made to one of the selected causes. The application features a visually appealing interface with background images with a positive message :)

## Features
- Displays a random charity cause on each visit.
- Increments the visitor count with each page refresh.
- Showcases different causes related to education, mental health, clean water, and more.
- Vibrant and responsive design for a better user experience.

## Demo

![alt text](../Snippet.png)

## Technologies Used
- **Flask**: A lightweight WSGI web application framework in Python.
- **Redis**: Used for counting visitors and storing data.
- **HTML/CSS**: For building and styling the web pages.
- **Docker**: For containerising the application and its dependencies.

## Getting Started

### Prerequisites
- [Docker](https://www.docker.com/get-started) and Docker Compose  installed on your machine.
- Docker Compose installed (usually included with Docker installation).

### Installation
1. Clone the repository:  
   `git clone <repository-url>`  
   `cd <repository-folder>`

2. Build and run the Docker containers:  
`docker-compose up --build`

3. Open your web browser and go to http://localhost:8080 to view the application.


## Contributions

Contributions are welcome! If you have suggestions for improvements or new features, feel free to open an issue or submit a pull request.