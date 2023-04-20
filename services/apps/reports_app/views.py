from flask import Blueprint, render_template

report = Blueprint('report', __name__, url_prefix='/reports')


@report.route('/')
def report_list():
    return render_template(
        'reports_app/list.html',
        reports=[1, 21, 4, 137]
    )
