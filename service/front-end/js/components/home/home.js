import React from "react";
import Authentication from "./authentication.component";
import AuthStore from '../../stores/auth.store';
import { withRouter } from 'react-router'


class Home extends React.Component {

    //@Override
    componentWillMount() {
        if(AuthStore.isAuthorized()) {
            this.props.router.push('dashboard');
        }
    }

    //@Override
    componentDidMount() {
        //TodoStore.addChangeListener(this._onChange); TODO See EventEmitter for that
    }

    //@Override
    componentWillUnmount() {
        //TodoStore.removeChangeListener(this._onChange);
    }

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

export default withRouter(Home);
