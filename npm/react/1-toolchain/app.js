import React, { Component } from "react";
import ReactDOM from "react-dom";
import "./app.css";

class App extends Component{
  render(){
    return(
      <div className="App">
        <h1> Hello, React &amp; Webpack! </h1>
      </div>
    );
  }
}
ReactDOM.render(<App />, document.getElementById("root"));

export default App;
