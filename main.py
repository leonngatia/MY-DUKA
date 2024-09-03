from flask import Flask,render_template,redirect,url_for,request,flash,session
from dbservice import get_data, insert_products,sales_product,profit,sales_daily,profit_daily,recent_sales,insert_user,check_email,check_email_password,insert_sales
# Create the flask instance
app=Flask(__name__)
app.secret_key='leon'
# first route
@app.route('/')
def home():
    return render_template ('home.html')


@app.route("/contact")
def contact():
    return render_template('contact.html')


@app.route("/products")
def products():
 if "email" in session:
    prods=get_data("products")
    return render_template('products.html',products=prods)
 else:
     flash("login to view this page")
     return redirect(url_for('login'))


@app.route("/add_products",methods=['POST','GET'])
def add_products():
    # check method
    if request.method=='POST':
      # get form data
     name=request.form["pname"]
     bprice=request.form["bp"]
     sprice=request.form["sp"]
     squantity=request.form["quantity"]
     new_prod=(name,bprice,sprice,squantity,)
     insert_products(new_prod)
    return redirect(url_for("products"))


@app.route("/sales")
def sales():
 if "email" in session:
    sal=get_data("sales")
    products=get_data("products")
    return render_template('sales.html',sales=sal,products=products)
 else:
     flash("login to view this page")
     return redirect(url_for('login'))


@app.route("/add_sales",methods=['POST','GET'])
def add_sales():
    # check method
    if request.method=='POST':
       id=request.form["pid"]
       
       qt=request.form["quantity"]

       new_sales=(id,qt)
       insert_sales(new_sales)
       return redirect(url_for("sales"))





 
@app.route("/dashboard")
def dashboard():
#   sales per product
    if "email" in session:
        sales_prod=sales_product()
  
        psales=[]
        for i in sales_prod:
    
            psales.append(float(i[1]))
    #  profit
        pr=profit()
        prof=[]
        pn=[]
        for i in pr:
            prof.append(i[1])
            pn.append(i[0])
    # sales per day
        s_d=sales_daily()
        sales_d=[]
        date=[]
    
        for i in s_d:
            sales_d.append(float(i[1]))
            date.append(str(i[0]))
    #    profit per day
    else:
        flash("login to view this page")
        return redirect(url_for('login'))

    p_d=profit_daily()
    print(p_d)
    profit_d=[]
    for i in p_d:
        profit_d.append(float(i[1]))
 # recent sales
    r_s=recent_sales()

    
    






   
    return render_template("dashboard.html",pn=pn,prof=prof,psales=psales,sales_d=sales_d,date=date,profit_d=profit_d,r_s=r_s)




@app.route("/login",methods=['POST','GET'])
def login():
    # get form data
    if request.method=='POST':
        email=request.form['email']
        password=request.form['password']
        c_email=check_email(email)
        if len(c_email)==1:
            c_em_ps=check_email_password(email,password)
            if len(c_em_ps)==1:
                session['email']=email
                flash("login succesfully")
                return redirect(url_for('dashboard'))
            else:
                flash("wrong credentials")
        flash("email does not exist")                

    return render_template("login.html")






@app.route("/register",methods=['POST','GET'])
def register():
    if request.method=='POST':
        fname=request.form['username']
        email=request.form['email']
        passw=request.form['password']

        insert=(fname,email,passw,)
        c_email=check_email(email)
        if len (c_email)==0:
          insert_user(insert)
          flash("Registered Successfully")
          return redirect(url_for("login"))
        else:
            flash("Email already exists")
    return render_template('register.html')
@app.route("/logout")
def logout():
    # Clear the session
    session.clear()
    return redirect(url_for("login"))

app.run(debug=True)

