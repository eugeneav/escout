import React from "react";

export default class NewPassword extends React.Component {
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
                            <form>
                                <div className="form-group">
                                    <label htmlFor="recover-password">New Password</label>
                                    <input id="recover-password" className="form-control" type="password"
                                           name="password"
                                           required="required"/>
                                </div>
                                <div className="form-group">
                                    <label htmlFor="recover-password-repeat">Repeat Password</label>
                                    <input id="recover-password-repeat" className="form-control" type="password"
                                           name="password"
                                           required="required"/>
                                </div>
                                <button type="submit" className="btn btn-default">Set New Password</button>
                            </form>
                        </div>
                    </div>
                    <div className="col-md-4"></div>
                </div>
            </div>
        );
    }
}
