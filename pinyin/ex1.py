from flask import Flask,render_template,request
from xpinyin import Pinyin

app=Flask(__name__)

@app.route('/')
def index():
    pinyin=Pinyin()
    wby=pinyin.get_pinyin(u'code',show_tone_marks=True)
    wby1=request.form.get(wby)
    print wby1
    if request.method=='GET':
        return render_template('ex1.html')    
    else:
        return 'post success!!!!!~~~!!!!!!!' 



if __name__=='__main__':
    app.run(debug=True)