from email.message import EmailMessage
from ..utils.exception_handler import ErrorMessage
from ..configs import message, app_configs
from ..schemas import ServiceResultModel
from ..schemas.Request_schema import (
    RequestSchema,
    GetRequestSchema,
    CreateRequestschema,
    VolunteerSchema
)
from sqlalchemy.orm import Session
import smtplib
from pydantic import ValidationError
from ..utils.helper import get_html_template
from datetime import datetime


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
            message = EmailMessage()
            message['from'] = app_configs.email_settings.MAIL_USERNAME
            message['to'] = app_configs.email_settings.MAIL_TO
            message['Subject'] = f"Service request from {form.company_name.capitalize()}"
            message.add_alternative(get_html_template('colauncha_mail.html', **form.model_dump()), subtype='html')
            # print(message)

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
                server.send_message(message)
                message.clear_content()

            result.data = {"message": "Request submitted successfully"}
            return result
        except (Exception, ValidationError, smtplib.SMTPException) as e:
            message.clear_content()
            result.add_error(str(e))
            print(f'Error type: {type(e)}\nError: {e}')
            raise ErrorMessage(
                message="Something went wrong with sending request", 
                status_code=500,
                detail="Error on server side"
            )

    def form_submit_company(
            self, requestform: RequestSchema,
            filename: str
        ) -> ServiceResultModel:

        result = ServiceResultModel()
        try:
            form = RequestSchema.model_validate(requestform)
            parameters = form.model_dump()
            parameters['filename'] = filename if filename else None
            parameters['current_year'] = datetime.now().strftime('%Y')
            message_company = EmailMessage()
            message_company["From"] = app_configs.email_settings.MAIL_USERNAME
            message_company["To"] = form.email
            message_company["Subject"] = "Talent request form submitted successfully"
            message_company.add_alternative(
                get_html_template('company_mail.html', **parameters),
                subtype='html'
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
                server.send_message(message_company)
                message_company.clear_content()

            result.data = {"message": "Request submitted successfully"}
            return result

        except (Exception, ValidationError, smtplib.SMTPException) as e:
            message_company.clear_content()
            result.add_error(str(e))
            print(f'Error type: {type(e)}\nError: {e}')
            raise ErrorMessage(
                message="Something went wrong with sending request", 
                status_code=500,
                detail="Error on server side"
            )
        
# Talent volunteer
    def volunteer_submit_colauncha(
            self,
            requestform: VolunteerSchema,
            attachment: bytes,
            filename: str,
            file_type: str
        ) -> ServiceResultModel:
        result = ServiceResultModel()
        try:
            form = VolunteerSchema.model_validate(requestform)
            message = EmailMessage()
            message['from'] = app_configs.email_settings.MAIL_USERNAME
            message['to'] = app_configs.email_settings.MAIL_TO
            message['Subject'] = f"Volunteer request from {form.name.capitalize()}"
            message.add_alternative(get_html_template('talent_colauncha.html', **form.model_dump()), subtype='html')
            # print(message)

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
                server.send_message(message)
                message.clear_content()

            result.data = {"message": "Request submitted successfully"}
            return result

        except (Exception, ValidationError, smtplib.SMTPException) as e:
            message.clear_content()
            result.add_error(str(e))
            print(f'Error type: {type(e)}\nError: {e}')
            raise ErrorMessage(
                message="Something went wrong with sending request", 
                status_code=500,
                detail="Error on server side"
            )

    def volunteer_submit(
            self, requestform: VolunteerSchema,
            filename: str
        ) -> ServiceResultModel:

        result = ServiceResultModel()
        try:
            form = VolunteerSchema.model_validate(requestform)
            parameters = form.model_dump()
            parameters['filename'] = filename if filename else None
            parameters['current_year'] = datetime.now().strftime('%Y')
            message_company = EmailMessage()
            message_company["From"] = app_configs.email_settings.MAIL_USERNAME
            message_company["To"] = form.email
            message_company["Subject"] = "Talent request form submitted successfully"
            message_company.add_alternative(
                get_html_template('talent_mail.html', **parameters),
                subtype='html'
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
                server.send_message(message_company)
                message_company.clear_content()

            result.data = {"message": "Request submitted successfully"}
            return result

        except (Exception, ValidationError, smtplib.SMTPException) as e:
            message_company.clear_content()
            result.add_error(str(e))
            print(f'Error type: {type(e)}\nError: {e}')
            raise ErrorMessage(
                message="Something went wrong with sending request", 
                status_code=500,
                detail="Error on server side"
            )
