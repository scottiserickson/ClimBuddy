#ifndef CLIMBUDDYWIRING_H
#define CLIMBUDDYWIRING_H

class ClimBuddyWiring 
{
	public: 
		void sleep(int milliseconds);
		void wiringSetup();
		void wiringISR(int input, int edge, void (*function)(void));
		void wiringWrite(int input, int value);
};

#endif
