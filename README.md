This project uses Flask and Postgresql to display an HTML of unique fruits and allows you to insert an item
## Group Members
Bryan Bridge




## Quick Start
### Local Test Setup
First, we need to install a Python 3 virtual environment with:
```
sudo apt-get install python3-venv
```

Create a virtual environment:
```
python3 -m venv python_venv
```

You need to activate the virtual environment when you want to use it:
```
source python_venv/bin/activate
```

To fufil all the requirements for the python server, you need to run:
```
pip3 install -r requirements.txt
```

Then you can start the server with:
```
python3 main.py
```
### Running the App
To access this Flask server you can follow this address in system browser:
```
https://127.0.0.1:5000/api/unique
```

Then you can either follow the provided hyperlink in that html or follow this address:
```
https://127.0.0.1:5000/api/update_basket_a
```
You can return to the /api/unique page. 
After returning, you should now see the new fruit added to basket_a and the unique fruits table. 
If already updated, the program will produce an error and let you return to home.


