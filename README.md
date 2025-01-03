# Law Office Management System

## Video Demo
Explore the project functionality and user interface in this video:
[Watch on YouTube](https://youtu.be/pE9l5p8BmF0?si=xm6PdlSeR2sRZNdv)

---

## Overview
The **Law Office Management System** is a bilingual (Persian and English) desktop application designed to help law offices efficiently manage their operations. Built using Python's Tkinter and CustomTkinter libraries, this application provides functionalities for client registration, case management, appointment scheduling, and reporting. The system follows a three-layer architecture to ensure modularity and scalability.

---

## Features

1. **Bilingual Interface:**
   - Supports Persian and English languages.
   - Easy language switching for better accessibility.

2. **Client Management:**
   - Register new clients with details such as full name, contact number, and address.
   - Manage case-related information, including case type and status.

3. **Appointment Scheduling:**
   - Schedule and manage appointments for clients.
   - View appointment history and associated cases.

4. **Role-Based Access Control:**
   - Separate roles for managers and employees.
   - Restricted access to specific features based on roles.

5. **Reporting:**
   - Generate and display reports on client cases and appointment statuses.

6. **Interactive Search:**
   - Dynamic search suggestions for easier data retrieval.
   - Filter and view data in tabular format.

---

## Requirements

- Python 3.8 or higher
- SQL Server (for database connection)
- Internet connection for dependencies

---

## Project Structure

### Files and Directories:
- **`project.py`**: Main application file containing the GUI and logic implementation.
- **`BE/`**: Backend layer for database interaction and data management.
  - `Law.py`: Handles data models for cases, appointments, and client information.
- **`BLL/`**: Business logic layer.
  - `Rules.py`: Contains business rules and database repository logic.
- **`requirements.txt`**: List of dependencies for the project.
- **`design.png`**, **`img2.png`**, **`c5.png`**: Images used in the application.

---

## Setup and Installation

1. **Ensure SQL Server is running:**
   - Create a database and tables as required by the project.
   - Update database credentials in the `config.py` file.

2. **Clone the Repository:**
   ```bash
   git clone https://github.com/Maryam-tli/law_office_project.git
   cd law_office_project
   ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application:**
   ```bash
   python project.py
   ```

---

## Usage Instructions

1. Launch the application.
2. Use the **Login Panel** to log in as a manager or employee.
3. Navigate through the menus for:
   - **Client Management:** Add, update, or delete client details.
   - **Appointments:** Schedule and view appointments.
   - **Reports:** Generate detailed case or appointment reports.
4. Use the **Language Menu** to switch between Persian and English.

---

## Dependencies

The following libraries are required to run this application:
- **Tkinter**: GUI framework for building the interface.
- **CustomTkinter**: Enhanced widgets and themes for Tkinter.
- **Datetime**: Managing date and time operations.
- **Pytest** (optional): For testing functions and modules.

Install these dependencies using `pip` as mentioned in the setup section.

---

## Future Enhancements

1. Integration with a cloud-based database for remote access.
2. Enhanced reporting features with export options (e.g., PDF, Excel).
3. User activity logs for better accountability.
4. Advanced role management with custom permissions.

---

## Credits and Contact

Developed by: **Maryam**

For more details, contributions, or questions, please visit the [GitHub repository](https://github.com/Maryam-tli/law_office_project) or email me at **your-email@example.com**.

