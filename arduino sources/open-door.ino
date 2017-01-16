const short int stringSize = 255;
const int relay1 = 7;
const int relay2 = 8;
short unsigned int inputCharCount = 0;
String inputString = "";         // a string to hold incoming data
boolean stringComplete = false;  // whether the string is complete

void setup() {
  Serial.begin(9600);
  pinMode(relay1, OUTPUT);
  pinMode(relay2, OUTPUT);
  inputString.reserve(stringSize);
}

void loop() {
  digitalWrite(relay1, HIGH);
  digitalWrite(relay2, HIGH);
  if (stringComplete) {
    Serial.println(inputString);
    if (inputString == "open door\n") {
      Serial.println("opening door");
      digitalWrite(relay1, LOW);
      delay(500);
    }
    else if (inputString == "open fence\n") {
      Serial.println("opening fence");
      digitalWrite(relay2, LOW);
      delay(500);
    }
    else {
      Serial.println("invalid command");
    }
    inputCharCount = 0;
    inputString = "";
    stringComplete = false;
  }
}

void serialEvent() {
  while (Serial.available()) {
    char inChar = (char)Serial.read();
    inputCharCount += 1;
    if (inputCharCount < stringSize) {
      inputString += inChar;
      if (inChar == '\n') {
        stringComplete = true;
      }
    } else {
      stringComplete = true;
    }
  }
}

