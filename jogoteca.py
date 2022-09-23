from flask import Flask, render_template

class Jogo:


  def __init__(self, nome, categoria, console):

     self.nome = nome
     self.categoria = categoria
     self.console = console
     
jogo1 = Jogo('Resident Evil', 'Survival Horror', 'Playstation')
jogo2 = Jogo('Kirby', 'Ação e plataforma', 'Nintendo')
jogo3 = Jogo('Silent Hill', 'Survival Horror', 'Playstation')


lista = [jogo1, jogo2, jogo3]

app = Flask(__name__)


@app.route('/inicio')


def ola():

  return render_template("lista.html", titulo='Meus jogos', jogos=lista)


app.run()

