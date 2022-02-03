def get_pic_upload_to(instance, filename):
    return "static/profile/{}/pic/{}".format(instance.user, filename)

def get_aadhar_upload_to(instance, filename):
    instance.filename = filename
    return "static/profile/{}/aadhar/{}".format(instance.user, filename)

def get_passbook_upload_to(instance, filename):
    instance.filename = filename
    return "static/profile/{}/passbook/{}".format(instance.user, filename)