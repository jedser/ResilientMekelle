import json
from datetime import datetime

# VISION Green Mobility Hub - Diagnostic Engine v1.0
# Developed for: PWD Technical Team (Mekelle, Tigray)
# Objective: Analyze EV Battery Health & Safety

def load_vehicle_data(vehicle_id):
    """
    Simulates connecting to the EV's On-Board Diagnostic (OBD) port.
    """
    print(f"Connecting to Vehicle ID: {vehicle_id}...")
    # In a real scenario, this reads from the OBD-II bluetooth dongle
    with open('data/diagnostic_sample.json', 'r') as file:
        return json.load(file)

def check_safety_thresholds(data):
    """
    Analyzes cell voltage to prevent fire hazards.
    """
    print("\n--- RUNNING SAFETY DIAGNOSTICS ---")
    cells = data['cells']
    safety_status = "SAFE"
    
    for cell in cells:
        if cell['voltage'] < 3.5:
            print(f"⚠️ ALERT: Cell {cell['id']} is UNDER-VOLTAGE ({cell['voltage']}V)")
            safety_status = "CRITICAL_MAINTENANCE_NEEDED"
        elif cell['voltage'] > 4.2:
             print(f"⚠️ ALERT: Cell {cell['id']} is OVER-VOLTAGE ({cell['voltage']}V)")
             safety_status = "WARNING"
        else:
            print(f"✅ Cell {cell['id']} is stable.")
            
    return safety_status

def generate_technician_report(status):
    """
    Generates a simplified report for the PWD Technician Tablet.
    """
    print("\n--- TECHNICIAN REPORT ---")
    print(f"Date: {datetime.now()}")
    print(f"System Status: {status}")
    
    if status != "SAFE":
        print("ACTION: Do not release vehicle. Initiate Cell Balancing Protocol.")
    else:
        print("ACTION: Vehicle approved for road use.")

# --- MAIN EXECUTION ---
if __name__ == "__main__":
    vehicle_data = load_vehicle_data("ET-MK-EV-004")
    safety_result = check_safety_thresholds(vehicle_data)
    generate_technician_report(safety_result)
