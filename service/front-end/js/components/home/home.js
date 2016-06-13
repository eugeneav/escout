import React from "react";
import Authentication from "./authentication.component";

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
                        <Authentication />
                    </div>
                </div>
            </div>
        );
    }
}
