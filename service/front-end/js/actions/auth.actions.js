import AppDispatcher from '../dispatcher';
import Constants from '../constants'

class AuthActions {

    login(data) {
        AppDispatcher.handleSystemActions({
            actionType: Constants.LOGIN_TRY,
            data: data
        })
    }

    signUp(data) {
        AppDispatcher.handleSystemActions({
            actionType: Constants.SIGNUP_TRY,
            data: data
        })
    }
}

export default new AuthActions;