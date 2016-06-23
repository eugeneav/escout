import AppDispatcher from '../dispatcher';
import Constants from '../constants'

class ApplicationActions {

    getApplications() {
        AppDispatcher.handleSystemActions({
            actionType: Constants.GET_ACCOUNT_APPLICATIONS,
            data: null
        })
    }
}

export default new ApplicationActions;
