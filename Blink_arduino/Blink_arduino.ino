
void setup() {
  // initialize digital pin LED_BUILTIN as an output.
  Serial.begin(9600);
  pinMode(2, OUTPUT);
  digitalWrite(2,LOW);
  digitalWrite(3,LOW);
}
// the loop function runs over and over again forever
void loop() {
  int flag1;
  int flag2;
  int times;
  while (Serial.available() or flag1 == 1 or flag2 == 1)
 {
  int data = Serial.read();
  if (data == '1')
    {
      digitalWrite(2, HIGH);
      flag1 = 0;   
    }
  else if (data == '0')
    {
      digitalWrite(2, LOW);   
      flag1 = 0; 
    }
  else if (data == '2')
    {
      flag1 = 1;
    }
  
  
  if (data == '4')
    {
      digitalWrite(3, HIGH);
      flag2 = 0;   
    }
  else if (data == '3')
    {
      digitalWrite(3, LOW);   
      flag2 = 0; 
    }
  else if (data == '5')
    {
      flag2 = 1;
    }
  if (flag2 == 1 and flag1 != 1)
   {
      times = 1000;
      digitalWrite(3, HIGH);
      while (times > 0)
        {
          times--;
          delay(1);
          if (Serial.available())
            break;
        }
      digitalWrite(3, LOW);
      times = 1000;
      while (times > 0)
        {
          times--;
          delay(1);
          if (Serial.available())
            break;
        }
   }
   
   if (flag1 == 1 and flag2 !=1)
   {
      times = 1000;
      digitalWrite(2, HIGH);
      while (times > 0)
        {
          times--;
          delay(1);
          if (Serial.available())
            break;
        }
      digitalWrite(2, LOW);
      times = 1000;
      while (times > 0)
        {
          times--;
          delay(1);
          if (Serial.available())
            break;
        }
   }
   
   if (flag2 == 1 and flag1 == 1)
   {
      times = 1000;
      digitalWrite(3, HIGH);
      digitalWrite(2, HIGH);
      while (times > 0)
        {
          times--;
          delay(1);
          if (Serial.available())
            break;
        }
      digitalWrite(3, LOW);
      digitalWrite(2, LOW);
      times = 1000;
      while (times > 0)
        {
          times--;
          delay(1);
          if (Serial.available())
            break;
        }
   }
 }
}
