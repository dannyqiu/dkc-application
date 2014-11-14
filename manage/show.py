import urllib
#from dkc import *
from manage import *
from dkc.models import User

class ShowHandler(AdminBaseHandler):

    def get(self, email):
        email = str(urllib.unquote(email))
        applicant = User.get_by_auth_id(email)
        application = applicant.application.get()

        template_values = {
            'applicant': applicant,
            'application': application,
            'admin_url': '/admin/show/' + email
        }
        self.render_template('admin-show.html', template_values)

    def post(self):
        pass