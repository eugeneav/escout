import AppDispatcher from '../dispatcher';
import Constants from '../constants'

class AuthActions {

    login(data) {
        AppDispatcher.dispatch({
            actionType: Constants.LOGIN_TRY,
            data: data
        })
    }

    signUp(data) {
        AppDispatcher.dispatch({
            actionType: Constants.SIGNUP_TRY,
            data: data
        })
    }
}

export default new AuthActions;