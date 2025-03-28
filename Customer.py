from User import User
import shelve, dbm, os

shelveDir = 'db'
shelvePath = os.path.join(shelveDir, 'id_counter')


class Customer(User):
    count_id: int = None

    def load_customer_id(self):
        try:
            counter = shelve.open(f'{shelvePath}', 'r')
        except dbm.error:
            if not os.path.isdir(shelveDir):
                os.makedirs(shelveDir)
            counter = shelve.open(f'{shelvePath}', 'c')

        if 'Customer' not in counter:
            counter.close()
            counter = shelve.open(f'{shelvePath}', 'w')
            counter['Customer'] = 0

        self.__class__.count_id = counter['Customer']
        counter.close()

    def save_customer_id(self):
        with shelve.open(f'{shelvePath}', 'w') as counter:
            counter['Customer'] = self.__class__.count_id

    def __init__(self, first_name, last_name, gender, membership, remarks, email, date_joined, address):
        super().__init__(first_name, last_name, gender, membership, remarks)
        self.__class__.load_customer_id(self)
        self.__class__.count_id += 1
        self.__class__.save_customer_id(self)
        self.__customer_id = self.__class__.count_id
        self.__email = email
        self.__date_joined = date_joined
        self.__address = address

    def __str__(self):
        return super().__str__() + (
            f"\tCustomer ID: {self.__customer_id}\n"
            f"\tEmail: {self.__email}\n"
            f"\tDate Joined: {self.__date_joined}\n"
            f"\tAddress: {self.__address}\n"
        )

    # Accessor methods
    def get_customer_id(self):
        return self.__customer_id

    def get_email(self):
        return self.__email

    def get_date_joined(self):
        return self.__date_joined

    def get_address(self):
        return self.__address

    # Mutator  methods
    def set_customer_id(self, customer_id):
        self.__customer_id = customer_id

    def set_email(self, email):
        self.__email = email

    def set_date_joined(self, date_joined):
        self.__date_joined = date_joined

    def set_address(self, address):
        self.__address = address
