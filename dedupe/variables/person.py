from dedupe.variables.name import WesternNameType

class WesternPersonNameType(WesternNameType):
    type = "Person Name"

    def __init__(self, definition) :
        definition['name type'] = 'person'

        super(WesternPersonNameType, self).__init__(definition)

