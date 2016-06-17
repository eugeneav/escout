import AppDispatcher from '../dispatcher';
import EventEmitter from 'events';
import Constants from '../constants';
import axios from 'axios';

class AuthStore extends EventEmitter {
    constructor() {
        super()
    }

    isAuthorized() {
        // TODO 
        return false;
    }
}

AuthStore.dispatcherIndex = AppDispatcher.register(data => {

    if (data.source === Constants.SYSTEM_ACTION) {
        switch (data.action.actionType) {
            case Constants.LOGIN_TRY:

                axios.post('/api/guard/login/', {
                    email: data.action.data.email,
                    password: data.action.data.password
                })
                .then(function (response) {
                    console.log(response);
                })
                .catch(function (error) {
                    console.log(error);
                });

                break;
            default:
            // Do nothing
        }
        //console.debug(action);
    }

    console.debug("LoginTry Action", action);
});

export default new AuthStore;