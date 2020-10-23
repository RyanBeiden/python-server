class Animal():

    # Class initializer. It has 5 custom parameters, with the
    # special `self` parameter that every method on a class
    # needs as the first parameter.
    def __init__(self, id, name, breed, treatment, locationId, customerId):
        self.id = id
        self.name = name
        self.breed = breed
        self.treatment = treatment
        self.locationId = locationId
        self.customerId = customerId
        self.location = None
        self.customer = None
