class Student():

    def __init__(self, **kwargs):
        self.name = kwargs['name']
        self.lastname = kwargs['lastname']
        self.dni = kwargs['dni']
        self.career = kwargs['career_name'].capitalize()
        if kwargs['email']:
            self.email = kwargs['email']

        if kwargs['second_name']:
            self.second_name = kwargs['second_name']

        if kwargs['second_lastname']:
            self.second_lastname = kwargs['second_lastname']

    def show_data(self):
        message = self.name
        if 'second_name' in vars(self).keys():
            message += f' {self.second_name}'

        message += f' {self.lastname}'
        if 'second_lastname' in vars(self).keys():
            message += f' {self.second_lastname}'

        message += f'.\n{self.dni.upper()}.'
        message += f'\n{self.career}.'
        if 'email' in vars(self).keys():
            message += f'\n{self.email}.'

        return message
