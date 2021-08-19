import React from "react";
import ReactDOM from "react-dom";
import Carousel from "react-elastic-carousel";
import Item from "./Item";
// import "./styles.css";

class App extends React.Component {
  render() {
    return (
      <div>
        <Carousel ref={ref => (this.carousel = ref)}>
          <Item>1
            <button onClick={() => this.carousel.slidePrev()}>Prev</button>
            <button onClick={() => this.carousel.slideNext()}>Next</button>
            <hr />
          </Item>
          <Item>2A
            <button onClick={() => this.carousel.slidePrev()}>Prev</button>
            <button onClick={() => this.carousel.slideNext()}>Next</button>
            <hr />
          </Item>
          <Item>2</Item>
          <Item>3</Item>
          <Item>4</Item>
          <Item>5</Item>
          <Item>6</Item>
        </Carousel>
      </div>
    )
  }
}

const rootElement = document.getElementById("root");
ReactDOM.render(<App />, rootElement);
