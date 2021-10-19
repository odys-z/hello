/**
 * https://reactrouter.com/web/example/url-params
 */

import React from 'react';
import ReactDOM from 'react-dom';

import {
  BrowserRouter as Router,
  Routes,
  Route,
  Link,
} from "./router-dom";

//home/ody/git/hello/npm/react/3-router-dom/src/router-index.tsx
// import { Route } from './router';
class Home extends React.Component {

  constructor(props) {
    console.log(props);
  }

  render() {
    return <>HOOOOOOOME</>
  }
}

const routes = [
  { path: "/",
    exact: true,
    name: 'Home',
    // sidebar: () => <div>home!</div>,
    // // main: () => <h2>Home</h2>
    main: () => Home
  },
  {
    path: "/bubblegum",
    name: 'Bubb',
    sidebar: () => <div>bubblegum!</div>,
    main: () => <h2>Bubblegum</h2>
  },
  {
    path: "/shoelaces",
    name: 'Shoe',
    sidebar: () => <div>shoelaces!</div>,
    main: () => <h2>Shoelaces</h2>
  }
];

export default function NaviExample() {
  return (
    <Router>
      <div style={{ display: "flex" }}>
        <div
          style={{
            padding: "10px",
            width: "20%",
            background: "#f0f0f0"
          }}
        >
          {/* <Routes>
            {routes.map((route, index) => (
              <Route
                key={index}
                path={route.path}
                exact={route.exact}
                // children={<>Current: <route.sidebar /></>}
                component={route.main}
                children={<>Current: {route.main}</>}
              />
            ))}
          </Routes> */}
          <ul style={{ listStyleType: "none", padding: 0 }}>
            <li>
              <Link to="/">Home</Link>
            </li>
            <li>
              <Link to="/bubblegum">Bubblegum</Link>
            </li>
            <li>
              <Link to="/shoelaces">Shoelaces</Link>
            </li>
          </ul>

        </div>

        <div style={{ flex: 1, padding: "10px" }}>
          <Routes>
            {routes.map((route, index) => (
              // Render more <Route>s with the same paths as
              // above, but different components this time.
              <Route
                key={index}
                path={route.path}
                exact={route.exact}
                component={<Home/>}
              />
            ))}
          </Routes>
        </div>
      </div>
    </Router>
  );
}

export function bindNav(eid) {
	ReactDOM.render(
		<NaviExample />,
		document.getElementById(eid)
	);
}
