import random
import string
from operator import truediv

from flask import Flask,render_template,request
punctuation='!@#$%^&*()?><{}'
def generate_password(length,use_number,use_symbols):
    all_character = string.ascii_letters
    password_list=[]
    if use_number:
        pass
    elif use_symbols:
        pass
    else:
        use_number=True
        use_symbols=True



    if use_number:
        password_list.append(random.choice(string.digits))
        all_character += string.digits
    if use_symbols:
        password_list.append(random.choice(punctuation))
        all_character+= punctuation
    remaining_length = length - len(password_list)
    password_list.extend(random.choices(all_character,k=remaining_length))
    random.shuffle(password_list)
    password = ''.join(password_list)
    return password
app=Flask(__name__)

@app.route('/',methods=['GET','POST'])
def home():
    password=''
    if request.method=='POST':
        length=int(request.form.get('length'))
        num=request.form.get('use_number')
        symbol=request.form.get('use_symbols')

        password=generate_password(length,use_number=num,use_symbols=symbol)
    return render_template('index.html',password=password)
if __name__== '__main__':
    app.run(debug=True)

