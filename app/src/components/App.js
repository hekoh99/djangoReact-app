// import React, {Component} from 'react';
// import logo from './logo.svg';
// import './App.css';
//
// function App() {
//   return (
//     <div className="App">
//       <header className="App-header">
//         <img src={logo} className="App-logo" alt="logo" />
//         <p>
//           Edit <code>src/App.js</code> and save to reload.
//         </p>
//         <a
//           className="App-link"
//           href="https://reactjs.org"
//           target="_blank"
//           rel="noopener noreferrer"
//         >
//           Learn React
//         </a>
//       </header>
//     </div>
//   );
// }

import React, { Component } from 'react';
import { NavLink, Route, Switch } from 'react-router-dom'
import Home from './Home'
import ChatList from '../containers/ChatList'

class App extends Component {
  render() {
    return (
      <div className="App">
        <div className="App-header">
          <h1>chatting Room</h1>
        </div>
        <div className="content-wrapper">
          <ul>
            <li><NavLink exact to="/">홈으로</NavLink></li>
            <li><NavLink to="/chat">채팅 리스트 보기</NavLink></li>
          </ul>
        <Switch>
          <Route exact path="/chat" component={ChatList}/>
          <Route exact path="/" component={Home}/>
        </Switch>
      </div>
      </div>
    );
  }
}

export default App;
