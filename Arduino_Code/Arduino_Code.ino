String data;
char d1;
void setup() 
{
  pinMode(LED_BUILTIN, OUTPUT);
  Serial.begin(9600);
}

// the loop function runs over and over again forever
void loop()
{
  if(Serial.available())
  {
    data = Serial.readString();
    d1 = data.charAt(0);
    if(d1 == 'H')
    {
      digitalWrite(LED_BUILTIN, HIGH);
    }
    else if (d1 == 'L')
    {
      digitalWrite(LED_BUILTIN, LOW);
    }
  }
//  digitalWrite(LED_BUILTIN, HIGH);   // turn the LED on (HIGH is the voltage level)
//  Serial.println('H');
//  delay(1000);                       // wait for a second
//  digitalWrite(LED_BUILTIN, LOW);    // turn the LED off by making the voltage LOW
//  Serial.println('L');
//  delay(1000);                       // wait for a second
}
