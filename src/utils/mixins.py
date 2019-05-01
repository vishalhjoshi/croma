

class CreateFormsMixin(object):
    model = None
    lookup = None
    formClass = None
    templateName = None

    def get(self, *args, **kwargs):
        pass

    def post(self, *args, **kwargs):
        pass

    