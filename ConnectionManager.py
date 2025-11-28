import os
from dotenv import load_dotenv
import mysql.connector
from mysql.connector import errorcode

load_dotenv()

cfg = dict(
host=os.getenv("MYSQL_HOST"),
port=int(os.getenv("MYSQL_PORT", 3306)),
database=os.getenv("MYSQL_DB"),
user=os.getenv("MYSQL_USER"),
password=os.getenv("MYSQL_PASSWORD"),
)

def get_connection():
    return mysql.connector.connect(**cfg)
def list_patients_ordered_by_last_name(limit=20):
    sql = """
        SELECT IID, FullName,Birth,Phone
        FROM Patient
        ORDER BY SUBSTRING_INDEX(FullName, ' ',-1), FullName
        LIMIT %s
 """
    with get_connection() as cnx:
        with cnx.cursor(dictionary=True) as cur:
            cur.execute(sql, (limit,))
            return cur.fetchall()
def insert_patient(iid, cin, full_name, birth, sex, blood, phone):
    sql = """
    INSERT INTO Patient(IID, CIN, FullName, Birth, Sex, BloodGroup, Phone)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    """
    with get_connection() as cnx:
        try:
            with cnx.cursor() as cur:
                cur.execute(sql, (iid, cin, full_name, birth, sex, blood, phone))
                cnx.commit()
        except Exception:
            cnx.rollback()
            raise

def schedule_appointment(caid, iid, staff_id, dep_id, date_str, time_str, reason):
    ins_ca = """
    INSERT INTO ClinicalActivity(CAID, IID, STAFF_ID, DEP_ID, Date, Time)
    VALUES (%s , %s , %s , %s , %s , %s )
    """
    ins_appt = """
    INSERT INTO Appointment(CAID, Reason, Status)
    VALUES (%s , %s , 'Scheduled')
    """
    with get_connection() as cnx:
        try:
            with cnx.cursor() as cur:
                cur.execute(ins_ca, (caid, iid, staff_id, dep_id, date_str, time_str))
                cur.execute(ins_appt, (caid, reason))
            cnx.commit()
        except Exception:
            cnx.rollback()
            raise

def get_low_stock():
    sql = """
        SELECT
            h.HID,
            h.Name AS HospitalName,
            m.MID,
            m.Name AS MedicationName,
            COALESCE(s.Qty, 0) AS Quantity,
            COALESCE(s.ReorderLevel, 10) AS ReorderLevel,
            m.Manufacturer
        FROM Medication m
        LEFT JOIN Stock s ON s.MID = m.MID
        JOIN Hospital h ON s.HID = h.HID
        WHERE COALESCE(s.Qty, 0) < COALESCE(s.ReorderLevel, 10)
        ORDER BY h.HID, m.Name
    """
    cnx=get_connection()
    with cnx.cursor(dictionary=True) as cur:
        cur.execute(sql)
        return cur.fetchall()


def get_staff_share():
    sql="""
    WITH staff_hosp AS (
        SELECT S.FullName, d.HID, COUNT(*) AS n,h.Name as HName
        FROM Appointment a
        JOIN ClinicalActivity c ON c.CAID = a.CAID
        JOIN Department d ON d.DEP_ID = c.DEP_ID
        JOIN Staff S ON S.STAFF_ID=c.STAFF_ID
        JOIN Hospital h ON h.HID=d.HID
        GROUP BY c.STAFF_ID, d.HID
    ),
    hosp_tot AS (
        SELECT d.HID, COUNT(*) AS n
        FROM Appointment a
        JOIN ClinicalActivity c ON c.CAID = a.CAID
        JOIN Department d ON d.DEP_ID = c.DEP_ID
        GROUP BY d.HID
    )

    SELECT sh.FullName, sh.HID, sh.n AS TotalAppointments,sh.HName,
    ROUND(100 * sh.n / ht.n, 2) AS PctOfHospital
    
    FROM staff_hosp sh
    JOIN hosp_tot ht ON ht.HID = sh.HID;
    GROUP BY sh.HID
    ORDER BY PctOfHospital DESC
    """
    cnx=get_connection()
    with cnx.cursor(dictionary=True) as cur:
        cur.execute(sql)
        return cur.fetchall()

def get_upcoming_appt():
    sql = """
SELECT 
    a.CAID,
    a.Status,
    s.FullName AS StaffName,
    p.FullName AS PatientName,
    p.IID AS PatientID,
    dep.Name AS DName,
    h.Name AS HName,
    DATE(c.Date) AS ApptDate
    FROM Appointment a
    JOIN ClinicalActivity c ON c.CAID = a.CAID
    JOIN Staff s ON s.STAFF_ID = c.STAFF_ID
    JOIN Patient p ON p.IID = c.IID
    JOIN Department dep ON dep.DEP_ID=c.DEP_ID
    JOIN Hospital h ON h.HID=dep.HID
    WHERE a.Status = 'Scheduled'
    AND c.Date>=CURDATE()
    ORDER BY c.Time ASC;

    """
    
    cnx = get_connection()
    with cnx.cursor(dictionary=True) as cur:
        cur.execute(sql)
        return cur.fetchall()

def get_total_staff():
    sql = """
    SELECT COUNT(*) AS TotalStaff FROM Staff;
    """
    cnx = get_connection()
    with cnx.cursor(dictionary=True) as cur:
        cur.execute(sql)
        return cur.fetchone()
def get_total_patients():
    sql = """
    SELECT COUNT(*) AS TotalPatients FROM Patient ;
    """
    cnx = get_connection()
    with cnx.cursor(dictionary=True) as cur:
        cur.execute(sql)
        return cur.fetchone()
def get_total_upcoming_appointements():
    sql = """
            SELECT COUNT(*) AS UpcomingAppointments
            FROM Appointment a
            JOIN ClinicalActivity c ON c.CAID = a.CAID
            WHERE a.Status = 'Scheduled'
            AND c.Date >= CURDATE();
        """
    cnx = get_connection()
    with cnx.cursor(dictionary=True) as cur:
        cur.execute(sql)
        return cur.fetchone()

if __name__ == "__main__":
    for row in list_patients_ordered_by_last_name():
        print(f"{row['IID']} {row['FullName']}")