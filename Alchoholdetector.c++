#define sensorDigital A0
#define Motor 9
#define buzzer 8

void setup() {

  pinMode(sensorDigital, INPUT);

	pinMode(Motor, OUTPUT);

  	pinMode(buzzer, OUTPUT);

    	Serial.begin(9600);

    	}

    	void loop() {

      	bool digital = digitalRead(sensorDigital);

  	Serial.print("t");

    	Serial.print("Digital value :");

      	Serial.println(digital);

  if (digital == 0) {

  	digitalWrite(Motor, LOW);

      	digitalWrite(buzzer, HIGH);

        	} else {

            	digitalWrite(Motor, HIGH);

                	digitalWrite(buzzer, LOW);

                  	}

                  	}
