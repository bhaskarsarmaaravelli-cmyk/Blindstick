const int trigPin1 = 4; 
const int echoPin1 = 5; 
const int buzzer = 7; 
const int led = 9; 
long duration1; 
int distance1; 
int safetyDistance = 100; // Set a default safety distance

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

    // Check if the distance is less than or equal to the safety distance
    if (distance1 <= safetyDistance) { 
        digitalWrite(buzzer, HIGH); // Activate buzzer
    } else { 
        digitalWrite(buzzer, LOW); // Deactivate buzzer
    }

    // Print distance to Serial Monitor for debugging
    Serial.print("Distance: ");
    Serial.print(distance1);
    Serial.println(" cm");

    // Add a delay for stability
    delay(500); 
}
