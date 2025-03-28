import shelve, dbm, os

shelveDir = 'db'
shelvePath = os.path.join(shelveDir, 'id_counter')


class User:
    count_id: int = None

    def load_user_id(self):
        try:
            counter = shelve.open(f'{shelvePath}', 'r')
        except dbm.error:
            if not os.path.isdir(shelveDir):
                os.makedirs(shelveDir)
            counter = shelve.open(f'{shelvePath}', 'c')

        if 'User' not in counter:
            counter.close()
            counter = shelve.open(f'{shelvePath}', 'w')
            counter['User'] = 0

        self.__class__.count_id = counter['User']
        counter.close()

    def save_user_id(self):
        with shelve.open(f'{shelvePath}', 'w') as counter:
            counter['User'] = self.__class__.count_id

    def __init__(self, first_name, last_name, gender, membership, remarks):
        self.__class__.load_user_id(self)
        self.__class__.count_id += 1
        self.__class__.save_user_id(self)
        self.__user_id = self.__class__.count_id
        self.__first_name = first_name
        self.__last_name = last_name
        self.__gender = gender
        self.__membership = membership
        self.__remarks = remarks

    def __str__(self):
        membership_status = dict(F="Fellow", S="Senior", P="Professional")

        return (
                f"User #{self.__user_id}\n"
                f"\tName: {self.__first_name} {self.__last_name}\n"
                f"\tGender: {"Male" if self.__gender == "M" else "Female" if self.__gender == "F" else None}\n"
                f"\tMembership: {membership_status[self.__membership]}\n"
                f"\tRemarks: {self.__remarks}\n"
                )


    # Accessor methods
    def set_user_id(self, user_id):
        self.__user_id = user_id

    def set_first_name(self, first_name):
        self.__first_name = first_name

    def set_last_name(self, last_name):
        self.__last_name = last_name

    def set_gender(self, gender):
        self.__gender = gender

    def set_membership(self, membership):
        self.__membership = membership

    def set_remarks(self, remarks):
        self.__remarks = remarks


    # Mutator methods
    def get_user_id(self):
        return self.__user_id

    def get_first_name(self):
        return self.__first_name

    def get_last_name(self):
        return self.__last_name

    def get_gender(self):
        return self.__gender

    def get_membership(self):
        return self.__membership

    def get_remarks(self):
        return self.__remarks
