from dkc import *

class LogoutPage(BaseHandler):

    def get(self):
        self.auth.unset_session()
        self.redirect('/')
