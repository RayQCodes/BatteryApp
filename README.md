Battery Telemetry API
A Flask REST API for Battery Temperature & Utility Endpoints

Overview
This is a simple Flask REST API that provides mock battery telemetry data, date retrieval, and basic math operations.
It’s designed as a lightweight backend service for testing REST API development and integration.

## 🎥 Demo Video: Project Tutorial

Check out this quick 2-minute walkthrough of how the project works!

[![Watch the video](https://img.youtube.com/vi/1od0hNYNNhE/0.jpg)](https://www.youtube.com/watch?v=1od0hNYNNhE)

> ▶️ Click the image above to watch on YouTube  
> Duration: ~2 minutes  
> Covers: setup, core features, and a live demo


Features
Battery Temperature API – Retrieve mock temperature readings for a given battery ID.

Math Endpoints – Addition and subtraction endpoints for quick testing.

Date Endpoint – Get the current server date/time.

Endpoints
Method	Endpoint	Description	Example Response
GET	/api/batteries/<battery_id>	Retrieve battery temperature by ID	[{ "battery_id": "100", "battery_type": "temp", "battery_temperature": "42" }]
GET	/num/<int:x>_<int:y>	Add two numbers	["total is", 7]
GET	/<int:x>&<int:y>	Subtract two numbers	{ "total Subtraction": 3 }
GET	/date	Get current server date/time	"2025-08-04T12:34:56"

Installation & Setup
1. Navigate to your project folder

cd flaskbatteryproject
2. (Optional) Create a virtual environment


python -m venv venv
# Activate on Mac/Linux
source venv/bin/activate
# Activate on Windows
venv\Scripts\activate
3. Install dependencies

pip install -r requirements.txt
4. Run the API

python app.py
This will start the API on http://0.0.0.0:8080 (accessible at http://localhost:8080 in your browser).

Example Usage
# Get battery temperature for battery ID 100
curl http://localhost:8080/api/batteries/100

# Add two numbers
curl http://localhost:8080/num/3_4

# Subtract two numbers
curl http://localhost:8080/5&2

# Get server date
curl http://localhost:8080/date


Technologies Used
Python 3
Flask
Flask-RESTful
