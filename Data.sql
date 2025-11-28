--=====================================================--DML: Sample data for MNHS ( 5 rows per table)--Order respects FK dependencies--=====================================================--HOSPITAL
 INSERT INTO Hospital (HID, Name, City, Region) VALUES
 (1, 'Benguerir Central Hospital', 'Benguerir', 'Marrakech-Safi'),
 (2, 'Casablanca University Hospital', 'Casablanca',
 'Casablanca-Settat'),
 (3, 'Rabat Clinical Center', 'Rabat', 'Rabat-Sal-K nitra'),
 (4, 'Marrakech Regional Hospital', 'Marrakech',
 'Marrakech-Safi'),
 (5, 'Agadir City Hospital', 'Agadir', 'Souss-Massa');--DEPARTMENT
 INSERT INTO Department (DEP_ID, HID, Name, Specialty) VALUES
 (10, 1, 'Cardiology', 'Heart Care'),
 (11, 1, 'Pediatrics', 'Child Care'),
 (20, 2, 'Radiology', 'Imaging'),
 (30, 3, 'Oncology', 'Cancer Care'),
 (40, 4, 'Emergency', 'Acute Care'),
 (50, 5, 'Internal Medicine', 'General');--PATIENT
 INSERT INTO Patient (IID, CIN, FullName, Birth, Sex, BloodGroup, Phone) VALUES
 (1, 'CIN001', 'Sara El Amrani', '1999-04-10', 'F', 'A+', '0612345678'),
 (2, 'CIN002', 'Youssef Benali', '1988-09-22', 'M', 'O-', '0678912345'),
 (3, 'CIN003', 'Hajar Berrada', '1995-01-18', 'F', 'B+', '0600112233'),
 (4, 'CIN004', 'Ayoub El Khattabi', '1992-07-06', 'M', 'AB-', '0600223344'),
 (5, 'CIN005', 'Imane Othmani', '2001-03-30', 'F', 'O+', '0600334455');--STAFF
 INSERT INTO Staff (STAFF_ID, FullName, Status) VALUES
 (501, 'Dr. Amina Idrissi', 'Active'),
(502, 'Dr. Mehdi Touil', 'Active'),
 (503, 'Nurse Firdawse Guerbouzi', 'Active'),
 (504, 'Technician Omar Lahlou', 'Active'),
 (505, 'Dr. Khaoula Messari', 'Active');--INSURANCE
 INSERT INTO Insurance (InsID, Type) VALUES
 (100, 'CNOPS'),
 (101, 'CNSS'),
 (102, 'RAMED'),
 (103, 'Private'),
 (104, 'None');--MEDICATION
 INSERT INTO Medication (MID, Name, Form, Strength, ActiveIngredient, TherapeuticClass, Manufacturer) VALUES
 (1001, 'Amoxicillin', 'Tablet', '500mg', 'Amoxicillin', 'Antibiotic', 'PharmaMA'),
 (1002, 'Ibuprofen', 'Tablet', '400mg', 'Ibuprofen', 'Analgesic', 'MediCare'),
 (1003, 'Azithromycin', 'Tablet', '250mg', 'Azithromycin', 'Antibiotic', 'HealthCo'),
 (1004, 'Paracetamol', 'Syrup', '120mg/5ml', 'Acetaminophen', 'Analgesic', 'MediCare'),
 (1005, 'Ceftriaxone', 'Injection', '1g', 'Ceftriaxone', 'Antibiotic', 'PharmaMA');
 --CONTACTLOCATION
 INSERT INTO ContactLocation (CLID, City, Province, Street, Number, PostalCode, Phone_Location) VALUES
 (201, 'Benguerir', 'Rehamna', 'Avenue Mohammed VI', '12', '43150', '0523000001'),
 (202, 'Casablanca', 'Anfa', 'Bd Zerktouni', '77', '20000', '0522000002'),
 (203, 'Rabat', 'Agdal', 'Rue Oued Ziz', '5', '10000', '0537000003'),
 (204, 'Marrakech', 'Gueliz', 'Rue de la Libert ', '9', '40000', '0524000004'),
 (205, 'Agadir', 'Cit Dakhla', 'Rue Al Atlas', '3', '80000', '0528000005');--have
 INSERT INTO have (IID, CLID) VALUES
 (1, 201),
 (1, 202),
 (2, 202),
 (3, 203),
 (4, 204),
 (5, 205);--Work_in

