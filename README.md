# Smart Blind Stick Using Arduino

An Arduino-based assistive device designed to help visually impaired people navigate safely by detecting obstacles and providing audio alerts using an ultrasonic sensor and buzzer.

## 📌 Project Overview

The Smart Blind Stick is an innovative and low-cost navigation aid for visually impaired individuals. It uses an ultrasonic sensor to detect nearby obstacles and alerts the user through sound notifications, enabling safer and more independent movement.

The system is designed to:
- Detect obstacles in real time
- Provide audio feedback through a buzzer
- Assist visually impaired people in navigating independently
- Offer a low-cost and lightweight solution

---

## 🚀 Features

- Obstacle detection using an HC-SR04 Ultrasonic Sensor
- Audio alert system using a buzzer
- LED indication for system status
- Low power consumption
- Lightweight and portable design
- Easy to build and cost-effective

---

## 🛠️ Components Required

| Component | Quantity |
|-----------|-----------|
| Arduino UNO | 1 |
| HC-SR04 Ultrasonic Sensor | 1 |
| Piezo Buzzer | 1 |
| LED | 1 |
| 9V Battery | 1 |
| Connecting Wires | As required |
| Breadboard | 1 |

---

## 🔌 Circuit Connections

### Ultrasonic Sensor (HC-SR04)

| HC-SR04 Pin | Arduino UNO Pin |
|-------------|------------------|
| VCC | 5V |
| GND | GND |
| TRIG | Pin 4 |
| ECHO | Pin 5 |

### Other Components

| Component | Arduino Pin |
|-----------|--------------|
| Buzzer | Pin 7 |
| LED | Pin 9 |

---

## ⚙️ Working Principle

1. The ultrasonic sensor continuously emits ultrasonic waves.
2. The waves bounce back after hitting an obstacle.
3. Arduino calculates the distance using the echo time.
4. If the obstacle is within the predefined safety distance, the buzzer is activated.
5. The user receives an audio alert and can avoid the obstacle.

---

## 💻 Arduino Code

```cpp
const int trigPin1 = 4;
const int echoPin1 = 5;
const int buzzer = 7;
const int led = 9;

long duration1;
int distance1;
int safetyDistance = 100;

void setup() {
  pinMode(trigPin1, OUTPUT);
  pinMode(echoPin1, INPUT);
  pinMode(buzzer, OUTPUT);
  pinMode(led, OUTPUT);

  Serial.begin(9600);
}

void loop() {
  digitalWrite(led, HIGH);

  digitalWrite(trigPin1, LOW);
  delayMicroseconds(5);

  digitalWrite(trigPin1, HIGH);
  delayMicroseconds(15);

  duration1 = pulseIn(echoPin1, HIGH);
  distance1 = duration1 * 0.034 / 2;

  if (distance1 <= safetyDistance) {
    digitalWrite(buzzer, HIGH);
  }
  else {
    digitalWrite(buzzer, LOW);
  }

  Serial.print("Distance: ");
  Serial.print(distance1);
  Serial.println(" cm");

  delay(500);
}
```

---

## 📊 Applications

- Navigation assistance for visually impaired individuals
- Obstacle detection systems
- Automotive parking sensors
- Robotics and autonomous systems
- Safety and warning systems

---

## 🔮 Future Enhancements

- Integration of Bluetooth module
- GPS tracking for emergency situations
- Voice instruction module
- Soil moisture detection for safer navigation
- AI-based image recognition and collision detection
- Mobile application integration

---

## 📷 Project Architecture

```
Ultrasonic Sensor → Arduino UNO → Buzzer/LED → User Alert
```

---

## 🎯 Advantages

- Low cost
- Easy to implement
- Portable and lightweight
- Real-time obstacle detection
- Improves independence and safety for visually impaired users

---

## 📚 References

- IEEE Maker Project – Smart Stick for the Blind
- IJERT – Smart Blind Stick Using Arduino
- ICACCS Conference Papers on Smart Blind Stick
- ICCES Conference Papers on Multi-Functional Blind Stick

---

## 👨‍💻 Authors
**Aravelli V S B Sarma**
Department of Computer Science & Engineering  
Dadi Institute of Engineering & Technology  
Academic Year: 2024–2025

Guided by: **Dr. K. Sujatha**
Professor, Department of CSE

---

## 📄 License

This project is developed for educational and socially relevant purposes. Feel free to use, modify, and improve the project for research and learning purposes.
