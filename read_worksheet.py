import gspread
from oauth2client.service_account import ServiceAccountCredentials

#Credenciais para acessar a planilha
SHEET_SALARY_ID = '1x6CROvObenzmRbypEm2cch4PvWqKrHV3wGa6BbL9G6I'
CREDENTIALS_JSON = 'puc-sheets-fb4da8a3aee2.json'

#Escopo utilizado
scope = ['https://spreadsheets.google.com/feeds']

#Autendicando
credentials = ServiceAccountCredentials.from_json_keyfile_name(CREDENTIALS_JSON, scope)
gc = gspread.authorize(credentials)
wks = gc.open_by_key(SHEET_SALARY_ID)

#Seleciona a primeira página da planilha
worksheet = wks.get_worksheet(0)
