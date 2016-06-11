import React from "react";

export default class RecoverEmail extends React.Component {
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
                                    <label htmlFor="recover-email">Enter your email</label>
                                    <input id="recover-email" className="form-control" type="email" name="email"
                                           placeholder="example@mail.com"
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
