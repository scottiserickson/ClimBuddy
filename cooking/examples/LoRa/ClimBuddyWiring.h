#ifndef CLIMBUDDYWIRING_H
#define CLIMBUDDYWIRING_H

namespace ClimbFuncs 
{
class ClimBuddyWiring 
{
	public: 
		static void wiringSetup();
		static void wiringISR(int input, int edge, void (*function)(void));
		static void wiringWrite(int input, int value);
};
}

#endif
