import React from "react";
import Validator from  '../../utils/validator.util';
import AuthActions from '../../actions/auth.actions';
import AuthStore from '../../stores/auth.store';
import Constants from '../../constants';

export default class RecoverEmail extends React.Component {

    constructor() {
        super();

        this.state = {
            email: null,
            errors: null,
            success: null
        };

        this.onRecoverEmailChanged = this.onRecoverEmailChanged.bind(this);
        this.recover = this.recover.bind(this);
        this.recoverEmailSentCallback = this.recoverEmailSentCallback.bind(this)
    }

    recoverEmailSentCallback() {

        this.setState({
            email: this.state.email,
            errors: null,
            success: <div className="alert alert-success" role="alert">Recover email has been sent</div>
        })
    }

    // @Override
    componentWillMount() {
        AuthStore.on(Constants.RECOVER_EMAIL_SENT, this.recoverEmailSentCallback);
    }

    onRecoverEmailChanged(event) {
        this.setState({
            email: event.target.value
        });

        console.debug("Recover email: ", event.target.value);
    }


    recover(e) {
        e.preventDefault();

        var result = Validator.validateRecoverData(this.state);

        if (result.valid) {

            this.setState({
                email: this.state.email,
                errors: null,
                success: null
            });

            AuthActions.recoverPasswordByEmail({email: this.state.email});

        } else {

            var errors = result.errors.map(function (error, index) {
                return <div className="alert alert-danger" role="alert" key={index}>{error.message}</div>;
            });

            this.setState({
                email: this.state.email,
                errors: errors,
                success: null
            })
        }

    }


    render() {
        return (
            <div className="container">
                <div className="row">
                    <div className="col-md-12">
                        <h1>e-scout</h1>
                        <i>Remote front-end logging tool</i>
                    </div>
                </div>
                <div className="row">
                    <div className="col-md-4"></div>
                    <div className="col-md-4">
                        <div className="pad-top-140">
                            { this.state.errors }
                            { this.state.success }
                            <form onSubmit={this.recover}>
                                <div className="form-group">
                                    <label htmlFor="recover-email">Enter your email</label>
                                    <input id="recover-email"
                                           className="form-control"
                                           type="email"
                                           name="email"
                                           placeholder="example@mail.com"
                                           onChange={this.onRecoverEmailChanged}
                                           value={this.state.email}
                                           required="required"/>
                                </div>
                                <button type="submit" className="btn btn-default">Recover</button>
                            </form>
                        </div>
                    </div>
                    <div className="col-md-4"></div>
                </div>
            </div>
        );
    }
}
