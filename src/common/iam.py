import os
import googleapiclient.discovery

if os.getenv("GAE_ENV", "").startswith("standard"):
    # Production in the standard environment
    cloudresourcemanager = googleapiclient.discovery.build("cloudresourcemanager", "v1")
else:
    # Local execution.
    if not os.environ.get("GOOGLE_APPLICATION_CREDENTIALS"):
        raise EnvironmentError(
            """===== ENVIRONMENT ERROR =====
Please set GOOGLE_APPLICATION_CREDENTIALS to the path of your service account credential file.
This is usually a JSON file with a key to a service account, following instructions from
https://cloud.google.com/iam/docs/creating-managing-service-account-keys#creating_service_account_keys.
The preferred service account is the AppEngine service account:
    {}@appspot.gserviceaccount.com
===== ENVIORNMENT ERROR =====""".format(
                os.environ.get("GOOGLE_CLOUD_PROJECT", "dkc-app")
            )
        )
    cloudresourcemanager = googleapiclient.discovery.build("cloudresourcemanager", "v1")


def get_project_iam_policy():
    project_id = os.environ.get("GOOGLE_CLOUD_PROJECT", "dkc-app")
    request = cloudresourcemanager.projects().getIamPolicy(resource=project_id)
    resp = request.execute()
    return resp