INSERT INTO Work_in (STAFF_ID, DEP_ID) VALUES
 (501, 10),
 (502, 10),
 (503, 11),
 (504, 20),
 (505, 40),
 (501, 30);--ClinicalActivity--Appointments
 INSERT INTO ClinicalActivity (CAID, IID, STAFF_ID, DEP_ID, Date,
 Time) VALUES
 (1001, 1, 501, 10, '2025-10-10', '10:00:00'),
 (1002, 2, 502, 10, '2025-10-12', '11:00:00'),
 (1003, 3, 503, 11, '2025-10-15', '09:30:00'),
 (1004, 4, 504, 20, '2025-10-20', '14:00:00'),
 (1005, 5, 505, 40, '2025-10-22', '16:15:00');--Emergencies
 INSERT INTO ClinicalActivity (CAID, IID, STAFF_ID, DEP_ID, Date,
 Time) VALUES
 (1011, 1, 505, 40, '2025-10-25', '01:10:00'),
 (1012, 2, 501, 40, '2025-10-26', '02:25:00'),
 (1013, 3, 502, 40, '2025-10-27', '03:05:00'),
 (1014, 4, 503, 40, '2025-10-28', '05:40:00'),
 (1015, 5, 504, 40, '2025-10-29', '06:55:00');--Appointment
 INSERT INTO Appointment (CAID, Reason, Status) VALUES
 (1001, 'Routine check-up', 'Scheduled'),
 (1002, 'Follow-up imaging', 'Completed'),
 (1003, 'Pediatric visit', 'Cancelled'),
 (1004, 'X-ray review', 'Scheduled'),
 (1005, 'Triage follow-up', 'Completed');--Emergency
 INSERT INTO Emergency (CAID, TriageLevel, Outcome) VALUES
 (1011, 3, 'Admitted'),
 (1012, 2, 'Discharged'),
 (1013, 4, 'Transferred'),
 (1014, 5, 'Admitted'),
 (1015, 1, 'Discharged');--Expense
 INSERT INTO Expense (ExpID, InsID, CAID, Total) VALUES
 (9001, 100, 1001, 250.00),
 (9002, 101, 1002, 400.00),
 (9003, 103, 1011, 1200.00),
 (9004, 104, 1012, 80.00),
 (9005, 102, 1004, 150.00);
--Prescription
 INSERT INTO Prescription (PID, CAID, DateIssued) VALUES
 (8001, 1001, '2025-10-10'),
 (8002, 1002, '2025-10-12'),
 (8003, 1004, '2025-10-20'),
 (8004, 1011, '2025-10-25'),
 (8005, 1013, '2025-10-27');--Includes (
 INSERT INTO Includes (PID, MID, Dosage, Duration) VALUES
 (8001, 1001, '1 tab BID', '5 days'),
 (8001, 1002, '1 tab PRN', '3 days'),
 (8002, 1003, '1 tab OD', '3 days'),
 (8003, 1004, '10 ml Q6H', '2 days'),
 (8004, 1005, '1 g IV', '1 day'),
 (8005, 1002, '1 tab TID', '4 days');--Stock (Inventory)
 INSERT INTO Stock (HID, MID, StockTimestamp, UnitPrice, Qty, ReorderLevel) VALUES
 (1, 1001, '2025-10-10 08:00:00', 22.00, 120, 20),
 (1, 1002, '2025-10-10 08:00:00', 6.50, 300, 50),
 (2, 1003, '2025-10-12 08:00:00', 35.00, 80, 15),
 (3, 1004, '2025-10-15 08:00:00', 4.00, 500, 60),
 (4, 1005, '2025-10-20 08:00:00', 120.00, 40, 10);--=====================================================--Updates--=====================================================--Update a patients phone number (e.g., IID = 1)
 UPDATE Patient
 SET Phone = '0611111111'
 WHERE IID = 1;--Update a hospitals region (e.g., HID = 2)
 
 UPDATE Hospital
 SET Region = 'Grand Casablanca'
 WHERE HID = 2;--=====================================================--Delete: remove a cancelled appointment--(we inserted CAID = 1003 with Status = 'Cancelled')
 
 DELETE FROM Appointment
 WHERE CAID = 1003
 AND Status = 'Cancelled';