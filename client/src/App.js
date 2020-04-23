import React, { Component } from "react";

import { BrowserRouter as Router, Route, Switch } from "react-router-dom";
import "bootstrap/dist/css/bootstrap.min.css";
import "./App.scss";
import { Layout } from "./Components/Layouts/Layout";
import BizList from "./Components/BizCards/BizList";
import { NavBar } from "./Components/NavBar/NavBar";

class App extends Component {
  render() {
    return (
      <React.Fragment>
        <NavBar />
        <Layout>
          <Router>
            <Switch>
              <Route exact path="/" component={BizList} />
            </Switch>
          </Router>
        </Layout>
      </React.Fragment>


import logo from "./logo.svg";

import "./App.scss";

import BizList from "./components/BizList";

class App extends Component {
  render() {
    return (
      <div className="App">
        <header className="App-header">
          <img src={logo} className="App-logo" alt="logo" />
          <h1 className="App-title">Welcome to React</h1>
        </header>
        <p className="App-intro">
          To get started, edit <code>src/App.js</code> and save to reload.
        </p>
        <BizList />
      </div>
    );
  }
}

export default App;
