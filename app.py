from flask import Flask, render_template, request
from car_functions.import_functions import get_random_cars_brand

# initiate the flask app
app = Flask(__name__)


# first route
@app.route('/')
def index():

    return render_template("index.html")


# route to show cars
@app.route('/get_brand', methods=['GET', 'POST'])
def get_brand():
    if request.method == 'GET':
        return render_template("get_brand.html")
    else:
        # define the brand
        selected_brand = request.form.get('brand')

        # use the function to get the list with cars
        cars_list = get_random_cars_brand(selected_brand)
        
        return render_template("get_brand.html", 
                            cars_list=cars_list)


# run the application
if __name__ == "__main__":
    app.run()