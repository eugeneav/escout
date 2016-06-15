import AppDispatcher from '../dispatcher';
import EventEmitter from 'events';

class AuthStore extends EventEmitter {
    constructor() {
        super()
    }
    
    isAuthorized() {
        // TODO 
        return false;
    }
}

AuthStore.dispatcherIndex = AppDispatcher.register(action => {
    console.debug("LoginTry Action", action);
});

export default new AuthStore;