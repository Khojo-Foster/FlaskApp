from flask import Flask,render_template,request


app = Flask(__name__) # Creating an instance of app

@app.route("/")  
def index():
    return render_template("index.html")
    # return "Welcome to My App"

@app.route("/user/<username>")   
def show_user_profile(username):
    return render_template("user_profile.html", user=username) 

api_data = [
    {
        "id":1,
        "name": "Apple",
        "description": "A fruit known for being crisp and sweet."
    },
    
    {
        "id":2,
        "name": "Banana",
        "description": "A yellow tropical fruit rich in potassium."
    },

    {
        "id":3,
        "name": "Cherry",
        "description": "A small, round stone fruit that can be red or black."
    },

    {
        "id":4,
        "name": "Orange",
        "description": "A small, round juicy fruit that taste so good."
    },
]    

@app.route("/items")
def show_all_items():
    return render_template("all_items.html", items=api_data)

@app.route("/shoppinglist",methods =["GET","POST"])
def shoppinglist():
    if request.method == "POST":
        item = request.form.get("item")
        if item:
            api_data.append({
                "id": len(api_data) + 1,
                "name": item,
                "description": "No description"
            })
    return render_template("shopping_list.html", items = item)        


if __name__== "__main__":
    app.run(debug=True)