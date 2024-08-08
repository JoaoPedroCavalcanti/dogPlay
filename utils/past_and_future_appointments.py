from datetime import datetime


def checkIfAppointmentIsOld(appointment):
    now = datetime.now()
    now_date = now.date()
    now_time = now.time()
    
    
    appointment_date = appointment.date
    appointment_time = appointment.time
    
    if appointment_date < now_date:
        return True
    if appointment_time < now_time:
        return True
    return False

def past_and_future_appointments(appointments):
    past_appointments = []
    future_appointments = []
    for appointment in appointments:
        if checkIfAppointmentIsOld(appointment):
            past_appointments.append(appointment)
        else:
            future_appointments.append(appointment)
        
    return past_appointments, future_appointments
    
