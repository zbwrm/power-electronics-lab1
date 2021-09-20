
int input_1 = A0;
int input_2 = A1;

void setup() {
  // start serial communication with laptop
  Serial.begin(9600);
}

void loop() {
  // read the value from the sensors every 100ms:
  Serial.print(analogRead(input_1));
  Serial.print(" ");
  Serial.println(analogRead(input_2));
  delay(100);
}
