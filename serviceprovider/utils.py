def get_catelog_upload_to(instance, filename):
    return "static/auditorium/{}/{}/catelog/{}".format(instance.user,instance.name, filename)

def get_preview_upload_to(instance, filename):
    return "static/auditorium/{}/{}/preview/{}".format(instance.auditorium.user,instance.auditorium.name, filename)
