#include "PhysicalAttack.h"

/* This function performs the physical attack. The parameter "destroyed" is set to true if the node is destroyed during the attack.
 * More specifically, the node is not actually destroyed, but it will drop every received/created packet, thus appearing to be destroyed.
 */

void PhysicalAttack::execute(bool& destroyed) {

	/* Execute all actions composing the attack */
	for(int i=0; i < actions.size(); i++ ) {

		switch( actions[i]->getName() ) {
		  
			case MOVE:{
				Move* move = (Move *)actions[i];
				move->execute();
				break;
			}

			case DESTROY:{
				Destroy *destroy = (Destroy *)(actions[i]);
				destroy->execute(destroyed);
				break;
			}

		} // END SWITCH

	}// END FOR

}
