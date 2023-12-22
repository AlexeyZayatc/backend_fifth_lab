from flask import Flask
app = Flask(__name__)
# здесь должны импортироваться все программы-контроллеры,
# размещенные в папке controllers

import controllers.hello
import controllers.index
import controllers.subject

