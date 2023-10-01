''' Importe für Spike und umwandler '''
import spike


''' Importe für Spike'''
motor_module = spike.Motor('A')
motor_pair = spike.MotorPair('c', 'B')
color_sensor = spike.ColorSensor('E')	
distance_sensor = spike.DistanceSensor('F')
force_sensor = spike.ForceSensor('D')



# def AREA

def drive_forward(distance):
    motor_pair.start_tank(100, 100)
	
	while distance_sensor.get_distance_cm() > distance:
		pass
	motor_pair.stop()