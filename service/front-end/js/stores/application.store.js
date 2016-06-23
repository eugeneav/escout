import AppDispatcher from '../dispatcher';
import EventEmitter from 'events';
import Constants from '../constants';
import AuthStore from './auth.store';
import axios from 'axios';

class ApplicationStore extends EventEmitter {

    constructor() {
        super()
    }

    handleActions(data) {
        var that = this;

        if (data.source === Constants.SYSTEM_ACTION) {
            switch (data.action.actionType) {
                case Constants.GET_ACCOUNT_APPLICATIONS:

                    var config = {
                        headers: {'Authorization': 'Token ' + AuthStore.getToken()}
                    };

                    axios.get('/api/dashboard/applications', config)
                        .then(function (response) {
                            console.debug(response);
                            that.emit(Constants.APPLICATION_DATA_RECEIVED);
                        })
                        .catch(function (error) {
                            console.log(error);
                        });
                    break;
                default:
                // do nothing
            }
        }
    }
}

const applicationStore = new ApplicationStore;

AppDispatcher.register(applicationStore.handleActions.bind(applicationStore));

export default applicationStore;
