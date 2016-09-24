import React from "react";
import {Link} from 'react-router';
import AuthStore from '../../stores/auth.store';
import ApplicationStore from '../../stores/application.store';
import ApplicationActions from '../../actions/application.actions';
import Constants from '../../constants';
import {withRouter} from 'react-router'


// TODO React nested routes http://stackoverflow.com/questions/27612765/nested-routes-in-react-router
// http://ricostacruz.com/cheatsheets/react-router.html
class Dashboard extends React.Component {

    constructor() {
        super();

        this.logout = this.logout.bind(this)
    }

    componentWillMount() {
        if (!AuthStore.isAuthorized()) {
            console.info("Not logged in, back to home");
            this.props.router.push('/');
        }
        //this.props.router.push('dashboard/projects');

        ApplicationStore.on(Constants.APPLICATION_DATA_RECEIVED, this.onApplicationsDataReceived);
    }

    componentDidMount() {
        ApplicationActions.getApplications();
    }

    onApplicationsDataReceived() {

    }

    logout() {
        AuthStore.logout();
        this.props.router.push('/');
    }

    render() {
        return (
            <div className="container">
                <nav className="navbar navbar-default">
                    <div className="navbar-header pull-left">
                        <a className="navbar-brand">e-scout dashboard</a>
                    </div>
                    <div className="navbar-header pull-right">
                        <ul className="nav navbar-nav">
                            <li><a onClick={this.logout}>Logout</a></li>
                        </ul>
                    </div>

                </nav>
                <div className="row">
                    <div className="col-md-4">
                        <ul className="nav nav-pills nav-stacked">
                            <li className="active"><Link to="/dashboard/projects">Projects</Link></li>
                            <li><Link to="/dashboard/settings">Settings</Link></li>
                        </ul>
                    </div>
                    <div className="col-md-8">
                        {this.props.children}
                    </div>

                </div>
            </div>
        );
    }
}

export default withRouter(Dashboard);


// <div className="list-group">
//     <li className="list-group-item list-group-item-success">Log ok</li>
//     <li className="list-group-item list-group-item-warning">Log ok</li>
//     <li className="list-group-item list-group-item-info">Log ok</li>
//     <li className="list-group-item list-group-item-danger">Log ok</li>
// </div>