class Student():

    def __init__(self, **kwargs):
        self.name = kwargs['name']
        self.lastname = kwargs['lastname']
        self.dni = kwargs['dni']
        self.career = kwargs['career_name']
        print(kwargs.keys())

        if 'email' in kwargs.keys():
            self.email = kwargs['email']

        if 'second_name' in kwargs.keys():
            self.second_name = kwargs['second_name']

        if 'second_lastname' in kwargs.keys():
            self.second_lastname = kwargs['second_lastname']

    def show_data(self):
        message = self.name
        if 'second_name' in vars(self).keys():
            message += f' {self.second_name}'

        message += f' {self.lastname}'
        if 'second_lastname' in vars(self).keys():
            message += f' {self.second_lastname}'

        message += f'. {self.dni}'
        message += f'. {self.career}'
        if 'email' in vars(self).keys():
            message += f'. {self.email}'

        return message

# student = Student(**s)
