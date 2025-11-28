from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
from ConnectionManager import (
    list_patients_ordered_by_last_name,
    insert_patient,
    schedule_appointment,
    get_low_stock,
    get_staff_share,get_upcoming_appt,get_total_staff,get_total_patients,get_total_upcoming_appointements
)

app = Flask(__name__)
#.\.venv\Scripts\python.exe app.py
CORS(app, resources={
    r"/*": {
        "origins": "*",
        "methods": ["GET", "POST", "OPTIONS"],
        "allow_headers": ["Content-Type"]
    }
})



@app.route("/")
def serve_html():
    return send_file('index.html')



@app.route("/patients", methods=['GET', 'OPTIONS'])
def api_list_patients():
    if request.method == 'OPTIONS':
        return '', 204
    
    limit = request.args.get("limit", default=20, type=int)
    try:
        rows = list_patients_ordered_by_last_name(limit)
        return jsonify(rows), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/getAppt", methods=['GET', 'OPTIONS'])
def api_get_upcoming_appt():
    if request.method == 'OPTIONS':
        return '', 204
    
    try:
        rows = get_upcoming_appt()
        return jsonify(rows), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/inventory/low_stock", methods=['GET', 'OPTIONS'])
def api_low_stock():
    if request.method == 'OPTIONS':
        return '', 204
        
    try:
        rows = get_low_stock()
        return jsonify(rows), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/staff/share", methods=['GET', 'OPTIONS'])
def api_staff_share():
    if request.method == 'OPTIONS':
        return '', 204
        
    try:
        rows = get_staff_share()
        return jsonify(rows), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/Appt", methods=['POST', 'OPTIONS'])
def api_make_appt():
    if request.method == 'OPTIONS':
        return '', 204
    
    try:
        data = request.get_json()
        required_fields = ['caid', 'iid', 'staff_id', 'dep_id', 'date', 'time', 'reason']
        for field in required_fields:
            if field not in data:
                return jsonify({"error": f"Missing required field: {field}"}), 400
        
        result = schedule_appointment(
            caid=data['caid'],
            iid=data['iid'],
            staff_id=data['staff_id'],
            dep_id=data['dep_id'],
            date_str=data['date'],
            time_str=data['time'],
            reason=data['reason']
        )
        
        return jsonify({
            "success": True,
            "message": "Appointment scheduled successfully",
            "data": result
        }), 200
        
    except Exception as e:
        print(f"Error in /Appt: {str(e)}")
        return jsonify({"error": str(e)}), 500

@app.route("/RegPatient", methods=['POST', 'OPTIONS'])
def api_reg_patient():
    if request.method == 'OPTIONS':
        return '', 204
    
    try:
        data = request.get_json()
        required_fields = ['iid', 'cin', 'full_name', 'birth', 'sex', 'blood', 'phone']
        for field in required_fields:
            if field not in data:
                return jsonify({"error": f"Missing required field: {field}"}), 400
        
        result = insert_patient(
            iid=data['iid'],
            cin=data['cin'],
            full_name=data['full_name'],
            birth=data['birth'],
            sex=data['sex'],
            blood=data['blood'],
            phone=data['phone']
        )
        
        return jsonify({
            "success": True,
            "message": "Patient registered successfully",
            "data": result
        }), 200
        
    except Exception as e:
        print(f"Error in /Appt: {str(e)}")
        return jsonify({"error": str(e)}), 500

@app.route("/total/staffs", methods=['GET', 'OPTIONS'])
def api_get_total_staffs():
    if request.method == 'OPTIONS':
        return '', 204
    try:
        row = get_total_staff()
        return jsonify(row), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/total/patients", methods=['GET', 'OPTIONS'])
def api_get_total_patients():
    if request.method == 'OPTIONS':
        return '', 204
    try:
        row = get_total_patients()
        return jsonify(row), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/total/upcAppts", methods=['GET', 'OPTIONS'])
def api_get_total_upcAppt():
    if request.method == 'OPTIONS':
        return '', 204
    try:
        row = get_total_upcoming_appointements()
        return jsonify(row), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    print("=" * 60)
    print("🚀 Flask server started!")
    print("📱 Open your browser and go to: http://127.0.0.1:5000")
    print("=" * 60)
    app.run(debug=True, host='127.0.0.1', port=5000)