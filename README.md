# py-twilio-sms

A Twilio SMS Example with Python

## Twilio Setup 

Install the Twilio CLI:

```
brew tap twilio/brew && brew install twilio
``` 

Run `twilio login`

## Setup Environment 

Create a `.env` file with the following keys:

``` 
ACCOUNT_ID=
AUTH_TOKEN=
```

## Replying to an Incoming Message 

Configure the Twilio phone number to call the webhook URL:

```
twilio phone-numbers:update "+1XXXXXXXXXX" --sms-url="http://localhost:5000/sms"
```

_Note: create an encrypted tunnel using the 3rd-party service https://ngrok.io_
