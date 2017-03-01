void setup() {
  for(int i = 2; i < 12; i++){
    pinMode(i,INPUT_PULLUP);
  }
  Serial.begin(9600);
}

String key[10] = {"VK_VOLUME_UP",
"VK_VOLUME_DOWN",
"VK_VOLUME_MUTE",
"VK_MEDIA_PREV_TRACK",
"VK_MEDIA_PLAY_PAUSE",
"VK_MEDIA_NEXT_TRACK",
"",
"",
"",
"LOCK"};



void loop() {
  for(int i = 2; i < 12; i++){
    if(!digitalRead(i)){
      Serial.println(key[i-2]);
      while(!digitalRead(i)){
        delay(10);}
    }
  }
 
}
