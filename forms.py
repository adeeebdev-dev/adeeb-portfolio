from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import (StringField, PasswordField, TextAreaField, BooleanField,
                      IntegerField, SubmitField, SelectField, EmailField)
from wtforms.validators import DataRequired, Length, Optional, Email


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(max=80)])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log In')


class ProjectForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired(), Length(max=150)])
    slug = StringField('Slug (URL-friendly, e.g. my-project)', validators=[DataRequired(), Length(max=180)])
    short_description = StringField('Short Description', validators=[DataRequired(), Length(max=300)])
    full_description = TextAreaField('Full Description', validators=[Optional()])
    category = SelectField('Category', choices=[
        ('Web Development', 'Web Development'), ('Python', 'Python'), ('Java', 'Java'),
        ('JavaScript', 'JavaScript'), ('AI', 'AI'), ('Automation', 'Automation'), ('Academic', 'Academic')
    ])
    technologies = StringField('Technologies (comma-separated)', validators=[Optional(), Length(max=300)])
    features = TextAreaField('Features (one per line)', validators=[Optional()])
    github_url = StringField('GitHub URL', validators=[Optional(), Length(max=255)])
    live_demo_url = StringField('Live Demo URL', validators=[Optional(), Length(max=255)])
    project_date = StringField('Project Date (YYYY-MM-DD)', validators=[Optional()])
    image = FileField('Project Image', validators=[Optional(), FileAllowed(['png', 'jpg', 'jpeg', 'webp'], 'Images only!')])
    is_featured = BooleanField('Featured Project')
    is_published = BooleanField('Published')
    order_index = IntegerField('Order Index', default=0)
    submit = SubmitField('Save Project')


class CertificateForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired(), Length(max=150)])
    organization = StringField('Organization', validators=[DataRequired(), Length(max=150)])
    issue_date = StringField('Issue Date (YYYY-MM-DD)', validators=[Optional()])
    certificate_code = StringField('Certificate Code', validators=[Optional(), Length(max=100)])
    verification_url = StringField('Verification URL', validators=[Optional(), Length(max=255)])
    description = TextAreaField('Description', validators=[Optional()])
    image = FileField('Certificate Image', validators=[Optional(), FileAllowed(['png', 'jpg', 'jpeg', 'webp', 'pdf'], 'Images or PDF only!')])
    is_published = BooleanField('Published', default=True)
    order_index = IntegerField('Order Index', default=0)
    submit = SubmitField('Save Certificate')


class ExperienceForm(FlaskForm):
    organization = StringField('Organization', validators=[DataRequired(), Length(max=150)])
    role = StringField('Role', validators=[DataRequired(), Length(max=150)])
    location = StringField('Location', validators=[Optional(), Length(max=150)])
    start_date = StringField('Start Date (YYYY-MM-DD)', validators=[Optional()])
    end_date = StringField('End Date (YYYY-MM-DD, leave blank if current)', validators=[Optional()])
    is_current = BooleanField('Currently Working Here')
    description = TextAreaField('Description', validators=[Optional()])
    technologies = StringField('Technologies (comma-separated)', validators=[Optional(), Length(max=300)])
    document = FileField('Experience Document', validators=[Optional(), FileAllowed(['pdf', 'png', 'jpg', 'jpeg'], 'PDF or image only!')])
    document_is_public = BooleanField('Make Document Publicly Visible')
    order_index = IntegerField('Order Index', default=0)
    submit = SubmitField('Save Experience')


class SkillForm(FlaskForm):
    category = StringField('Category (e.g. Programming, Automation)', validators=[DataRequired(), Length(max=80)])
    name = StringField('Skill Name (e.g. Python)', validators=[DataRequired(), Length(max=80)])
    order_index = IntegerField('Order Index', default=0)
    submit = SubmitField('Save Skill')


class ContactForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(max=100)])
    email = EmailField('Email', validators=[DataRequired(), Email(), Length(max=150)])
    subject = StringField('Subject', validators=[Optional(), Length(max=200)])
    body = TextAreaField('Message', validators=[DataRequired(), Length(min=10, max=2000)])
    submit = SubmitField('Send Message')

class ProfileForm(FlaskForm):
    about_text = TextAreaField('About Text', validators=[DataRequired()])
    phone = StringField('Phone', validators=[Optional(), Length(max=30)])
    location = StringField('Location', validators=[Optional(), Length(max=150)])
    submit = SubmitField('Save Changes')