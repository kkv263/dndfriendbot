import discord
import gspread
import decimal
from oauth2client.service_account import ServiceAccountCredentials
from string import ascii_lowercase


def getTiers (tiers):
    getTierArray = []
    for i in range(len(tiers)):
        if tiers[i] != "":
            getTierArray.append(i)
    getTierArray.append(len(sheet.row_values(3)) + 1)

    return getTierArray

def calculateTreasure(seconds, role):
    cp = ((seconds + 900) // 1800) / 2
    tp = .5 if cp == .5 else int(decimal.Decimal((cp / 2) * 2).quantize(0, rounding=decimal.ROUND_HALF_UP )) / 2
    gp = cp * 40
    role = role.lower()

    if role == 'journey':
      gp = cp * 120

    if role == "elite":
      tp = cp
      gp = cp * 240

    if role == "true":
      tp = cp
      gp = cp * 600

    return [cp, tp, gp]

# use creds to create a client to interact with the Google Drive API
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)

# Find a workbook by name and open the first sheet
# Make sure you use the right name here.
sheet = client.open("Magic Item Table (Xyffei Test)").sheet1
token = 'not yours'
client = discord.Client()

gameCategory = "Game Rooms"
roleArray = ['Junior', 'Journey', 'Elite', 'True']
tierArray = getTiers(sheet.row_values(2))
tpArray = sheet.row_values(3)
alphabetList = list(ascii_lowercase)

one = '1⃣'
two = '2⃣'
three = '3⃣'
four = '4⃣'


left = '⏪'
right = '⏩'

numberEmojis = ['1⃣','2⃣','3⃣','4⃣','5⃣','6⃣','7⃣','8⃣','9⃣','🔟',]

alphaEmojis = ['🇦','🇧','🇨','🇩','🇪','🇫','🇬','🇭','🇮','🇯','🇰']
# '🇱','🇲','🇳','🇴','🇵','🇶','🇷','🇸','🇹','🇺','🇻','🇼','🇽','🇾','🇿']