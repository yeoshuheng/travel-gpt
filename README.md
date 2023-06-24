# TravelGPT
Your one-stop travel buddy app build for the lazy tourists.
Build for SIA Application Challenge under the Generative AI category.

### Table of Contents
- [Introduction](#introduction)
- [Tools](#Tools)
- [Project Structure](#project-structure)
- [Starting Up](#starting-up)
- [Endpoints](#endpoints)

### Introduction
Currently travel guides on SIA websites are lacking in locations, with very little information on them. It is however unrealistic for SIA to be able to provide handy travel guides for every location.
As tourists, it is also very cumbersome to gather information across various sources, hence we wanted a one-stop solution for everything from itinerary recommendations to weather forecasts.
With that, we have decided to leverage on the growing trend of free to use LLMs such as chatGPT to help tourists generate recommendations and gather related information.

### Tools
 - Frontend: JavaScript
 - Backend: Python, Flask, OpenAI API, LangChain
 - Tooling: Docker, Postman

### Project Structure
```bash
.
├── client
│   ├── backend_server
│   └── database
├── server
    ├── database
    └── chat
```

### Starting Up
1. Install Docker
2. Run and wait for docker to build and create the containers.
```bash
docker compose up --build
```

### Endpoints
Endpoint for the model server, tested on Postman.

**port_json**
```json
{
    "location" : "tokyo",
    "month" : "june",
    "day" : "5"
}
```
