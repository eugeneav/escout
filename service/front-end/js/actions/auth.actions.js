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

    recoverPasswordByEmail(data) {
        AppDispatcher.handleSystemActions({
            actionType: Constants.RECOVER_PASSWORD_TRY,
            data: data
        })
    }
}

export default new AuthActions;