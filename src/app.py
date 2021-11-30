from flask import app, Flask, render_template

app = Flask(__name__)


#HOME
@app.route('/')
def index():
    return render_template('index.html')

#SOBRE
@app.route('/sobre')
def sobre():
   return render_template('sobre.html')   

#TELA PROJETOS
@app.route('/projetos_tela')
def projetos_tela():    
   return render_template('Projetos_tela.html') 

#HOBBY TELA
@app.route('/Hobby_tela')
def Hobby_tela():
    return render_template('Hobby_tela.html')

#FUTEBOL
@app.route('/futebol')
def futebol():
    return render_template('futebol.html')

#GAMES
@app.route('/games')
def games():
    return render_template('games.html')

if __name__=="__main__":
    app.run(debug=True,port=5000)