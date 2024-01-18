from flask import Flask, render_template
from config import config

# routes
from routes import Product

app = Flask(__name__)

def page_not_found(error):
    return "<h1>Not Found page</h1>", 404

if __name__ == ('__main__'):
    app.config.from_object(config['development'])
    
    # Blueprints
    app.register_blueprint(Product.main, url_prefix='/home/products')
    
    # Error handlers
    app.register_error_handler(404, page_not_found)
    app.run()