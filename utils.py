import os
import uuid
from flask import current_app


def save_upload(file_storage, allowed_extensions):
    """Safely saves an uploaded file with a random filename.
    Returns the saved filename, or None if no file was provided."""
    if not file_storage or file_storage.filename == '':
        return None

    original_name = file_storage.filename
    ext = original_name.rsplit('.', 1)[-1].lower() if '.' in original_name else ''

    if ext not in allowed_extensions:
        raise ValueError('File type not allowed.')

    unique_name = f"{uuid.uuid4().hex}.{ext}"
    upload_folder = current_app.config['UPLOAD_FOLDER']
    file_storage.save(os.path.join(upload_folder, unique_name))
    return unique_name


def delete_upload(filename):
    """Deletes a previously uploaded file if it exists."""
    if not filename:
        return
    upload_folder = current_app.config['UPLOAD_FOLDER']
    path = os.path.join(upload_folder, filename)
    if os.path.exists(path):
        os.remove(path)