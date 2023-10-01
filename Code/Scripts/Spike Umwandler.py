''' Importe für Spike und umwandler '''
import spike
import tenserflow as tf

''' Importe für Spike'''
motor_module = spike.Motor('A')
motor_pair = spike.MotorPair('c', 'B')
color_sensor = spike.ColorSensor('E')	
distance_sensor = spike.DistanceSensor('F')
force_sensor = spike.ForceSensor('D')
calibration = 0


# def AREA

def drive_forward(distance):
	motor_pair.move(distance - calibration, 'cm')


def calibrate_driving():
	a = distance_sensor.get_distance_cm()
	motor_pair.move(10, 'cm')
	b = distance_sensor.get_distance_cm()
	calibration = a - b
	print(calibration)


def turn_left(angle):
	motor_pair.move(angle, 'degrees')


def turn_right(angle):
	motor_pair.move(angle, 'degrees')


def drive_backward(distance):
	motor_pair.move(distance - calibration, 'cm')


def drive_until_obstacle(speed):
	while distance_sensor.get_distance_cm() > 5:
		motor_pair.start(speed, speed)
	motor_pair.stop()


def drive_until_color(color, speed):
	while color_sensor.get_color() != color:
		motor_pair.start(speed, speed)
	motor_pair.stop()


def switch_module(switch):
	while switch == False:
		if force_sensor.is_pressed():
			switch = True
			return switch


def ai_control(Weg_daten):
	# Hier kommt der AI Code hin PPO AI für optimisierung des vorgedachten Weges
	pass


def main():
	# Hier kommt der Code hin
	pass


if __name__ == '__main__':
	main()