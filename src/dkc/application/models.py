from google.cloud import ndb
from common.models import Settings

class InternationalProject(ndb.Model):
    section = ndb.TextProperty()
    event = ndb.StringProperty()
    description = ndb.TextProperty()

class DistrictProject(ndb.Model):
    event = ndb.StringProperty()
    charity = ndb.StringProperty()
    description = ndb.TextProperty()

class Divisional(ndb.Model):
    date = ndb.StringProperty()
    location = ndb.StringProperty()

class GeneralProject(ndb.Model):
    event = ndb.StringProperty()
    location = ndb.StringProperty()
    description = ndb.TextProperty()

class Application(ndb.Model):
    start_time = ndb.DateTimeProperty(auto_now_add=True)
    updated_time = ndb.DateTimeProperty(auto_now=True)
    submit_time = ndb.DateTimeProperty()

    @ndb.model.ComputedProperty
    def is_early_submission(self):
        config = ndb.Key(Settings, 'config').get()
        early_due_date = config.early_due_date
        if self.submit_time is not None:
            return self.submit_time < early_due_date
        else:
            return False

    # Profile
    grade = ndb.StringProperty()
    address = ndb.StringProperty()
    city = ndb.StringProperty()
    zip_code = ndb.StringProperty()
    phone_number = ndb.StringProperty()
    division = ndb.StringProperty()
    ltg = ndb.StringProperty()
    school = ndb.StringProperty()
    school_address = ndb.StringProperty()
    school_city = ndb.StringProperty()
    school_zip_code = ndb.StringProperty()
    club_president = ndb.StringProperty()
    club_president_phone_number = ndb.StringProperty()
    faculty_advisor = ndb.StringProperty()
    faculty_advisor_phone_number = ndb.StringProperty()

    # Personal Statement
    personal_statement_choice = ndb.StringProperty()
    personal_statement = ndb.TextProperty()

    # Projects
    international_projects = ndb.StructuredProperty(InternationalProject, repeated=True)
    district_projects = ndb.StructuredProperty(DistrictProject, repeated=True)
    divisionals = ndb.StructuredProperty(Divisional, repeated=True)
    division_projects = ndb.StructuredProperty(GeneralProject, repeated=True)

    # Involvement
    key_club_week_mon = ndb.TextProperty()
    key_club_week_tue = ndb.TextProperty()
    key_club_week_wed = ndb.TextProperty()
    key_club_week_thu = ndb.TextProperty()
    key_club_week_fri = ndb.TextProperty()
    attendance_dtc = ndb.BooleanProperty()
    attendance_fall_rally = ndb.BooleanProperty()
    attendance_kamp_kiwanis = ndb.BooleanProperty()
    attendance_key_leader = ndb.BooleanProperty()
    attendance_ltc = ndb.BooleanProperty()
    attendance_icon = ndb.BooleanProperty()
    positions = ndb.TextProperty()

    # Activities
    kiwanis_one_day = ndb.StructuredProperty(GeneralProject)
    k_family_projects = ndb.StructuredProperty(GeneralProject, repeated=True)
    interclub_projects = ndb.StructuredProperty(GeneralProject, repeated=True)
    advocacy_cause = ndb.StringProperty()
    advocacy_description = ndb.TextProperty()
    advocacy_materials = ndb.BlobKeyProperty(repeated=True)
    committee = ndb.StringProperty()
    committee_type = ndb.StringProperty()
    committee_description = ndb.TextProperty()
    divisional_newsletter = ndb.BooleanProperty()
    divisional_newsletter_info = ndb.TextProperty()
    district_newsletter = ndb.BooleanProperty()
    district_newsletter_info = ndb.TextProperty()
    district_website = ndb.BooleanProperty()
    district_website_info = ndb.TextProperty()
    other_projects = ndb.StructuredProperty(GeneralProject, repeated=True)

    # Other
    early_submission_points = ndb.StringProperty()
    recommender_points = ndb.StringProperty()
    outstanding_awards = ndb.StringProperty()
    scoring_reason_two = ndb.TextProperty()
    scoring_reason_three = ndb.TextProperty()
    scoring_reason_four = ndb.TextProperty()
    other_materials = ndb.BlobKeyProperty(repeated=True)

    # Verification
    verification_ltg = ndb.BooleanProperty()
    verification_ltg_email = ndb.StringProperty()
    verification_ltg_sent = ndb.BooleanProperty()
    verification_ltg_token = ndb.StringProperty()

    verification_club_president = ndb.BooleanProperty()
    verification_club_president_email = ndb.StringProperty()
    verification_club_president_sent = ndb.BooleanProperty()
    verification_club_president_token = ndb.StringProperty()

    verification_faculty_advisor = ndb.BooleanProperty()
    verification_faculty_advisor_email = ndb.StringProperty()
    verification_faculty_advisor_sent = ndb.BooleanProperty()
    verification_faculty_advisor_token = ndb.StringProperty()

    verification_applicant = ndb.BooleanProperty()
    verification_applicant_date = ndb.DateTimeProperty()

    # INTERNAL ADMIN USE ONLY
    notes = ndb.TextProperty(default="")
    # TODO(dannyqiu): change graded to reviewed
    graded = ndb.BooleanProperty()