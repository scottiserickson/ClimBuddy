#include "ClimBuddyWiring.h" 
#include <iostream>
#include <stdio.h>
#include <wiringPi.h>

void ClimBuddyWiring::sleep(int milliseconds) 
{
	sleep(milliseconds);
}

void ClimBuddyWiring::wiringSetup() 
{
	wiringPiSetup();
}

void ClimBuddyWiring::wiringISR(int input, int edge, void (*function)(void))
{
	wiringPiISR(input, edge, function);
}

void ClimBuddyWiring::wiringWrite(int input, int value) 
{
	digitalWrite(input, value);
}
