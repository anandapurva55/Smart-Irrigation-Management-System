import pyfirmata

soil_moisture_Sensor = 9
water_motor = 8

board = pyfirmata.Arduino("/dev/ttyACM0")

while True:
    int a = board.digital[soil_moisture_Sensor].read(0)
    if a > 500:
      board.digital[water_motor].write(1)
    board.pass_time(1)
