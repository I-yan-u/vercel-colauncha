from .app_config import app_configs
from email.message import EmailMessage


message = EmailMessage()
message['from'] = app_configs.email_settings.MAIL_USERNAME
message['subject'] = 'Colauncha Request'
message['to'] = app_configs.email_settings.MAIL_TO