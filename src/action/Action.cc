#include "Action.h"

Action::Action(const ActionName name_action) {
	
	name = name_action;
	
	/* Actions as 'Destroy' or 'Move' do not deal with packets, thus do not need the following parameters */
	packetName = "";
	layer = NONE;

}
