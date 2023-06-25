# TravelGPT
Your one-stop travel buddy app build for the lazy tourists.
Build for SIA Application Challenge under the Generative AI category.

### Table of Contents
- [Introduction](#introduction)
- [Tools](#Tools)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
- [Technology Choices](#technology-choices)
- [Testing & Optimization](#testing-&-optimization)
- [Credits](#credits)

### Introduction
Currently travel guides on SIA websites are lacking in locations, with very little information on them. It is however unrealistic for SIA to be able to provide handy travel guides for every location.
As tourists, it is also very cumbersome to gather information across various sources, hence we wanted a one-stop solution for everything from itinerary recommendations to weather forecasts.
With that, we have decided to leverage on the growing trend of free to use LLMs such as chatGPT to help tourists generate recommendations and gather related information.

### Tools
 - Frontend: JavaScript, HTML, CSS
 - Backend: Python, Flask, OpenAI API, LangChain
 - Database: Redis
 - Tooling: Docker, Postman

### Project Structure
```bash
.
├── client
│   ├── images
│   ├── src
│   ├── styles
│   └── app.js
├── config
│   └── config.json # Put OpenAI API key here
├── launch
│   ├── launch.bat # For Windows
│   └── launch.sh # For Unix
└── server
    ├── database
    ├── chat
    └── main.py
```

### Getting Started
1. Clone this repository
```bash
git clone https://github.com/yeoshuheng/travel-gpt.git
```
2. Create OpenAI account and visit the [OpenAI API page](https://platform.openai.com/overview).
3. Create a API key *Settings>User>API Key* and copy it.
4. Go into the *travel-gpt/config/config.json* and add your API Key.
5. Install Docker
6. Run Docker
7. Run application\
\
**MacOS**\
    For MacOS, you will need to first give Google Chrome Full Disk Access, you can do so by going into *System Preferences > Privacy & Security > Full Disk Access* and adding Google Chrome.\
    \
    Afterwards, cd into the project directory's launch file and run:
    ```bash
    bash launch.sh
    ```
    The application should open, wait for a minute for the docker build to complete and you can now enjoy the app.\
    \
**Windows**\
    For Windows, cd into the project directory's launch file and run:
    ```powershell
    start launch.bat
    ```
    The application should open, wait for a minute for the docker build to complete and you can now enjoy the app.\
    \
    **Manual**\
    You can also manually start the app. Cd into the project directory and run:
    ```bash
    docker compose up --build
    ```
    Afterwards, you can just open *./client/src/index.html* and enjoy the application.

### Technology Choices
- While LangChain is available on both JS and Python, we eventually decided to adopt the Python version because Python is traditionally used to work with data, hence we felt that it would provide more flexibility if we eventually decide to add more data-enabled features in the future or if we decide to use a different model and finetune it with transfer learning. 
- Since we were already working in Python, we also decided to use Flask for our backend.
- A future consideration could possibly be to shift the backend's code into [Mojo](https://www.modular.com/mojo), a pythonic language that runs with the performance of C++. Additionally, Mojo also plans to support popular Python data manipulation packages and is already supporting MatplotLib & NumPy.
- Redis is easy to set up and handles queries more efficiently than SQL. Since we do not have any complex queries within our application that requires SQL, we decided upon Redis as our caching database. however this may change as the app evolves and more functionally is developed.
- We eventually decided to Dockerize the application to ease up application deployment, be it on our local devices or in the cloud.

### Testing & Optimization
- A issue we noticed is the long loading time in between user input and querying, this is because of the need for the LLM to generate the response. We decided to optimise this by caching standard responses (eg. Description of travel location) which does not change into a Redis database.
- The API for the Flask server has been tested on Postman.

### Credits
These are some tutorials we used when setting up the application that were of amazing help.
- Salvador Villalon's FreeCodeCamp [article on building applications in Flask](https://www.freecodecamp.org/news/how-to-build-a-web-application-using-flask-and-deploy-it-to-the-cloud-3551c985e492/)
- Paul Issack's [explanation on Dockerfiles](https://www.analyticsvidhya.com/blog/2022/06/writing-dockerfile-is-simple/)
- [Official Documentation for LangChain](https://js.langchain.com/docs/)
- [Official Documentation for Docker Compose](https://docs.docker.com/compose/)
- [Official Documentation for OpenAI API](https://platform.openai.com/docs/introduction)
