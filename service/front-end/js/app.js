import React from "react";
import ReactDOM from "react-dom";
import {Router, Route, IndexRedirect, IndexRoute, browserHistory} from "react-router";

import Layout from "./components/Layout";
import Home from "./components/home/home";
import Dashboard from "./components/dashboard/dashboard";
import RecoverEmail from "./components/recover-email/recover-email";
import NewPassword from "./components/new-password/new-password";
import Projects from "./components/dashboard/projects.component"
import Settings from "./components/dashboard/settings.component"

const app = document.getElementById('app');

ReactDOM.render(
    <Router history={browserHistory}>
        <Route path="/" component={Layout}>
            <IndexRoute component={Home} />
            <Route path="dashboard" component={Dashboard}>
                <IndexRedirect to="projects" />
                <Route path="projects" component={Projects} />
                <Route path="settings" component={Settings} />
            </Route>
            <Route path="/recover-email" component={RecoverEmail} />
            <Route path="/reset/:token" component={NewPassword} />
        </Route>
    </Router>,
    app);
