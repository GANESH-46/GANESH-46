#define in1 5
#define in2 6
#define in3 10
#define in4 11
#define p 13
char d;
void setup(){
pinMode(in1,OUTPUT);
pinMode(in2,OUTPUT);
pinMode(in3,OUTPUT);
pinMode(in4,OUTPUT);
Serial.begin(9600);
}
void loop(){
if(Serial.available()>0);
{
   d=Serial.read();
   if(d == 'a'){
    digitalWrite(in1,HIGH);
    digitalWrite(in2,LOW);
    digitalWrite(in3,HIGH);
    digitalWrite(in4,LOW);
    }
   else if(d == 'b'){
    digitalWrite(in1,LOW);
    digitalWrite(in2,HIGH);
    digitalWrite(in3,LOW);
    digitalWrite(in4,HIGH);
   }
   else if(d == 'c'){
    digitalWrite(in1,HIGH);
    digitalWrite(in2,LOW);
    digitalWrite(in3,LOW);
    digitalWrite(in4,HIGH);
   }
   else if(d == 'd'){
    digitalWrite(in1,LOW);
    digitalWrite(in2,HIGH);
    digitalWrite(in3,HIGH);
    digitalWrite(in4,LOW);
   }
 
     else if(d == 's'){
    digitalWrite(in1,LOW);
    digitalWrite(in2,LOW);
    digitalWrite(in3,LOW);
    digitalWrite(in4,LOW);
   }
   else if(d == 'v'){
    digitalWrite(p,HIGH);
   }
   else {
    digitalWrite(p,LOW);
   }
}}
