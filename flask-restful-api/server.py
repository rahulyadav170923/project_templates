from flask_api.app import app
import sys, os
sys.path.append(os.getcwd()+'/flask_api')

app.run(debug=True)