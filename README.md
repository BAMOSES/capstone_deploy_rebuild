# PitStopPro

PitStopPro is a business management application for an auto repair company. In this application, users will be able to track and manage inventory, create and forward invoices, view financial statements, manage employee information and payroll, and much more.

## Style Guide

https://google.github.io/styleguide/pyguide.html

## External Requirements

1. Install python - To install python go to https://python.org/download/
2. Open command prompt - check make sure that python was downloaded correctly by running ‘python –version’ in the command window
3. Install pip - in the command prompt, execute the command ‘easy_install pip’ 
4. Install Django- after installing pip you can now use it in the command prompt to download Django by typing the command ‘pip install django’

## Setup

1. After cloning the repository, you must create a virtual environment. To do this on Windows, run ‘py -3 -m venv .venv’ then ‘.venv\scripts\activate
2. To start the app run ‘python manage.py startapp <appname>

## Running
 Specify the commands for a developer to run the app from the cloned repo. 

Once you have cloned the repo and setup your virtual environment ,ensure you have navigated to the outside PitStopPro directory , and you will be able to build and run the app using the following command:

python manage.py runserver

From here the build will output the active link the app is running at ,which you can follow to see the views of the app.

## Deployment (UNIX)
Prerequisites:
Ensure you have access to an Ubuntu server.
For production usage, secure a domain name.
1. Install Essential Software:
Refresh your system's package list using sudo apt update.
Obtain essential tools: Python3, pip, Nginx, and other necessary utilities.
2. Create a Virtual Environment:
Designate a directory for PitStopPro on the server.
Set up and activate a Python virtual environment within this directory.
3. Get the PitStopPro Code:
Clone the PitStopPro project from its GitHub repository to your designated directory.
4. Configure Django Settings:
Deactivate the DEBUG mode for safety.
Add your domain or server IP to ALLOWED_HOSTS.
Since you're using SQLite, the default DATABASES setting in a new Django project will already be configured for SQLite. Ensure it looks similar to:

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / "db.sqlite3",
    }
}

5. Update the Database:
Execute Django's migrate command to create the SQLite database and implement database migrations.
6. Manage Static and Media Files:
Adjust settings for proper handling of static and media files.
Use the collectstatic command to assemble static assets.
7. Set Up Gunicorn:
Obtain Gunicorn, our chosen WSGI HTTP server.
Test Gunicorn with the PitStopPro application.
If successful, halt Gunicorn for now.
8. Automate Gunicorn with Systemd:
Craft a Gunicorn systemd service file. This ensures PitStopPro auto-starts on boot and can recover from failures.
Activate the Gunicorn service and set it to auto-start on system boot.
9. Integrate with Nginx:
Create an Nginx configuration tailored for PitStopPro.
Set rules to forward web requests to Gunicorn and to deliver static and media files.
Enable this configuration, validate it, then restart Nginx.
10. Enhance Security with Let's Encrypt (Recommended):
Install the Certbot utility.
Secure a complimentary SSL certificate from Let's Encrypt using Certbot.
Update Nginx settings to leverage this SSL certificate.

