# users/picture_handler.py 

import os
from PIL import Image 
from flask import url_for, current_app
from werkzeug.security import generate_password_hash

def add_profile_picture(picture_upload, username):

	filename = picture_upload.filename
	extention_type = filename.split('.')[-1]
	storage_filename = str(generate_password_hash(username))+'.'+extention_type
	# Set the path for storring profiel pictures
	filepath = os.path.join(current_app.root_path, 'static/profile_pics', storage_filename)

	# set the picture that will be served
	profile_picture = Image.open(picture_upload)
	# set size of thumbnail in px (200px x 200px in this case)
	profile_picture.thumbnail(200,200)
	profile_picture.save(filepath)

	return storage_filename