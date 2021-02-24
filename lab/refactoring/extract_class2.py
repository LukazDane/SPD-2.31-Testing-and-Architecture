# by Kami Bigdely
# Extract class
class Applicants():
    def __init__(self, first_name, last_name, birth_year, email=None, movies=None):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_year = birth_year
        self.email = email
        self.movies = movies

    def email(self, email_address):
        self.email = email_address

    def add_movies(self, movies):
        self.moveis.append(movies)
# first_names = ['elizabeth', 'Jim']
# last_names = ['debicki', 'Carrey']
# birth_year = [1990, 1962]
# movies = [['Tenet', 'Vita & Virgina', 'Guardians of the Galexy', 'The Great Gatsby'],
#           ['Ace Ventura', 'The Mask', 'Dumb and Dumber', 'The Truman Show', 'Yes Man']]
# emails = ['deb@makeschool.com', 'jim@makeschool.com']


def send_hiring_email(email):
    print("email sent to: ", email)


elizabeth_debicki = Applicants('Elizabeth', 'debicki', 1990, 'deb@makeschool.com',
                               ['Tenet', 'Vita & Virgina', 'Guardians of the Galexy', 'The Great Gatsby'])
jim_carrey = Applicants('Jim', 'Carrey', 1962, 'jim@makeschool.com',
                        ['Ace Ventura', 'The Mask', 'Dumb and Dumber', 'The Truman Show', 'Yes Man'])
applicants = [elizabeth_debicki, jim_carrey]

for applicant in applicants:
    if applicant.birth_year < 1985:
        print(applicant.first_name, applicant.last_name)
        print('Movies Played: ', end='')
        for m in applicant.movies:
            print(m, end=', ')
        print()
        send_hiring_email(applicant.email)

# for applicant in applicants:
#     if applicant.birth_year == 1962:
#         print(applicant.first_name, applicant.last_name)
#         print('Movies Played: ', end='')
#         for m in applicant.movies:
#             print(m, end=', ')
#         print()
#         send_hiring_email(applicant.email)
