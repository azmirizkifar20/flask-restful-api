ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

def allowedFiles(fileName):
    return '.' in fileName and fileName.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS