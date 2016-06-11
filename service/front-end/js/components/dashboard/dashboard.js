import React from "react";

export default class Dashboard extends React.Component {
    render() {
        return (
            <div className="container">
                <nav className="navbar navbar-default">
                    <div className="navbar-header pull-left">
                        <a className="navbar-brand">e-scout dashboard</a>
                    </div>
                    <div className="navbar-header pull-right">
                        <ul className="nav navbar-nav">
                            <li><a href="/logout">Logout</a></li>
                        </ul>
                    </div>

                </nav>
                <div className="row">
                    <div className="col-md-4">
                        <ul className="nav nav-pills nav-stacked">
                            <li className="active"><a href="/#">Projects</a></li>
                            <li><a href="/#">Settings</a></li>
                        </ul>
                    </div>
                    <div className="col-md-8">
                        <div className="list-group">
                            <a className="list-group-item active" href="#">Project 1</a>
                            <a className="list-group-item" href="#">Project 2<span className="badge">14</span></a>
                            <a className="list-group-item" href="#">Project 3<span className="badge">2</span></a>
                            <a className="list-group-item" href="#">Project 4<span className="badge">4</span></a>
                            <a className="list-group-item" href="#">Project 5<span className="badge">9</span></a>
                            <a className="list-group-item" href="#">Project 6</a>
                        </div>

                        <div className="list-group">
                            <li className="list-group-item list-group-item-success">Log ok</li>
                            <li className="list-group-item list-group-item-warning">Log ok</li>
                            <li className="list-group-item list-group-item-info">Log ok</li>
                            <li className="list-group-item list-group-item-danger">Log ok</li>
                        </div>

                        <nav>
                            <ul className="pager">
                                <li><a href="#">Previous</a></li>
                                <li><a href="#">Next</a></li>
                            </ul>
                        </nav>
                    </div>

                </div>
            </div>
        );
    }
}
