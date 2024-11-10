from jinja2 import Environment, FileSystemLoader, select_autoescape
import os


def get_html_template(template_name, **kwargs):
    template = Environment(
        loader=FileSystemLoader(os.path.join(os.path.dirname(__file__), '../templates')),
        autoescape=select_autoescape(['html', 'xml'])
    )
    template = template.get_template(template_name)
    return template.render(kwargs)