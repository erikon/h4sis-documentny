# h4sis-documentny

Hack For Social Good Project

**Python 3.0 or higher required**

* Install requirements: `pip install -r requirements.txt`
    - Recommended to use a virtual environment 
* To Start local server: `python run.py`
    - Server should start on `http://localhost:8080/`
* Serve on twilio: `twilio phone-numbers:update "+<Insert Phone Number Here>" --sms-url="<localhost link>"`
    - Localhost link to specific API endpoint: `http://localhost:8080/sms` 
* Send a text to `<phone number>` querying for 'Trade Name' (Company/Business Name)
