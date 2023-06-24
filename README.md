# TravelGPT
Your one-stop travel buddy app build for the lazy tourists.
Build for SIA Application Challenge under the Generative AI category.

### Table of Contents
- [Introduction](#introduction)
- [Tools](#Tools)
- [Project Structure](#project-structure)
- [Getting Started](#getting-started)
- [Testing & Optimization](#testing-&-optimization)

### Introduction
Currently travel guides on SIA websites are lacking in locations, with very little information on them. It is however unrealistic for SIA to be able to provide handy travel guides for every location.
As tourists, it is also very cumbersome to gather information across various sources, hence we wanted a one-stop solution for everything from itinerary recommendations to weather forecasts.
With that, we have decided to leverage on the growing trend of free to use LLMs such as chatGPT to help tourists generate recommendations and gather related information.

### Tools
 - Frontend: JavaScript, HTML, CSS
 - Backend: Python, Flask, OpenAI API, LangChain
 - Tooling: Docker, Postman

### Project Structure
```bash
.
├── client
│   ├── images
│   ├── src
│   └── styles
└── server
    ├── database
    └── chat
```

### Getting Started
1. Create OpenAI account and visit the [OpenAI API page](https://platform.openai.com/overview).
2. Create a API key *Settings>User>API Key* and copy it.
3. Go into the *travel-gpt/config/config.json* and add your API Key.
4. Install Docker
5. Run Docker
6. Run application\
\
**MacOS**\
    For MacOS, you will need to first give Google Chrome Full Disk Access, you can do so by going into *System Preferences > Privacy & Security > Full Disk Access* and adding Google Chrome.\
    \
    Afterwards, cd into the project directory and run:
    ```bash
    launch.sh
    ```
    The application should open, wait for a minute for the docker build to complete and you can now enjoy the app.\
    \
**Windows**\
    For Windows, cd into the project directory and run:
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

### Testing & Optimization
- A issue we noticed is the long loading time in between user input and querying, this is because of the need for the LLM to generate the response. We decided to optimise this by caching standard responses (eg. Description of travel location) which does not change into a Redis database.
- The API for the Flask server has been tested on Postman.
