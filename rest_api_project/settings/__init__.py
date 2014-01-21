from .production import *

if bool(os.environ.get('LOCAL_DEV', False)):
    from .development import *
