/*  
 *  LoRa 868 / 915MHz SX1272 LoRa module
 *  
 *  Copyright (C) Libelium Comunicaciones Distribuidas S.L. 
 *  http://www.libelium.com 
 *  
 *  This program is free software: you can redistribute it and/or modify 
 *  it under the terms of the GNU General Public License as published by 
 *  the Free Software Foundation, either version 3 of the License, or 
 *  (at your option) any later version. 
 *  
 *  This program is distributed in the hope that it will be useful, 
 *  but WITHOUT ANY WARRANTY; without even the implied warranty of 
 *  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the 
 *  GNU General Public License for more details.
 *  
 *  You should have received a copy of the GNU General Public License 
 *  along with this program.  If not, see http://www.gnu.org/licenses/. 
 *  
 *  Version:           1.1
 *  Design:            David Gascón 
 *  Implementation:    Covadonga Albiñana & Victor Boria
 */
 
// Include the SX1272 and SPI library: 
#include "arduPiLoRa.h"
#include <iostream>

int e;
char my_packet[100];

void setup()
{
  // Power ON the module
  e = sx1272.ON();
  
  // Set transmission mode
  e = sx1272.setMode(4);
  
  // Set header
  e = sx1272.setHeaderON();
  
  // Select frequency channel
  e = sx1272.setChannel(CH_10_868);
  
  // Set CRC
  e = sx1272.setCRC_ON();
  
  // Select output power (Max, High or Low)
  e = sx1272.setPower('H');
  
  // Set the node address
  e = sx1272.setNodeAddress(8);
  
  // Print a success message
  delay(1000);
}

void loop(void)
{
	// Receive message
  	e = sx1272.receivePacketTimeout(10000);
  	if ( e == 0 )
  	{
    		for (unsigned int i = 0; i < sx1272.packet_received.length; i++)
    		{
      			my_packet[i] = (char)sx1272.packet_received.data[i];
    		}
    		std::cout << my_packet << std::endl;
    		exit(0);
  	}
}

int main (){
	setup();
	while(1){
		//loop();
		e = sx1272.receivePacketTimeout(10000);
  		if ( e == 0 )
  		{
    			for (unsigned int i = 0; i < sx1272.packet_received.length; i++)
    			{
      				my_packet[i] = (char)sx1272.packet_received.data[i];
    			}
    			std::cout << my_packet << std::endl;
    			return(0);
  		}
	}
}
