import React from "react";
import ReactDOM from "react-dom";
import { Router, Route, IndexRoute, hashHistory } from "react-router";

import Layout from "./components/Layout";
import Home from "./components/Home";
import Dashboard from "./components/Dashboard";

const app = document.getElementById('app');

ReactDOM.render(
  <Router history={hashHistory}>
    <Route path="/" component={Layout}>
      <IndexRoute component={Home}></IndexRoute>
      <Route path="dashboard" component={Dashboard}></Route>
    </Route>
  </Router>,
app);

// <Route path="favorites" component={Favorites}></Route>
// <Route path="settings" component={Settings}></Route>
