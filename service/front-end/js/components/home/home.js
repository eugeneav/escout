import React from "react";

export default class Home extends React.Component {
    render() {
        return (
            <div className="container">
                <div className="col-md-12">
                    <h1>e-scout</h1>
                    <i>Remote front-end logging tool</i>
                </div>
                <div className="row">
                    <div className="col-md-4"></div>
                    <div className="col-md-4"></div>
                    <div className="col-md-4">
                        <div className="pad-top-140">
                            <ul className="nav nav-tabs">
                                <li className="active"><a href="#">Sign in</a></li>
                                <li><a href="#">Sign up</a></li>
                            </ul>
                            <div className="tab-content pad-16 grey-borders">
                                <div
                                    className="tab-pane active">
                                    <form>
                                        <div className="form-group">
                                            <label htmlFor="login-email">Email</label>
                                            <input id="login-email" className="form-control" type="email" name="email"
                                                   placeholder="example@mail.com" required="required"/>
                                        </div>
                                        <div className="form-group">
                                            <label htmlFor="login-password">Password</label>
                                            <input id="login-password" className="form-control" type="password"
                                                   name="password"
                                                   required="required"/>
                                        </div>
                                        <button type="submit" className="btn btn-default mar-right-16">Login</button>
                                        <a href="#">Forgot password</a>
                                    </form>
                                </div>
                                <div className="tab-pane">
                                    <form>
                                        <div className="form-group">
                                            <label htmlFor="signup-email">Email</label>
                                            <input id="signup-email" className="form-control" type="email" name="email"
                                                   placeholder="example@mail.com"
                                                   required="required"/>
                                        </div>
                                        <div className="form-group">
                                            <label htmlFor="signup-password">Password</label>
                                            <input id="signup-password" className="form-control" type="password"
                                                   name="password"
                                                   required="required"/>
                                        </div>
                                        <div className="form-group">
                                            <label htmlFor="signup-password-repeat">Repeat Password</label>
                                            <input id="signup-password-repeat" className="form-control" type="password"
                                                   name="password"
                                                   required="required"/>
                                        </div>
                                        <button type="submit" className="btn btn-default">Sign Up</button>
                                    </form>
                                </div>
                            </div>

                        </div>
                    </div>
                </div>
            </div>
        );
    }
}
