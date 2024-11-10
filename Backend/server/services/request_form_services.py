from sys import stderr
from server.utils.exception_handler import ErrorMessage
from server.configs import message, app_configs
from server.schemas import RequestSchema, ServiceResultModel
import smtplib
from pydantic import ValidationError
from server.utils.helper import get_html_template


class RequestFormServices:
    def form_submit(
            self,
            requestform: RequestSchema,
            attachment: bytes,
            filename: str,
            file_type: str
        ) -> ServiceResultModel:
        result = ServiceResultModel()
        try:
            form = RequestSchema.model_validate(requestform)
            message.add_alternative(get_html_template('colauncha_mail.html', **form.model_dump()), subtype='html')
            if attachment and filename and file_type:
                message.add_attachment(
                    attachment,
                    maintype=file_type.split('/')[0],
                    subtype=file_type.split('/')[1],
                    filename=filename
                )
            with smtplib.SMTP(
                app_configs.email_settings.MAIL_SERVER,
                app_configs.email_settings.MAIL_PORT,
            ) as server:
                server.starttls()
                server.login(
                    app_configs.email_settings.MAIL_USERNAME,
                    app_configs.email_settings.MAIL_PASSWORD
                )
                print(message)
                server.send_message(message)
            result.data = {"message": "Request submitted successfully"}
            return result
        except (Exception, ValidationError, smtplib.SMTPException) as e:
            result.add_error(str(e))
            print(f'Error type: {type(e)}\nError: {e}')
            raise e
            raise ErrorMessage(
                message="Something went wrong with sending request", 
                status_code=500,
                detail="Error on server side"
            )
