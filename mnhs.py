import argparse
from ConnectionManager import list_patients_ordered_by_last_name, schedule_appointment,get_low_stock,get_staff_share
def main():
    parser = argparse.ArgumentParser(description="MNHS CLI")
    sub = parser.add_subparsers(dest="cmd", required=True)
    
    sub.add_parser("list_patients")
    
    sub.add_parser("low_stock")
    
    sub.add_parser("staff_share")

    appt = sub.add_parser("schedule_appt", help="Schedule a new appointment")
    appt.add_argument("--caid", type=int, required=True)
    appt.add_argument("--iid", type=int, required=True)
    appt.add_argument("--staff", type=int, required=True)
    appt.add_argument("--dep", type=int, required=True)
    appt.add_argument("--date", required=True) # YYYY-MM-DD
    appt.add_argument("--time", required=True) # HH:MM:SS
    appt.add_argument("--reason", required=True)

    args = parser.parse_args()
    
    if args.cmd == "list_patients":
        for r in list_patients_ordered_by_last_name():
            print(f"{ r['IID']} { r['FullName']} ")
    
    elif args.cmd == "schedule_appt":
        print("__________ Scheduling Appointement .... ... .. .")
        schedule_appointment(args.caid, args.iid, args.staff, args.dep,args.date, args.time, args.reason)
        print("Appointment scheduled")
    elif args.cmd == "low_stock":
        print("__________ Generating Low Stock Report : .... ... .. .")
        for row in get_low_stock():
            print(f"{row['HID']}    |   {row['HospitalName']}    |   {row['MID']}    |   {row['MedicationName']}    |   {row['Quantity']}    |   {row['ReorderLevel']}")
    elif args.cmd == "staff_share":
        print("__________ Generating Staff Percentage Share Report : .... ... .. .")
        for row in get_staff_share():
            print(f"{row['FullName']}    |   {row['HName']}    |   {row['TotalAppointments']}    |   {row['PctOfHospital']} %")
    

if __name__ == "__main__":
    main()