## Deployment (macOS)
Prerequisites:
Ensure you have access to a macOS machine.
For production usage, secure a domain name. (Keep in mind deploying on macOS for production isn't standard practice.)
1. Install Essential Software:
If not already installed, get Homebrew from https://brew.sh/.
Use Homebrew to obtain essential tools: brew install python3 nginx.
2. Create a Virtual Environment:
Designate a directory for PitStopPro on your machine.
Navigate to this directory in Terminal.
Set up and activate a Python virtual environment within this directory using:

python3 -m venv <venv_name>
source <venv_name>/bin/activate

3. Get the PitStopPro Code:
Clone the PitStopPro project from its GitHub repository to your designated directory.
4. Configure Django Settings:
Deactivate the DEBUG mode for safety.
Add your domain or localhost to ALLOWED_HOSTS.
Ensure the DATABASES setting is configured for SQLite (similar to the previous Ubuntu guide).
5. Update the Database:
Execute Django's migrate command to create the SQLite database and apply migrations.
6. Manage Static and Media Files:
Adjust settings for proper handling of static and media files.
Use the collectstatic command to assemble static assets.
7. Set Up Gunicorn:
Install Gunicorn with pip: pip install gunicorn.
Test Gunicorn with the PitStopPro application.
If successful, halt Gunicorn for the moment.
8. Integrate with Nginx:
Modify the Nginx configuration, usually found at /usr/local/etc/nginx/nginx.conf, to work with PitStopPro.
Ensure the configuration is set to proxy web requests to Gunicorn and to serve static and media files.
Restart Nginx: sudo nginx -s reload.

## Deployment (Windows)
Prerequisites:
Ensure you have access to a Windows machine.
For production usage, secure a domain name. (However, deploying on Windows for production isn't standard practice.)
1. Install Essential Software:
Download and install Python from https://www.python.org/downloads/windows/. Ensure you add Python to the system PATH during installation.
Install Nginx for Windows from http://nginx.org/en/docs/windows.html.
2. Create a Virtual Environment:
Designate a directory for PitStopPro on your computer.
Navigate to this directory using Command Prompt.
Set up and activate a Python virtual environment within this directory using:

python -m venv <venv_name>
<venv_name>\Scripts\activate

3. Get the PitStopPro Code:
Clone the PitStopPro project from its GitHub repository to your designated directory.
4. Configure Django Settings:
Deactivate the DEBUG mode for safety.
Add your domain or localhost to ALLOWED_HOSTS.
Ensure the DATABASES setting is configured for SQLite.
5. Update the Database:
Execute Django's migrate command to create the SQLite database and apply migrations.
6. Manage Static and Media Files:
Adjust settings for proper handling of static and media files.
Use the collectstatic command to assemble static assets.
7. Set Up Gunicorn:
Since Gunicorn doesn't natively support Windows, you can use the Waitress server instead. Install it with pip:

pip install waitress
Test Waitress with the PitStopPro application.

8. Integrate with Nginx:
Modify the Nginx configuration (found in the directory where you installed Nginx) to work with PitStopPro.
Ensure the configuration is set to proxy web requests to Waitress and to serve static and media files.
Restart Nginx.

## Testing 
### Employees/tests.py
setUp Method:
   - The setUp method is called before each test case. It's used to set up any necessary data or configurations needed for the tests. In this case, it creates sample instances of Employee and Payroll models, providing a consistent starting point for the tests.

Testing Forms:
  - The test_employee_form and test_payroll_form methods are testing the functionality of the EmployeeForm and PayrollForm, respectively.
  - They create instances of the forms with specific data and check if the forms are valid. These tests help ensure that the forms handle input data correctly and validate it according to the defined model.

Testing Views:
  - The test_employee_detail_view and test_payroll_detail_view methods test the behavior of specific views (employee_detail and payroll_detail).
  - They use the Django test client to simulate HTTP requests to these views and check if the responses are as expected.

Assertions and Checking Response Content:
  - The self.assertContains method is used to check if a specific content (e.g., HTML tags, text) is present in the HTTP response.
  - It's important to use this method to verify that the views render the expected content, ensuring that the web application behaves correctly.

Running Tests:
  - The python manage.py test Employees.tests command is used to run the tests for the Employees app. This command discovers and runs all tests in the specified module (tests.py).

Test Output:
  - The output of the test run indicates the status of each test. The OK at the end means that all tests passed successfully.

### Invoices/tests.py
 - Will test the invoicing page of the application.
 - To use:
   1. Activate the environment using env/Scripts/activate.
   2. Add selenium and pytest to the environment using pip install.
   3. Enter pytest Invoicing/tests.py.
   4. The test should run automatically.
 - Output:
   - The output of the test run indicates the status of each test.

# Authors

Danai Angelidis - danaia@email.sc.edu

Thomas Ferguson - thomaslf@email.sc.edu

Will Columbia - columbiw@email.sc.edu

Blaise Moses - bamoses@email.sc.edu

