import AppDispatcher from '../dispatcher';
import EventEmitter from 'events';
import Constants from '../constants';
import axios from 'axios';

class AuthStore extends EventEmitter {
    constructor() {
        super()
    }

    isAuthorized() {
        // TODO Get cookie
        // TODO Cookie has token
        return false;
    }

    handleActions(data) {

        var that = this; // TODO Look for more beauty way

        if (data.source === Constants.SYSTEM_ACTION) {
            switch (data.action.actionType) {
                case Constants.LOGIN_TRY:

                        axios.post('/api/guard/sign-in', {
                            email: data.action.data.email, // TODO Fix on backend
                            password: data.action.data.password
                        })
                        .then(function (response) {
                            
                            console.debug(response);
                            // TODO Get token (? with some user data)
                            // TODO Save token to storage (or cookie)
                            console.debug('LOGGED_IN');
                            that.emit('LOGGED_IN');
                        })
                        .catch(function (error) {
                            console.log(error);
                        });

                        break;
                case Constants.SIGNUP_TRY:
                    
                        axios.post('/api/guard/sign-up', {
                            email: data.action.data.email, // TODO Fix on backend
                            password: data.action.data.password
                        })
                        .then(function (response) {

                            console.debug(response);
                            // TODO Get token (? with some user data)
                            // TODO Save token to storage (or cookie)
                            console.debug('SIGNED_UP');
                            that.emit('SIGNED_UP');

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

        console.debug("LoginTry Action", data);
    }
}

const authStore = new AuthStore;

AppDispatcher.register(authStore.handleActions.bind(authStore));

export default authStore;