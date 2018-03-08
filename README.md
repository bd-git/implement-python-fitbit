# implement-python-fitbit
This is a Quick implementation to get started with the Python-Fitbit API on Ubuntu Server using a virtual environment

 1) cd to the directory you want to compile in
        cd ~/
        git clone https://github.com/orcasgit/python-fitbit
        git clone https://github.com/bd-git/implement-python-fitbit/
   
   2) Register a new Fitbit App, https://dev.fitbit.com/apps/new 
        --Make sure to use Type: "Personal" and set CallbackURL to http://127.0.0.1:8080/
   
   3) Make a virtual environment if needed (recommended), then activate:
        mkdir ~/envs (create folder for envs, optional)
        python3 -m venv ~/envs/fitbit (make "fitbit" virtual environment, creates a folder "fitbit" in ~/envs/)
        source ~/envs/fitbit/bin/activate (activate your environment)
    
   4) Move implement.py to the python-fitbit folder, then work from there
        cp ~/implement-python-fitbit/implement.py ~/python-fitbit/implement.py
        cd ~/python-fitbit
        pip install --upgrade pip
        pip install -r requirements/base.txt
        pip install -r requirements/dev.txt
        sudo apt-get install elinks (required if headless ubuntu server, unecessary if using the implement-p-f requirements)
        
   5) modify ~/python-fitbit/implement.py to include your client_id and client_secret for first run
   
   6) Run: > python3 ~/python-fitbit/implement.py
   
   7) Example Program:
   
>>>   from implement import load_client
>>>
>>>   fb = load_client()
>>>   s=fb.sleep(date='today')['sleep'][0]
>>>   print(s)
>>>

