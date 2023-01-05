# python3 -m pip install --upgrade pip
# pip install oauth2client
# pip install google-api-python-client   (this vs gspread)
# pip install gspread

from oauth2client.service_account import ServiceAccountCredentials
import gspread

scope = ['https://www.googleapis.com/auth/spreadsheets',
		'https://www.googleapis.com/auth/drive']
# scope = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive.file'
#      	'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('database-standbyclub.json', scope)
client = gspread.authorize(creds)

python_test = client.open("StandByClub",).sheet1
#python_test1 = client.open("StandByClub",).worksheet("test0")

first_line = ["id", "order", "payment", "check"]
for i in range(1, len(first_line)+1):
    python_test.update_cell(1, i, first_line[i-1])
#
