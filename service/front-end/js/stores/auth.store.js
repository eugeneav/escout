import AppDispatcher from '../dispatcher';
import EventEmitter from 'events';
import Constants from '../constants';
import axios from 'axios';

class AuthStore extends EventEmitter {
    constructor() {
        super()
    }

    isAuthorized() {
        return localStorage.getItem(Constants.AUTH_TOKEN) !== undefined && localStorage.getItem(Constants.AUTH_TOKEN) !== null;
    }

    getToken() {
        return localStorage.getItem(Constants.AUTH_TOKEN);
    }

    _setToken(value) {
        localStorage.setItem(Constants.AUTH_TOKEN, value);
    }

    _cleanToken() {
        localStorage.removeItem(Constants.AUTH_TOKEN);
    }

    handleActions(data) {

        var that = this;

        if (data.source === Constants.SYSTEM_ACTION) {
            switch (data.action.actionType) {
                case Constants.LOGIN_TRY:

                    // TODO Use for headers sending
                    var config = {
                        headers: {'X-My-Custom-Header': 'Header-Value'}
                    };


                    axios.post('/api/guard/sign-in', {
                        email: data.action.data.email, // TODO Fix on backend
                        password: data.action.data.password
                    })
                        .then(function (response) {

                            if (response.data.status === 'ok') { // TODO Errors need to be handled in error callback
                                that._setToken(response.data.data.token);
                            }
                            that.emit(Constants.SIGNED_IN);
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
                            that.emit(Constants.SIGNED_UP);
                        })
                        .catch(function (error) {
                            console.log(error);
                        });

                    break;
                default:
                // Do nothing
            }
        }

        console.debug("LoginTry Action", data);
    }
}

const authStore = new AuthStore;

AppDispatcher.register(authStore.handleActions.bind(authStore));

export default authStore;