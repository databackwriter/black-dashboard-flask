# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from apps.home import blueprint
from apps.services.hue import toggle_light, light_list
from flask import jsonify, render_template, request
from flask_login import login_required
from jinja2 import TemplateNotFound


@blueprint.route('/index')
@login_required
def index():

    return render_template('home/index.html', segment='index')

@blueprint.route('/hue_light_on/<id>', methods=['GET', 'POST'])
@login_required
def hue_light_on(id):

    y = toggle_light(id)
    print(y)
    return lights_table()

@blueprint.route('/lights', methods=['GET', 'POST'])
@login_required
def lights_table():
    lights = light_list()
    segment = get_segment(request)
    return render_template('home/lights.html',  
                        #    tables=[df.to_html(classes=['tablesorter', 'text-primary'], border=None).replace("dataframe ", "table ")], 
                        #    titles=df.columns.values, 
                            titles = ['sdk', 'id_', 'name', 'is_on', 'bri', 'hue', 'sat'],
                            lights = lights,
                            segment=segment)

@blueprint.route('/<template>')
@login_required
def route_template(template):

    try:

        if not template.endswith('.html'):
            template += '.html'

        # Detect the current page
        segment = get_segment(request)

        # Serve the file (if exists) from app/templates/home/FILE.html
        return render_template("home/" + template, segment=segment)

    except TemplateNotFound:
        return render_template('home/page-404.html'), 404

    except:
        return render_template('home/page-500.html'), 500


# Helper - Extract current page name from request
def get_segment(request):

    try:

        segment = request.path.split('/')[-1]

        if segment == '':
            segment = 'index'

        return segment

    except:
        return None
