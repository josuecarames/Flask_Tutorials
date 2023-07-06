# Tutorial auth: https://www.digitalocean.com/community/tutorials/how-to-add-authentication-to-your-app-with-flask-login
# Tutorial blog: https://www.digitalocean.com/community/tutorials/how-to-make-a-web-application-using-flask-in-python-3

Instructions to run the App:

1. start with creating the project directory: mkdir flask_auth_app
2. Next, navigate to the project directory: cd flask_auth_app
3. Pull request from git@github.com:josuecarames/Flask_Tutorials.git via SSH to get latest version or https://github.com/josuecarames/Flask_Tutorials.git via HTTPS
4. OPTIONAL: Create a Python environment if you don’t have one: python3 -m venv venv
5. OPTIONAL: Next, run the following command: source venv/bin/activate This command will activate the virtual environment on a Linux/macOS. If you want to run it in Windows, type in cmd "venv\Scripts\activate.bat" or in PowerShell "venv\Scripts\Activate.ps1"
6. Run the following command from the project directory to install the needed packages: pip3 install -r requirements.txt
7. In a terminal, you can set the FLASK_APP and FLASK_DEBUG values as follows: export FLASK_APP=project && export FLASK_DEBUG=1
8. Then, run in a terminal: flask run

Now, you should be able to type in a Internet browser of your choice the following to see the web application: http://localhost:5000 or alternatively http://127.0.0.1:5000