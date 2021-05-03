import pandas as pd
import read_worksheet as sheets

data = sheets.worksheet.get_all_records()
dfWorksheet = pd.DataFrame(data)

dfWorksheet.head()git 