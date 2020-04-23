import React, { Component } from "react";
import axios from "axios";
import { Card, Button } from "react-bootstrap";

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
      <div>
        {this.state.biz.map((biz) => (
          <Card key={biz.key} style={{ width: "18rem" }}>
            <Card.Img variant="top" src="holder.js/100px180" />
            <Card.Body>
              <Card.Title>{biz.title}</Card.Title>
              <Card.Text>{biz.description}</Card.Text>
              <Card.Text>{biz.address}</Card.Text>
              <Button variant="primary">Go somewhere</Button>
            </Card.Body>
          </Card>
        ))}
      </div>
    );
  }
}

export default BizList;

// <ul>
//   {this.state.biz.map((biz) => (
//     <li key={biz.key}>{biz.title}</li>
//   ))}
// </ul>
