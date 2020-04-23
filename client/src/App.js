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
    );
  }
}

export default App;
