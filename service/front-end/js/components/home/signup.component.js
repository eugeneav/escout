import React from 'react';
import AuthActions from '../../actions/auth.actions';
import Validator from  '../../utils/validator.util';

export default class SignUp extends React.Component {
    constructor() {
        super();

        this.state = {
            signUpData: {
                email: null,
                password: null,
                passwordRepeat: null
            }
        }

        this.onSignUpEmailChanged = this.onSignUpEmailChanged.bind(this);
        this.onSignupPasswordChanged = this.onSignupPasswordChanged.bind(this);
        this.onSignUpPasswordRepeatChanged = this.onSignUpPasswordRepeatChanged.bind(this);
        this.signUp = this.signUp.bind(this);
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

        var result = Validator.validateSignUpData(this.state.signUpData);

        if (result.valid) {

            this.setState({
                signUpData: this.state.signUpData,
                signUpErrors: null
            });
            
            AuthActions.signUp(this.state.signUpData)
        } else {

            var signUpErrors = result.errors.map(function (error, index) {
                return <div className="alert alert-danger" role="alert" key={index}>{error.message}</div>;
            });

            this.setState({
                signUpData: this.state.signUpData,
                signUpErrors: signUpErrors
            })
        }
    }

    render() {
        return (
            <div className={this.props.tabSignUpClass}>
                { this.state.signUpErrors }
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
                               minLength="6"
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
        );
    }
}
