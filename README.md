# Microblog Flask Application

This is a simple microblog web application built using Flask. The project structure and features implemented so far are as follows:

## Project Structure

```
config.py
microblog.py
app/
    __init__.py
    forms.py
    routes.py
    templates/
        base.html
        index.html
        login.html
```

## Features Implemented

- **Flask Application Factory**: The main Flask app is created in `app/__init__.py` and imported in `microblog.py`.
- **Configuration**: App configuration is managed in `config.py`.
- **Routing**: Application routes are defined in `app/routes.py`.
- **Forms**: WTForms are defined in `app/forms.py` for handling user input.
- **Templates**: Jinja2 templates are used for rendering HTML pages. The templates include:
  - `base.html`: The base template for the site layout.
  - `index.html`: The homepage template.
  - `login.html`: The login page template.

## How to Run

1. **Install dependencies** (if not already installed):
   ```bash
   pip install flask
   pip install flask-wtf
   ```

2. **Run the application**:
   ```bash
   export FLASK_APP=microblog.py
   flask run
   ```
   Or, you can run directly with Python:
   ```bash
   python microblog.py
   ```

## Notes
- The application uses a simple structure suitable for learning Flask basics.
- All templates are located in the `app/templates/` directory.
- The project is ready for further development, such as adding a database, user authentication, and more features.

---

Feel free to extend this project as needed!
