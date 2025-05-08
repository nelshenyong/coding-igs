import gspread
from oauth2client.service_account import ServiceAccountCredentials
import logging
import os

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def initialize_google_sheets():
    try:
        credentials_path = "credentials/thinking-window-456322-c7-0aa0721afcf6.json"
        if not os.path.exists(credentials_path):
            logger.error(f"Credentials file not found at: {credentials_path}")
            return None

        scope = ["https://spreadsheets.google.com/feeds", 
                "https://www.googleapis.com/auth/drive",
                "https://www.googleapis.com/auth/spreadsheets"]
        
        logger.info("Initializing Google Sheets connection...")
        
        creds = ServiceAccountCredentials.from_json_keyfile_name(
            credentials_path, 
            scope
        )
        client = gspread.authorize(creds)
        
        spreadsheet_name = "gspread-python-informatika11-sr-anas"
        try:
            spreadsheet = client.open(spreadsheet_name)
            logger.info(f"Successfully opened spreadsheet: {spreadsheet_name}")
        except gspread.SpreadsheetNotFound:
            logger.error(f"Spreadsheet not found: {spreadsheet_name}")
            return None
            
        sheet = spreadsheet.sheet1
        logger.info("Successfully accessed worksheet")
        
        headers = ["ID", "Name", "Age", "Games Played", "Highest Score", "Lowest Score", "Current Score"]
        if not sheet.row_values(1):
            logger.info("Adding headers to the sheet")
            sheet.append_row(headers)
        
        return sheet
    except Exception as e:
        logger.error(f"Error initializing Google Sheets: {str(e)}")
        return None

def find_player_row(sheet, player_id):
    """Find the row number for a given player ID."""
    try:
        all_values = sheet.get_all_values()
        for i, row in enumerate(all_values[1:], start=2):  # Skip header row
            if row[0] == str(player_id):
                return i
        return None
    except Exception as e:
        logger.error(f"Error finding player row: {str(e)}")
        return None

def update_player_row(sheet, player):
    """Update a player's row in the sheet."""
    try:
        row_num = find_player_row(sheet, player.id)
        if row_num:
            updated_row = [
                player.id,
                player.name,
                player.age,
                player.games_played,
                player.highest_score,
                player.lowest_score,
                player.current_score
            ]
            sheet.update(f'A{row_num}:G{row_num}', [updated_row])
            logger.info(f"Successfully updated player {player.name} in Google Sheets")
            return True
        return False
    except Exception as e:
        logger.error(f"Error updating player row: {str(e)}")
        return False

def delete_player_row(sheet, player_id):
    """Delete a player's row from the sheet."""
    try:
        row_num = find_player_row(sheet, player_id)
        if row_num:
            sheet.delete_rows(row_num)
            logger.info(f"Successfully deleted player ID {player_id} from Google Sheets")
            return True
        return False
    except Exception as e:
        logger.error(f"Error deleting player row: {str(e)}")
        return False

def add_player_row(sheet, player):
    """Add a new player row to the sheet."""
    try:
        row = [
            player.id,
            player.name,
            player.age,
            player.games_played,
            player.highest_score,
            player.lowest_score,
            player.current_score
        ]
        sheet.append_row(row)
        logger.info(f"Successfully added player {player.name} to Google Sheets")
        return True
    except Exception as e:
        logger.error(f"Error adding player row: {str(e)}")
        return False

sheet = initialize_google_sheets()
if sheet is None:
    logger.error("Failed to initialize Google Sheets connection")
else:
    logger.info("Google Sheets connection initialized successfully")
