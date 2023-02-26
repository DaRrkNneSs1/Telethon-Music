import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "28117970"))
    API_HASH = os.environ.get("API_HASH", "2bbe41e0345f95848c36b726954b6732")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5834280033:AAHT9x1Bd99bn8ibPFZ-lXoy5q8IkJgtmBQ")
    STRING_SESSION = os.environ.get("STRING_SESSION", "1BJWap1wBu7tFTvRXwcUJ8cDP1LLrKTfHwibHuCvbQRNwrXTwb0yoASIWxRVaYxeol3s_Ok9MYhRZcfrhWh7hMpktXIGibK7ymEyxVBfBWw4F5g7hoB7xwnjYxYtZt0jaWf6H3n2F3zFxZtB5gzQA-wFNtJ4HsQSIc8rV0L3z6fQm9KVBcjJIUlt186Lz69uSasuEAu2tHihkzqqvSAgKdSBtk0lMdc84kIhuD1tAnQxYOWhddEZohqU6e7wQkOv_BvVIKhnMTuonluTUHRYR2Xtcy8OAKiIKMz0KYYj4Ksv_gW2jR69YcAlJsM8ixPC2ad2dB8gPs2pIkLIdRsy6SXGI1hh1fbk=")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "azao1_bot")
    SUPPORT = os.environ.get("SUPPORT", "SI_MI1") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "SI_M1I") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://edit.telegra.ph/auth/ddADHFgjnyQvlzFvbXlqi4PisR2SbocoBM1hrfAOMp")
    CMD_IMG = os.environ.get("CMD_IMG", "https://edit.telegra.ph/auth/ddADHFgjnyQvlzFvbXlqi4PisR2SbocoBM1hrfAOMp")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "830359032")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"
