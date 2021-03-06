/* 
 * This class represents a physical attack, actually performed by the node Local Filter.
 *
 *  Author : Alessandro Pischedda
 *  e-mail : alessandro.pischedda@gmail.com
 */

#ifndef PHYSICALATTACK_H
#define PHYSICALATTACK_H

#include "Destroy.h"
#include "Move.h"
#include "CastaliaModule.h"
#include "Attack.h"


using namespace std;

class PhysicalAttack : public Attack {

	public:
	  
	PhysicalAttack() : Attack() {}
	virtual ~PhysicalAttack() {}
	
	void execute(bool& destroyed);
	
};

#endif
