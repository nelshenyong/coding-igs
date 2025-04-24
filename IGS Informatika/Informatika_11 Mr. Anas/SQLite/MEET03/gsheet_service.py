from google.oauth2.credentials import Credentials
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

class GoogleSheetService:
    def __init__(self, credentials_path):
        self.credentials_path = credentials_path
        self.credentials = None
        self.service = None
        self.setup_service()

    def setup_service(self):
        try:
            self.credentials = service_account.Credentials.from_service_account_file(
                self.credentials_path, scopes=SCOPES)
            self.service = build('sheets', 'v4', credentials=self.credentials)
        except Exception as e:
            print(f"Error setting up Google Sheets service: {e}")
            raise

    def append_to_sheet(self, spreadsheet_id, range_name, values):
        try:
            body = {
                'values': values
            }
            result = self.service.spreadsheets().values().append(
                spreadsheetId=spreadsheet_id,
                range=range_name,
                valueInputOption='RAW',
                insertDataOption='INSERT_ROWS',
                body=body
            ).execute()
            return result
        except HttpError as error:
            print(f"An error occurred: {error}")
            return None

    def read_sheet(self, spreadsheet_id, range_name):
        try:
            result = self.service.spreadsheets().values().get(
                spreadsheetId=spreadsheet_id,
                range=range_name
            ).execute()
            return result.get('values', [])
        except HttpError as error:
            print(f"An error occurred: {error}")
            return None

    def update_sheet(self, spreadsheet_id, range_name, values):
        try:
            body = {
                'values': values
            }
            result = self.service.spreadsheets().values().update(
                spreadsheetId=spreadsheet_id,
                range=range_name,
                valueInputOption='RAW',
                body=body
            ).execute()
            return result
        except HttpError as error:
            print(f"An error occurred: {error}")
            return None 