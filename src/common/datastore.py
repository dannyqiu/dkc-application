import os
import google.auth.credentials
from google.cloud import ndb

if os.getenv("GAE_ENV", "").startswith("standard"):
    # Production in the standard environment
    db = ndb.Client()
else:
    # Local execution.
    os.environ["DATASTORE_DATASET"] = "dkc-app"
    os.environ["DATASTORE_PROJECT_ID"] = "dkc-app-fake-project-id"
    os.environ["DATASTORE_EMULATOR_HOST"] = "localhost:8500"
    os.environ["DATASTORE_EMULATOR_HOST_PATH"] = "localhost:8500/datastore"
    os.environ["DATASTORE_HOST"] = "http://localhost:8500"

    from unittest.mock import Mock

    credentials = Mock(spec=google.auth.credentials.Credentials)
    db = ndb.Client(credentials=credentials)


def g_ndb_wsgi_middleware(wsgi_app):
    def middleware(environ, start_response):
        with db.context():
            return wsgi_app(environ, start_response)

    return middleware
