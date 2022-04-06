# separator used by search.py, categories.py, ...
SEPARATOR = ";"

LANG            = "zh_CN" # can be en_US, fr_FR, ...
ANDROID_ID      = 'f45c95602c83de39'
GOOGLE_LOGIN    = '341965901qv@gmail.com'
GOOGLE_PASSWORD = 'he1234567890@@'
AUTH_TOKEN      = None # "yyyyyyyyy"

# force the user to edit this file
if any([each == None for each in [ANDROID_ID, GOOGLE_LOGIN, GOOGLE_PASSWORD]]):
    raise Exception("config.py not updated")

