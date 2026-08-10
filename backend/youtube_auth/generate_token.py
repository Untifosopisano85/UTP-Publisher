from google_auth_oauthlib.flow import InstalledAppFlow


SCOPES = [
    "https://www.googleapis.com/auth/youtube.upload",
    "https://www.googleapis.com/auth/youtube.readonly",
]


CLIENT_SECRETS_FILE = "youtube_auth/client_secret.json"



flow = InstalledAppFlow.from_client_secrets_file(
    CLIENT_SECRETS_FILE,
    SCOPES
)


credentials = flow.run_local_server(
    port=8080,
    access_type="offline",
    prompt="consent"
)



print("\nACCESS TOKEN:")
print(credentials.token)


print("\nREFRESH TOKEN:")
print(credentials.refresh_token)