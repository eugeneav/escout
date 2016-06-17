import React from 'react';
import {Link} from 'react-router';
import AuthActions from '../../actions/auth.actions';
import Validator from  '../../utils/validator.util';

export default class SignIn extends React.Component {

    constructor() {
        super();

        this.state = {
            loginData: {
                email: null,
                password: null
            },
            loginErrors: null
        };

        this.onLoginEmailChanged = this.onLoginEmailChanged.bind(this);
        this.onLoginPasswordChanged = this.onLoginPasswordChanged.bind(this);
        this.login = this.login.bind(this);

    }

    onLoginEmailChanged(event) {
        this.setState({
            loginData: {
                email: event.target.value,
                password: this.state.loginData.password
            }
        });
    }

    onLoginPasswordChanged(event) {
        this.setState({
            loginData: {
                email: this.state.loginData.email,
                password: event.target.value
            }
        });
    }

    login(e) {
        e.preventDefault();
        
        var result = Validator.validateSignInData(this.state.loginData);

        if (result.valid) {

            this.setState({
                loginData: this.state.loginData,
                loginErrors: null
            });

            AuthActions.login(this.state.loginData);
        } else {

            var loginErrors = result.errors.map(function (error, index) {
                return <div className="alert alert-danger" role="alert" key={index}>{error.message}</div>;
            });

            this.setState({
                loginData: this.state.loginData,
                loginErrors: loginErrors
            })
        }
    }


    render() {
        return (
            <div className={this.props.tabSignInClass}>
                { this.state.loginErrors }
                <form onSubmit={this.login}>
                    <div className="form-group">
                        <label htmlFor="login-email">Email</label>
                        <input id="login-email" className="form-control" type="email" name="email"
                               placeholder="example@mail.com" required="required"
                               onChange={this.onLoginEmailChanged}
                               value={this.state.loginData.email}/>
                    </div>
                    <div className="form-group">
                        <label htmlFor="login-password">Password</label>
                        <input id="login-password" className="form-control" type="password"
                               name="password"
                               required="required"
                               onChange={this.onLoginPasswordChanged}
                               value={this.state.loginData.password}
                        />
                    </div>
                    <button type="submit" className="btn btn-default mar-right-16">Sign in
                    </button>
                    <Link to="recover-email">Forgot password</Link>
                </form>
            </div>
        )
    };

}
