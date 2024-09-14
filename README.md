Certainly! Here is the entire `README.md` content in Markdown format:

```markdown
# Event Management System

## Project Overview

The Event Management System is a simple web application built with Flask. It allows users to create, view, update, and delete events. The application also includes user authentication with different roles, where an admin can manage events, and a user can only view event details.

### Features
- Create, view, update, and delete events (Admin only).
- View event details (Available to all users).
- User authentication with roles (Admin and User).
- Simple login system with password protection.

## Requirements

This project requires the following Python packages:

- Flask
- Werkzeug

## Installation

1. **Clone the repository** (if applicable):
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Create a virtual environment** (recommended):
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install the dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

1. **Run the Flask application**:
   ```bash
   python app.py
   ```

2. **Open your web browser** and go to `http://127.0.0.1:5000/` to access the application.

## User Credentials

- **Admin**
  - Username: `admin`
  - Password: `12345`

- **User**
  - Username: `user`
  - Password: `12345`

## Project Structure

- `app.py`: The main application script containing routes and logic.
- `templates/`: Directory containing HTML templates.
  - `index.html`: The main page listing all events.
  - `create_event.html`: Form to create a new event.
  - `event.html`: Page to view event details.
  - `update_event.html`: Form to update an existing event.
  - `login.html`: Login page for user authentication.
- `passwords.txt`: File containing usernames and hashed passwords.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- Flask documentation
- Werkzeug documentation
```

### Instructions:
1. **Replace** `<repository-url>` and `<repository-directory>` with the appropriate values if you're cloning from a repository.
2. **Add** a `LICENSE` file or modify the License section if needed.
3. **Include** any additional details or instructions specific to your project if necessary.