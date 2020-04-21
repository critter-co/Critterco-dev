import React, { Component } from "react";
import axios from "axios";
class BizList extends Component {
  state = {
    biz: [],
  };
  componentDidMount() {
    axios.get("http://localhost:8000/api/biz/").then((res) => {
      console.log(res);
      this.setState({
        biz: res.data,
      });
    });
  }
  render() {
    return (
      <ul>
        {this.state.biz.map((biz) => (
          <li key={biz.key}>{biz.title}</li>
        ))}
      </ul>
    );
  }
}

export default BizList;
