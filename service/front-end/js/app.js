import React from "react";
import ReactDOM from "react-dom";
import { Router, Route, IndexRoute, hashHistory } from "react-router";

import Layout from "./components/Layout";
import Home from "./components/home/home";
import Dashboard from "./components/dashboard/dashboard";
import RecoverEmail from "./components/recover-email/recover-email";
import NewPassword from "./components/new-password/new-password";

const app = document.getElementById('app');

ReactDOM.render(
  <Router history={hashHistory}>
    <Route path="/" component={Layout}>
      <IndexRoute component={Home}></IndexRoute>
      <Route path="dashboard" component={Dashboard}></Route>
      <Route path="recover-email" component={RecoverEmail}></Route>
      <Route path="new-password" component={NewPassword}></Route>
    </Route>
  </Router>,
app);

// <Route path="favorites" component={Favorites}></Route>
// <Route path="settings" component={Settings}></Route>
