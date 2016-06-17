import React from 'react';
import classNames from 'classnames';
import SignIn from './signin.component';
import SignUp from './signup.component';

export default class Authentication extends React.Component {

    constructor() {
        super();

        this.state = {
            tabs: {
                showLogin: true
            }
        };

        this.toggleTab = this.toggleTab.bind(this);
    }

    toggleTab(tabName) {
        this._toggleTab(tabName);
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
                    <SignIn tabSignInClass={tabSignInClass} />
                    <SignUp tabSignUpClass={tabSignUpClass} />
                </div>
            </div>
        );
    }
}