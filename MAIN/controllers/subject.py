from app import app
import constants
from flask import render_template, request


@app.route('/subject/<sub>')
def subject(sub):
    html = render_template(
        'subject.html',
        sub=sub,
        discription=constants.subject_dict[sub]
    )
    return html