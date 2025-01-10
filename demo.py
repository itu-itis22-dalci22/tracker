import RPi.GPIO as GPIO
import time

# Pin tanımlamaları (BCM pin numaraları kullanılıyor)
DIR_PIN = 21   # Yön pini
STEP_PIN = 19  # Step pini
MS1_PIN = 29   # MS1 pini
MS2_PIN = 31   # MS2 pini
MS3_PIN = 33  # MS3 pini

# GPIO ayarları
GPIO.setmode(GPIO.BCM)
GPIO.setup(DIR_PIN, GPIO.OUT)
GPIO.setup(STEP_PIN, GPIO.OUT)
GPIO.setup(MS1_PIN, GPIO.OUT)
GPIO.setup(MS2_PIN, GPIO.OUT)
GPIO.setup(MS3_PIN, GPIO.OUT)

# Yarım adım modunu ayarla (MS1 = HIGH, MS2 = LOW, MS3 = LOW)
GPIO.output(MS1_PIN, GPIO.HIGH)
GPIO.output(MS2_PIN, GPIO.LOW)
GPIO.output(MS3_PIN, GPIO.LOW)

def move_motor(steps, direction):
    """
    Step motorunu verilen adım sayısı ve yön ile hareket ettirir.

    :param steps: Atılacak adım sayısı
    :param direction: Yön (True: İleri, False: Geri)
    """
    # Yönü ayarla
    GPIO.output(DIR_PIN, GPIO.HIGH if direction else GPIO.LOW)

    for _ in range(steps):
        GPIO.output(STEP_PIN, GPIO.HIGH)
        time.sleep(0.001)  # 1000 mikrosaniye (adım süresi ayarlanabilir)
        GPIO.output(STEP_PIN, GPIO.LOW)
        time.sleep(0.001)

try:
    while True:
        # 1 saniye ileri hareket
        move_motor(200, True)  # 200 adım ileri git
        time.sleep(1)  # 1 saniye bekle

        # 1 saniye geri hareket
        move_motor(200, False)  # 200 adım geri git
        time.sleep(1)  # 1 saniye bekle

except KeyboardInterrupt:
    print("\nÇıkış yapılıyor...")

finally:
    GPIO.cleanup()