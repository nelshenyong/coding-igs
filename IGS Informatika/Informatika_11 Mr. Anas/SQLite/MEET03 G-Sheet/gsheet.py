import gspread
from oauth2client.service_account import ServiceAccountCredentials
import logging
import os

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def initialize_google_sheets():
    try:
        # Check if credentials file exists
        credentials_path = "credentials/thinking-window-456322-c7-0aa0721afcf6.json"
        if not os.path.exists(credentials_path):
            logger.error(f"Credentials file not found at: {credentials_path}")
            return None

        # Tentukan scope akses Google Sheets dan Drive
        scope = ["https://spreadsheets.google.com/feeds", 
                "https://www.googleapis.com/auth/drive",
                "https://www.googleapis.com/auth/spreadsheets"]
        
        logger.info("Initializing Google Sheets connection...")
        
        # Autentikasi dengan file JSON yang sudah didownload
        creds = ServiceAccountCredentials.from_json_keyfile_name(
            credentials_path, 
            scope
        )
        client = gspread.authorize(creds)
        
        # Buka Google Sheet dengan nama yang sudah kamu buat
        spreadsheet_name = "gspread-python-informatika11-sr-anas"
        try:
            spreadsheet = client.open(spreadsheet_name)
            logger.info(f"Successfully opened spreadsheet: {spreadsheet_name}")
        except gspread.SpreadsheetNotFound:
            logger.error(f"Spreadsheet not found: {spreadsheet_name}")
            return None
            
        sheet = spreadsheet.sheet1
        logger.info("Successfully accessed worksheet")
        
        # Ensure headers exist
        headers = ["ID", "Name", "Age", "Games Played", "Highest Score", "Lowest Score", "Current Score"]
        if not sheet.row_values(1):
            logger.info("Adding headers to the sheet")
            sheet.append_row(headers)
        
        return sheet
    except Exception as e:
        logger.error(f"Error initializing Google Sheets: {str(e)}")
        return None

# Initialize the sheet object
sheet = initialize_google_sheets()
if sheet is None:
    logger.error("Failed to initialize Google Sheets connection")
else:
    logger.info("Google Sheets connection initialized successfully")
