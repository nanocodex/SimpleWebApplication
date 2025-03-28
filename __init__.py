from flask import Flask, render_template, request, redirect, url_for, session
from Forms import CreateUserForm, CreateCustomerForm
import shelve, dbm, User, Customer, os

app = Flask(__name__)
app.secret_key = 'any_random_string'
shelveDir = 'db'
shelvePathUser = os.path.join(shelveDir, 'user')
shelvePathCustomer = os.path.join(shelveDir, 'customer')


# Error Handlers
@app.errorhandler(404)
def page_not_found(_error):
    return render_template('error404.html'), 404

# App Routes
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/contactUs')
def contact_us():
    return render_template('contactUs.html')

@app.route('/createUser', methods=['GET', 'POST'])
def create_user():
    create_user_form = CreateUserForm(request.form)
    if request.method == 'POST' and create_user_form.validate():
        users_dict = {}
        if not os.path.isdir(shelveDir):
            os.makedirs(shelveDir)
        db = shelve.open(f'{shelvePathUser}', 'c')

        if 'Users' in db:
            users_dict = db['Users']
        else:
            db['Users'] = users_dict
        user = User.User(
            create_user_form.first_name.data,
            create_user_form.last_name.data,
            create_user_form.gender.data,
            create_user_form.membership.data,
            create_user_form.remarks.data
        )
        users_dict[user.get_user_id()] = user
        db['Users'] = users_dict

        db.close()

        session['user_created'] = user.get_first_name() + ' ' + user.get_last_name()

        return redirect(url_for('retrieve_users'))
    return render_template('createUser.html', form = create_user_form)

@app.route('/createCustomer', methods=['GET', 'POST'])
def create_customer():
    create_customer_form = CreateCustomerForm(request.form)
    if request.method == 'POST' and create_customer_form.validate():
        customers_dict = {}
        if not os.path.isdir(shelveDir):
            os.makedirs(shelveDir)
        db = shelve.open(f'{shelvePathCustomer}', 'c')

        if 'Customers' in db:
            customers_dict = db['Customers']
        else:
            db['Customers'] = customers_dict
        customer = Customer.Customer(
            create_customer_form.first_name.data,
            create_customer_form.last_name.data,
            create_customer_form.gender.data,
            create_customer_form.membership.data,
            create_customer_form.remarks.data,
            create_customer_form.email.data,
            create_customer_form.date_joined.data,
            create_customer_form.address.data
        )
        customers_dict[customer.get_customer_id()] = customer
        db['Customers'] = customers_dict

        db.close()

        session['customer_created'] = customer.get_first_name() + ' ' + customer.get_last_name()

        return redirect(url_for('retrieve_customers'))
    return render_template('createCustomer.html', form = create_customer_form)

@app.route('/retrieveUsers')
def retrieve_users():
    users_dict = {}
    try:
        db = shelve.open(f'{shelvePathUser}', 'r')
    except dbm.error:
        db = shelve.open(f'{shelvePathUser}', 'c')

    if 'Users' in db:
        users_dict = db['Users']
    else:
        db['Users'] = users_dict
    db.close()

    users_list = []
    for key in users_dict:
        user = users_dict.get(key)
        users_list.append(user)

    return render_template('retrieveUsers.html', count = len(users_list), users_list = users_list)

@app.route('/retrieveCustomers')
def retrieve_customers():
    customers_dict = {}
    try:
        db = shelve.open(f'{shelvePathCustomer}', 'r')
    except dbm.error:
        db = shelve.open(f'{shelvePathCustomer}', 'c')

    if 'Customers' in db:
        customers_dict = db['Customers']
    else:
        db['Customers'] = customers_dict
    db.close()

    customers_list = []
    for key in customers_dict:
        customer = customers_dict.get(key)
        customers_list.append(customer)

    return render_template('retrieveCustomers.html', count = len(customers_list), customers_list = customers_list)

