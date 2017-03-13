
#define SERIALSPEED 9600
#define STRINGSIZE 128
#define RELAY1 7
#define RELAY2 8

short unsigned int inputCharCount = 0;
String inputString = "";         // a string to hold incoming data
boolean stringComplete = false;  // whether the string is complete

void setup() {
    Serial.begin(SERIALSPEED);  // init serial
    inputString.reserve(STRINGSIZE);  // create buffer
    // relay pin as output pin
    pinMode(RELAY1, OUTPUT);
    pinMode(RELAY2, OUTPUT);
}

void loop() {
    // default relay state
    digitalWrite(RELAY1, HIGH);
    digitalWrite(RELAY2, HIGH);
    // loop until a complete command is received
    if (stringComplete) {
        // Serial.println(inputString);  // debug : show received command
        if (inputString == "open door\n") {
            Serial.println("opening door");
            digitalWrite(RELAY1, LOW);
            delay(500);  // delay of 500ms is sufficient to open the door
        }
        else if (inputString == "open fence\n") {
            Serial.println("opening fence");
            digitalWrite(RELAY2, LOW);
            delay(1500);  // delay of 1.5s to open the fence
        }
        else {
            Serial.print("invalid command : \"");
            Serial.print(inputString);
            Serial.println("\"");
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
        if (inputCharCount < STRINGSIZE) {
            inputString += inChar;
            if (inChar == '\n') {
                stringComplete = true;
            }
        } else {
            stringComplete = true;
        }
    }
}
