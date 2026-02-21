"""
FLIGHT RISK AI - LOGIC ENGINE
================================================================================
This module evaluates flight delays against traveler archetypes to determine
at what point a delay becomes a "tipping point" for a specific persona.

REFERENCE DATA (Personas):
--------------------------
1. THE EXECUTIVE: Tipping Point > 30 mins (🏢 Executive / Business Pro)
2. THE STUDENT: Tipping Point > 12 hours (🎒 Student / Young Traveler)
3. THE PARENT: Tipping Point > 60 mins (🧸 Family / Parent)
... (Full details available in personas.txt)
"""

from personas import PERSONAS

def evaluate_delay(persona_key, delay_minutes):
    """
    Evaluates the impact of a flight delay based on the traveler's persona.
    Returns status, severity, and persona-specific strategy recommendations.
    """
    persona = PERSONAS.get(persona_key)
    if not persona:
        return {
            "status": "Unknown",
            "severity": "Unknown",
            "coping_style": "Stay calm.",
            "flight_strategy": "Consult airline staff.",
            "insurance": {"name": "N/A", "focus": "N/A", "payout": "N/A", "fine_print": "N/A"}
        }

    tipping_point = persona["tipping_point_minutes"]
    
    # Calculate Severity and Status based on the Tipping Point
    if delay_minutes == 0:
        status = "On Time"
        severity = "None"
    elif delay_minutes < tipping_point:
        status = "Managing"
        severity = "Low"
    elif delay_minutes < tipping_point * 2:
        status = "Tipping Point Reached"
        severity = "Medium"
    elif delay_minutes < 720: # 12 hours
        status = "Crisis Mode"
        severity = "High"
    else:
        status = "Total System Failure"
        severity = "Critical"

    return {
        "status": status,
        "severity": severity,
        "coping_style": persona["coping_style"],
        "flight_strategy": persona["flight_strategy"],
        "insurance": persona["insurance"]
    }