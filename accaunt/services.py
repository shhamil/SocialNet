import uuid
from os.path import splitext


def get_unical_name(instance, filename):
    return '%s%s' % (uuid.uuid1(), splitext(filename)[1])
