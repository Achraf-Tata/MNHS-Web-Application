# 🏥 MNHS-Web-Application

A comprehensive web-based database management system for the Moroccan National Health Services (MNHS). This application provides an intuitive interface for managing patients, appointments, medical inventory, and staff analytics.

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![Flask](https://img.shields.io/badge/flask-2.0+-green.svg)
![MySQL](https://img.shields.io/badge/mysql-8.0+-orange.svg)

## ✨ Features

- 📋 **Patient Management**: View and manage patient records with detailed information
- 📅 **Appointment Scheduling**: Schedule and track medical appointments
- 💊 **Inventory Tracking**: Monitor low stock medications and supplies with automatic alerts
- 📊 **Staff Analytics**: View appointment distribution and staff workload across hospitals
- 🎨 **Modern UI**: Clean and responsive interface design
- 🔐 **Secure**: CORS-enabled API with proper error handling

## 📋 Prerequisites

Before you begin, ensure you have the following installed:

- **Python 3.8 or higher** - [Download Python](https://www.python.org/downloads/)
- **MySQL 8.0 or higher** - [Download MySQL](https://dev.mysql.com/downloads/)
- **Git** (optional) - [Download Git](https://git-scm.com/downloads/)

## 🚀 Quick Start

### Option 1: Automated Setup (Recommended)

#### For Linux/Mac:

```bash
# Clone the repository
git clone https://github.com/yourusername/mnhs-database.git
cd mnhs-database

# Make scripts executable
chmod +x setup.sh run.sh

# Run setup
./setup.sh

# Configure your database credentials
nano .env  # or use your preferred text editor

# Run the application
./run.sh
```

#### For Windows:

```batch
# Clone the repository
git clone https://github.com/yourusername/mnhs-database.git
cd mnhs-database

# Run setup
setup.bat

# Configure your database credentials
notepad .env

# Run the application
run.bat
```

### Option 2: Manual Setup

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/mnhs-database.git
   cd mnhs-database
   ```

2. **Create Virtual Environment**
   ```bash
   # Linux/Mac
   python3 -m venv venv
   source venv/bin/activate

   # Windows
   python -m venv venv
   venv\Scripts\activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up MySQL Database**
   
   Create a privileged user for the MNHS database:
   ```sql
   CREATE DATABASE mnhs_database;
   CREATE USER 'mnhs_user'@'localhost' IDENTIFIED BY 'your_password';
   GRANT ALL PRIVILEGES ON mnhs_database.* TO 'mnhs_user'@'localhost';
   FLUSH PRIVILEGES;
   ```

5. **Configure Environment Variables**
   
   Create a `.env` file in the project root:
   ```env
   # MySQL Database Configuration
   MYSQL_HOST=localhost
   MYSQL_PORT=3306
   MYSQL_DB=mnhs_database
   MYSQL_USER=mnhs_user
   MYSQL_PASSWORD=your_password
   ```

6. **Run the Application**
   ```bash
   python app.py
   ```

7. **Access the Application**
   
   Open your browser and navigate to: `http://127.0.0.1:5000`

## 📁 Project Structure

```
MNHS-Web-Application/
│
├── app.py                    # Flask application entry point
├── ConnectionManager.py      # Database operations and queries
├── index.html               # Single-page application interface
├── requirements.txt         # Python dependencies
├── .env                     # Environment variables (create this)
├── .gitignore              # Git ignore file
├── setup.sh                # Linux/Mac setup script
├── setup.bat               # Windows setup script
├── run.sh                  # Linux/Mac run script
└── run.bat                 # Windows run script
```

## 🔧 Configuration

### Database Configuration

Edit the `.env` file with your MySQL credentials:

```env
MYSQL_HOST=localhost        # Database host
MYSQL_PORT=3306            # Database port
MYSQL_DB=mnhs_database     # Your database name
MYSQL_USER=mnhs_user       # Your MySQL username
MYSQL_PASSWORD=password    # Your MySQL password
```

### ConnectionManager Configuration

Update `ConnectionManager.py` to use environment variables:

```python
import os
from dotenv import load_dotenv
import mysql.connector

load_dotenv()

def get_connection():
    return mysql.connector.connect(
        host=os.getenv('MYSQL_HOST'),
        port=os.getenv('MYSQL_PORT'),
        user=os.getenv('MYSQL_USER'),
        password=os.getenv('MYSQL_PASSWORD'),
        database=os.getenv('MYSQL_DB')
    )
```

## 📊 Database Schema Requirements

Your MySQL database should have the following tables (matching the MNHS DB schema):

- **Patient**: Patient information (IID, FullName, Birth, Phone, etc.)
- **Staff**: Staff/doctor information (StaffID, FullName, etc.)
- **Hospital**: Hospital locations (HospitalID, HName, etc.)
- **Department**: Hospital departments (DepID, DeptName, etc.)
- **ClinicalActivity**: Clinical activities (CAID, Reason, etc.)
- **Appointment**: Appointment details (linking patients, staff, and activities)
- **Medication**: Medication catalog (MedicationID, MedicationName, etc.)
- **Stock**: Medication inventory per hospital (Quantity, ReorderLevel, etc.)

## 🎯 Features Guide

### 1. Patient Management
Navigate to the **Patients** tab to:
- View all patients sorted by last name
- See patient IDs, names, birth dates, and contact information
- Click "Load Patients" to refresh the list

### 2. Appointment Scheduling
Navigate to the **Schedule** tab to:
- Fill in appointment details:
  - **Clinical Activity ID (CAID)**: Unique identifier for the clinical activity
  - **Patient ID (IID)**: The patient's identification number
  - **Staff ID**: Medical staff member's ID
  - **Department ID**: Department where the appointment will take place
  - **Date & Time**: Appointment date and time
  - **Reason**: Brief description of the appointment purpose
- Click "Schedule Appointment" to confirm
- View success confirmation with appointment details

### 3. Inventory Management
Navigate to the **Stock** tab to:
- View medications below reorder levels
- See current stock quantities and reorder thresholds
- Identify manufacturers and hospital locations
- Red badges indicate out-of-stock items (Quantity = 0)
- Orange badges indicate low stock warnings

### 4. Staff Analytics
Navigate to the **Staff Share** tab to:
- View appointment distribution per staff member
- See workload percentages per hospital
- Identify staff with highest appointment loads
- Monitor resource allocation across facilities

## 🛠️ Troubleshooting

### Common Issues

**Issue: Foreign Key Constraint Error (1216)**
```
Error 1216 (23000): Cannot add or update a child row: a foreign key constraint fails
```
- **Solution**: Ensure all referenced IDs exist in their parent tables:
  - Patient ID exists in Patient table
  - Staff ID exists in Staff table
  - Department ID exists in Department table
  - Verify IDs before scheduling appointments

**Issue: "ModuleNotFoundError: No module named 'flask'"**
- **Solution**: Activate virtual environment and install dependencies
  ```bash
  source venv/bin/activate  # Linux/Mac
  venv\Scripts\activate     # Windows
  pip install -r requirements.txt
  ```

**Issue: "Can't connect to MySQL server"**
- **Solution**: Verify MySQL is running and credentials in `.env` are correct
  ```bash
  # Check if MySQL is running
  sudo service mysql status  # Linux
  brew services list         # Mac
  net start MySQL            # Windows
  ```

**Issue: "Access denied for user"**
- **Solution**: Check your MySQL username and password in the `.env` file
- Ensure the user has proper privileges

**Issue: "Failed to fetch" or CORS errors**
- **Solution**: 
  - Verify Flask server is running on port 5000
  - Check browser console for detailed errors
  - Clear browser cache and reload
  - Ensure CORS is properly configured in `app.py`

### Debug Mode

Enable detailed logging in `app.py`:
```python
if __name__ == "__main__":
    app.run(debug=True, host='127.0.0.1', port=5000)
```

Check console output for detailed error messages and request logs.

## 📝 API Endpoints

| Endpoint | Method | Description | Parameters |
|----------|--------|-------------|------------|
| `/` | GET | Serve the main HTML interface | - |
| `/patients` | GET | Retrieve list of patients | `limit` (optional, default: 20) |
| `/Appt` | POST | Schedule a new appointment | `caid`, `iid`, `staff_id`, `dep_id`, `date`, `time`, `reason` |
| `/inventory/low_stock` | GET | Get low stock medications | - |
| `/staff/share` | GET | Get staff appointment distribution | - |

### Example API Request

```javascript
// Schedule appointment
fetch('http://127.0.0.1:5000/Appt', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({
    caid: "CA001",
    iid: "P12345",
    staff_id: "S001",
    dep_id: 1,
    date: "2024-12-25",
    time: "14:30",
    reason: "Regular checkup"
  })
})
```

### .gitignore Configuration

```gitignore
# .gitignore
venv/
__pycache__/
*.pyc
.env
*.db
.DS_Store
*.log
```

## 👥 Authors

- Achraf Tata
- Taha Tahiri Alaoui
- Adam Yassine
- Noura Riahi El idrissi
- Mohamadou Taha Thiam

## 🙏 Acknowledgments

- Labs Provided by our teacher for project requirements
- Flask framework for backend infrastructure
- MySQL for database management

---
