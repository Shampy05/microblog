from app import app, db
from app.models import User, Post
import sqlalchemy as sa
import sqlalchemy.orm as orm

@app.shell_context_processor
def make_shell_context():
    """Create a shell context for the Flask application."""
    return {'db': db, 'User': User, 'Post': Post, 'orm': orm, 'sa': sa}