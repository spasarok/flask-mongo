from flask import Flask

app = Flask(__name__)

import api.routes.home
import api.routes.stores
import api.routes.users
