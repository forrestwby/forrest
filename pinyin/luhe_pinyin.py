#encoding: utf-8
#usr/bin/env python


from flask import Flask,render_template,request
from xpinyin import Pinyin


app=Flask(__name__)

@app.route('/')
def index():
    
    #pinyin=Pinyin()
    #hanzi=request.form.get('name')
    #wby=pinyin.get_pinyin(u'hanzi',show_tone_marks=True)
    #print wby
    return render_template('pinyin.html')

@app.route('/pinyin/',methods=['GET','POST'])
def pinyin():
    if request.method=='GET':
        return render_template('pinyin.html')
    else:
        pinyin=Pinyin()
        hanzi=request.form.get('name')
        print hanzi
        wby=pinyin.get_pinyin(hanzi,show_tone_marks=True)
        return render_template('pinyin.html',name=wby) 
            
    
       
    
if __name__=='__main__':
    app.run(port=80, debug=True)