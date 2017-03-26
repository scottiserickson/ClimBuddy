#include <stdio.h>
#include <sys/time.h>
#include <wiringPi.h>
// Include the SX1272 and SPI library: 
#include "arduPiLoRa.h"

int e;

char message1 [] = "Packet 1, wanting to see if received packet is the same as sent packet";
char message2 [] = "Packet 2, broadcast test";

void setup()
{
  // Print a start message
  printf("SX1272 module and Raspberry Pi: send packets without ACK\n");
  
  // Power ON the module
  e = sx1272.ON();
  printf("Setting power ON: state %d\n", e);
  
  // Set transmission mode
  e = sx1272.setMode(4);
  printf("Setting Mode: state %d\n", e);
  
  // Set header
  e = sx1272.setHeaderON();
  printf("Setting Header ON: state %d\n", e);
  
  // Select frequency channel
  e = sx1272.setChannel(CH_10_868);
  printf("Setting Channel: state %d\n", e);
  
  // Set CRC
  e = sx1272.setCRC_ON();
  printf("Setting CRC ON: state %d\n", e);
  
  // Select output power (Max, High or Low)
  e = sx1272.setPower('H');
  printf("Setting Power: state %d\n", e);
  
  // Set the node address
  e = sx1272.setNodeAddress(3);
  printf("Setting Node address: state %d\n", e);
  
  // Print a success message
  printf("SX1272 successfully configured\n\n");
  delay(1000);
}

void loop(void)
{
	// Send message1 and print the result
    e = sx1272.sendPacketTimeout(8, message1);
    printf("Packet sent, state %d\n",e);
    
    delay(4000);
 
 	// Send message2 broadcast and print the result
    e = sx1272.sendPacketTimeout(0, message2);
    printf("Packet sent, state %d\n",e);
    
    delay(4000);
}

int main () {
	setup();
	while(1){
		loop();
	}
	return (0);
}

