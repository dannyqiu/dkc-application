import os, webapp2, jinja2
from google.appengine.api import users, memcache
from dkc import jinja_functions
from dkc.models import User

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__), '../templates/admin')),
    extensions=['jinja2.ext.autoescape'])
JINJA_ENVIRONMENT.filters['datetimeformat'] = jinja_functions.datetimeformat
JINJA_ENVIRONMENT.filters['getblobdata'] = jinja_functions.getBlobData
JINJA_ENVIRONMENT.filters['byteconvert'] = jinja_functions.byteConversion
JINJA_ENVIRONMENT.filters['split_string'] = jinja_functions.splitString
JINJA_ENVIRONMENT.filters['split_regex'] = jinja_functions.splitRegex

class AdminBaseHandler(webapp2.RequestHandler):

    def user(self):
        return users.get_current_user()

    def render_template(self, template_filename, template_values={}):
        user = users.get_current_user()
        user_object = {"email": user.email(),
                       "nickname": user.nickname(),
                       "user_id": user.user_id(),
                       "logout_url": users.create_logout_url('/')
                      }
        template_values['user'] = user_object
        template = JINJA_ENVIRONMENT.get_template(template_filename)
        self.response.out.write(template.render(template_values))

    def display_message(self, message):
        template_values = {
            'message': message
        }
        self.render_template('message.html', template_values)

    def get_applicants(self):
        applicants = memcache.get('all_applicants')
        if not applicants:
            query = User.query()
            applicants = query.fetch()
            memcache.add(key='all_applicants', value=applicants, time=900)
        return applicants