@app.route('/updateUser/<int:user_id>/', methods=['GET', 'POST'])
def update_user(user_id):
    update_user_form = CreateUserForm(request.form)
    if request.method == 'POST' and update_user_form.validate():
        users_dict = {}
        db = shelve.open(f'{shelvePathUser}', 'w')
        if 'Users' in db:
            users_dict = db['Users']
        else:
            db['Users'] = users_dict

        user = users_dict.get(user_id)
        user.set_first_name(update_user_form.first_name.data)
        user.set_last_name(update_user_form.last_name.data)
        user.set_gender(update_user_form.gender.data)
        user.set_membership(update_user_form.membership.data)
        user.set_remarks(update_user_form.remarks.data)

        db['Users'] = users_dict
        db.close()

        session['user_updated'] = user.get_first_name() + ' ' + user.get_last_name()

        return redirect(url_for('retrieve_users'))
    else:
        users_dict = {}
        db = shelve.open(f'{shelvePathUser}', 'r')
        if 'Users' in db:
            users_dict = db['Users']
        else:
            db['Users'] = users_dict
        db.close()

        user = users_dict.get(user_id)
        update_user_form.first_name.data = user.get_first_name()
        update_user_form.last_name.data = user.get_last_name()
        update_user_form.gender.data = user.get_gender()
        update_user_form.membership.data = user.get_membership()
        update_user_form.remarks.data = user.get_remarks()

        return render_template('updateUser.html', form = update_user_form)

@app.route('/updateCustomer/<int:customer_id>/', methods=['GET', 'POST'])
def update_customer(customer_id):
    update_customer_form = CreateCustomerForm(request.form)
    if request.method == 'POST' and update_customer_form.validate():
        customers_dict = {}
        db = shelve.open(f'{shelvePathCustomer}', 'w')
        if 'Customers' in db:
            customers_dict = db['Customers']
        else:
            db['Customers'] = customers_dict

        customer = customers_dict.get(customer_id)
        customer.set_first_name(update_customer_form.first_name.data)
        customer.set_last_name(update_customer_form.last_name.data)
        customer.set_gender(update_customer_form.gender.data)
        customer.set_email(update_customer_form.email.data)
        customer.set_date_joined(update_customer_form.date_joined.data)
        customer.set_address(update_customer_form.address.data)
        customer.set_membership(update_customer_form.membership.data)
        customer.set_remarks(update_customer_form.remarks.data)

        db['Customers'] = customers_dict
        db.close()

        session['customer_updated'] = customer.get_first_name() + ' ' + customer.get_last_name()

        return redirect(url_for('retrieve_customers'))
    else:
        customers_dict = {}
        db = shelve.open(f'{shelvePathCustomer}', 'r')
        if 'Customers' in db:
            customers_dict = db['Customers']
        else:
            db['Customers'] = customers_dict
        db.close()

        customer = customers_dict.get(customer_id)
        update_customer_form.first_name.data = customer.get_first_name()
        update_customer_form.last_name.data = customer.get_last_name()
        update_customer_form.gender.data = customer.get_gender()
        update_customer_form.email.data = customer.get_email()
        update_customer_form.date_joined.data = customer.get_date_joined()
        update_customer_form.address.data = customer.get_address()
        update_customer_form.membership.data = customer.get_membership()
        update_customer_form.remarks.data = customer.get_remarks()

        return render_template('updateCustomer.html', form = update_customer_form)

@app.route('/deleteUser/<int:user_id>', methods=['POST'])
def delete_user(user_id):
    users_dict = {}
    db = shelve.open(f'{shelvePathUser}', 'w')
    if 'Users' in db:
        users_dict = db['Users']
    else:
        db['Users'] = users_dict

    user = users_dict.pop(user_id)

    db['Users'] = users_dict
    db.close()

    session['user_deleted'] = user.get_first_name() + ' ' + user.get_last_name()

    return redirect(url_for('retrieve_users'))

@app.route('/deleteCustomer/<int:customer_id>', methods=['POST'])
def delete_customer(customer_id):
    customers_dict = {}
    db = shelve.open(f'{shelvePathCustomer}', 'w')
    if 'Customers' in db:
        customers_dict = db['Customers']
    else:
        db['Customers'] = customers_dict

    customer = customers_dict.pop(customer_id)

    db['Customers'] = customers_dict
    db.close()

    session['customer_deleted'] = customer.get_first_name() + ' ' + customer.get_last_name()

    return redirect(url_for('retrieve_customers'))


# Run App
if __name__ == '__main__':
    app.run(debug = False)
