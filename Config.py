import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "28117970"))
    API_HASH = os.environ.get("API_HASH", "2bbe41e0345f95848c36b726954b6732")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5834280033:AAHT9x1Bd99bn8ibPFZ-lXoy5q8IkJgtmBQ")
    STRING_SESSION = os.environ.get("STRING_SESSION", "BACqpG3Y2cyE6MG3ctdb51pVrv_G2TuLDnw4Z6zH1bIOwgEIVlq3o1pxnp7ODxUwccxwSNUahsdrJVKtpOzv2aLLHMan8wvaE7vDygMlP4VjVFSTA1gLdich_Skxz8I3ntJ6id6H-hrkEeZL4RG_IWQXD966jQkj9O6G7TvGHbyyi7auYJrAos_qN-orFMO8ZlvEairb-cBbI4iHH8gco4OR-m_p501O9nPZlJJj93krzcnD-FygRxddCLnDZ6NyedDIbJs_6dafROCfqM8vmrOz1QzewvMAojdFP7LKIPAaLlqvn9WJbyp9OAc2Ql9zLhkA847H4ZlCfqoSaPVMni_DAAAAAUkg2OQA")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", None)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "azao1_bot")
    SUPPORT = os.environ.get("SUPPORT", "RQ_V0") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "DL_R3") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://edit.telegra.ph/auth/ddADHFgjnyQvlzFvbXlqi4PisR2SbocoBM1hrfAOMp")
    CMD_IMG = os.environ.get("CMD_IMG", "https://edit.telegra.ph/auth/ddADHFgjnyQvlzFvbXlqi4PisR2SbocoBM1hrfAOMp")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "830359032")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"
