from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
import os.path

# Define scopes
SCOPES = ["https://www.googleapis.com/auth/gmail.readonly"]

# Authenticate using OAuth 2.0
creds = None
if os.path.exists("token.json"):
    creds = Credentials.from_authorized_user_file("token.json", SCOPES)
if not creds or not creds.valid:
    if creds and creds.expired and creds.refresh_token:
        creds.refresh(Request())
    else:
        flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
        creds = flow.run_local_server(port=0)
    with open("token.json", "w") as token:
        token.write(creds.to_json())

# Build the Gmail API service
gmail_service = build("gmail", "v1", credentials=creds)

# Fetch recent emails
try:
    results = gmail_service.users().messages().list(userId="me", maxResults=5).execute()
    messages = results.get("messages", [])

    if not messages:
        print("No messages found.")
    else:
        print("Recent emails:")
        for msg in messages:
            msg_data = gmail_service.users().messages().get(userId="me", id=msg["id"]).execute()
            print(f"Snippet: {msg_data['snippet']}")
except Exception as e:
    print(f"An error occurred: {e}")