# utils/alert_check.py

def should_alert(vitals):
    """
    Determines if an alert should be triggered based on vitals.
    
    Parameters:
        vitals (dict): {
            'heart_rate': int,
            'spo2': int,
            'temperature': float,
            'alcohol_level': float
        }
    
    Returns:
        alert (bool): Whether vitals are abnormal
        reasons (list): List of issues found
    """

    reasons = []

    # Heart rate check
    if vitals['heart_rate'] < 50 or vitals['heart_rate'] > 110:
        reasons.append(f"Abnormal Heart Rate: {vitals['heart_rate']} BPM")

    # SpO2 check
    if vitals['spo2'] < 92:
        reasons.append(f"Low Oxygen Level (SpO₂): {vitals['spo2']}%")

    # Temperature check
    if vitals['temperature'] > 100.4:
        reasons.append(f"Fever Detected: {vitals['temperature']}°F")

    # Alcohol detection
    if vitals['alcohol_level'] >= 0.02:
        reasons.append(f"Alcohol Detected: {vitals['alcohol_level']}%")

    alert = len(reasons) > 0
    return alert, reasons
