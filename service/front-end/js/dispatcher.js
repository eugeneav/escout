import {Dispatcher} from 'flux';
import Constants from './constants';

class DispatcherClass extends Dispatcher {

    handleViewAction(action) {
        this.dispatch({
            source: Constants.VIEW_ACTION,
            action: action
        });
    }

    handleSystemActions(action) {
        this.dispatch({
            source: Constants.SYSTEM_ACTION, // TODO To constants
            action: action
        });
    }


}

export default new DispatcherClass;
