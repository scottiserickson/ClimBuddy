//#include <stdio.h>
//#include <sys/time.h>
#include <wiringPi.h>
#include "arduPiLoRa.h"

// Which GPIO pin we're using
#define PIN 25
#define LEDR 29
#define LEDG 28

// How much time a change must be since the last in order to count as a change
#define IGNORE_CHANGE_BELOW_USEC 10000

// Current state of the pin
static volatile int state;
// Time of last change
struct timeval last_change;

// Mode variable for LoRa sx1272
int e;

// Messages sent in transmission
char message1 [] = "Packet 1, wanting to see if received packet is the same as sent packet";
char message2 [] = "Packet 2, broadcast test";

void transmitMessage(void)
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

// Handler for interrupt
void button_one(void) {
	struct timeval now;
	unsigned long diff;

	gettimeofday(&now, NULL);

	// Time difference in usec
	diff = (now.tv_sec * 1000000 + now.tv_usec) - (last_change.tv_sec * 1000000 + last_change.tv_usec);

	// Filter jitter
	if (diff > IGNORE_CHANGE_BELOW_USEC) {
		digitalWrite(LEDG, !state);
		state = !state; 
		transmitMessage();
	}

	last_change = now;
}

void loraSetup(void)
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

int main(void) {
	// Init GPIO and LoRa module
	wiringPiSetup();
	loraSetup();

	// Set pin to output in case it's not
	pinMode(PIN, OUTPUT);
	pinMode(LEDG, OUTPUT);

	// Time now
	gettimeofday(&last_change, NULL);

	// Bind to interrupt
	wiringPiISR(PIN, INT_EDGE_FALLING, &button_one);

	// Get initial state of pin
	state = digitalRead(PIN);

	if (state) {
		printf("Started! Initial state is on\n");
	}
	else {
		printf("Started! Initial state is off\n");
	}

	// Waste time but not CPU
	for (;;) {
		sleep(1);
	}
}
