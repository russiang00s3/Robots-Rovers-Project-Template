# hal/pin_config.py
# All Raspberry Pi pin assignments for the rover.
#
# BOARD numbering — these numbers refer to the physical pin
# positions on the 40-pin GPIO header, NOT BCM/GPIO numbers.
# Pin 1 is the 3.3V pin in the top-left corner of the header.
# Reference: https://pinout.xyz  (select "BOARD" numbering)
#
# Rules for this file:
#   ✅ Constants only — ALL_CAPS names
#   ✅ BOARD pin numbers only
#   ❌ No imports of any library
#   ❌ No functions, classes, or logic of any kind

# ── Status LED ────────────────────────────────────────────────
# Wiring: BOARD Pin 11 → 330Ω resistor → LED anode → LED cathode → GND
STATUS_LED = 11       # BOARD 11  (BCM 17)

# ── Left Motor (L298N channel A) ──────────────────────────────
# Wiring: ENA controls speed (PWM), IN1/IN2 control direction
MOTOR_LEFT_ENA = 32   # BOARD 32  (BCM 12) — PWM speed
MOTOR_LEFT_IN1 = 36   # BOARD 36  (BCM 16) — direction pin A
MOTOR_LEFT_IN2 = 38   # BOARD 38  (BCM 20) — direction pin B

# ── Right Motor (L298N channel B) ─────────────────────────────
MOTOR_RIGHT_ENB = 33  # BOARD 33  (BCM 13) — PWM speed
MOTOR_RIGHT_IN3 = 37  # BOARD 37  (BCM 26) — direction pin A
MOTOR_RIGHT_IN4 = 40  # BOARD 40  (BCM 21) — direction pin B

# ── HC-SR04 Ultrasonic Sensor ─────────────────────────────────
# ⚠️  ECHO outputs 5V — use a voltage divider before Pi GPIO input
ULTRASONIC_TRIG = 16  # BOARD 16  (BCM 23) — trigger output
ULTRASONIC_ECHO = 18  # BOARD 18  (BCM 24) — echo input (via divider)
