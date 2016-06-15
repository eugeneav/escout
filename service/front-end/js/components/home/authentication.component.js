import React from 'react';
import { Link } from 'react-router';
import classNames from 'classnames';
import AuthActions from '../../actions/auth.actions';

// TODO Input data validation needs to be added
export default class Authentication extends React.Component {

    constructor() {
        super();
        // Initial data
        this.state = {
            tabs: {
                showLogin: true
            },
            loginData: {
                email: null,
                password: null
            },
            signUpData: {
                email: null,
                password: null,
                passwordRepeat: null
            }
        };

        this.toggleTab = this.toggleTab.bind(this);

        this.onLoginEmailChanged = this.onLoginEmailChanged.bind(this);
        this.onLoginPasswordChanged = this.onLoginPasswordChanged.bind(this);
        this.login = this.login.bind(this);

        this.onSignUpEmailChanged = this.onSignUpEmailChanged.bind(this);
        this.onSignupPasswordChanged = this.onSignupPasswordChanged.bind(this);
        this.onSignUpPasswordRepeatChanged = this.onSignUpPasswordRepeatChanged.bind(this);
        this.signUp = this.signUp.bind(this);
    }

    toggleTab(tabName) {
        this._toggleTab(tabName);
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
        AuthActions.login(this.state.loginData);
    }

    onSignUpEmailChanged(event) {
        this.setState({
            signUpData: {
                email: event.target.value,
                password: this.state.signUpData.password,
                passwordRepeat: this.state.signUpData.passwordRepeat
            }
        })

    }

    onSignupPasswordChanged(event) {
        this.setState({
            signUpData: {
                email: this.state.signUpData.email,
                password: event.target.value,
                passwordRepeat: this.state.signUpData.passwordRepeat
            }
        })
    }

    onSignUpPasswordRepeatChanged(event) {
        this.setState({
            signUpData: {
                email: this.state.signUpData.email,
                password: this.state.signUpData.password,
                passwordRepeat: event.target.value
            }
        })
    }

    signUp(e) {
        e.preventDefault();
        AuthActions.signUp(this.state.signUpData)
    }

    _toggleTab(tabName) {
        if (tabName === 'sign-in') {
            this.setState({
                tabs: {
                    showLogin: true
                }
            })
        } else if (tabName === 'sign-up') {
            this.setState({
                tabs: {
                    showLogin: false
                }
            })
        }
    }

    render() {

        var tabSignInClass = classNames({
            'tab-pane': true,
            'active': this.state.tabs.showLogin
        });

        var tabSignUpClass = classNames({
            'tab-pane': true,
            'active': !this.state.tabs.showLogin
        });

        return (
            <div className="pad-top-140">
                <ul className="nav nav-tabs">
                    <li className={ this.state.tabs.showLogin ? 'active' : '' }>
                        <a onClick={() => {this.toggleTab('sign-in')}} href="#">Sign in</a>
                    </li>
                    <li className={ !this.state.tabs.showLogin ? 'active' : '' }>
                        <a onClick={() => {this.toggleTab('sign-up')}} href="#">Sign up</a>
                    </li>
                </ul>
                <div className="tab-content pad-16 grey-borders">
                    <div
                        className={tabSignInClass}>
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
                    <div className={tabSignUpClass}>
                        <form onSubmit={this.signUp}>
                            <div className="form-group">
                                <label htmlFor="signup-email">Email</label>
                                <input id="signup-email" className="form-control" type="email" name="email"
                                       placeholder="example@mail.com"
                                       required="required"
                                       onChange={this.onSignUpEmailChanged}
                                       value={this.state.signUpData.email}/>
                            </div>
                            <div className="form-group">
                                <label htmlFor="signup-password">Password</label>
                                <input id="signup-password" className="form-control" type="password"
                                       name="password"
                                       required="required"
                                       onChange={this.onSignupPasswordChanged}
                                       value={this.state.signUpData.password}/>
                            </div>
                            <div className="form-group">
                                <label htmlFor="signup-password-repeat">Repeat Password</label>
                                <input id="signup-password-repeat" className="form-control" type="password"
                                       name="password"
                                       required="required"
                                       onChange={this.onSignUpPasswordRepeatChanged}
                                       value={this.state.signUpData.passwordRepeat}/>
                            </div>
                            <button type="submit" className="btn btn-default">Sign Up</button>
                        </form>
                    </div>
                </div>
            </div>
        );
    }
}