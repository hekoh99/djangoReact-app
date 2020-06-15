import React, { Component } from 'react';
import { connect } from 'react-redux';
import Chat from '../components/Chat';
import { fetchChat } from '../actions/index';

class ChatList extends Component {
  componentDidMount() {
    this.props.fetchChat();
  }

  renderChat () {
    return this.props.chatList.map((chat) => {
      return <li key={chat.id}><Chat chatData={chat}/></li>;
    });
  }

  render () {
    return (
      <div>
        <h2>채팅 리스트</h2>
        <ul>
          {this.renderChat()}
        </ul>
      </div>
    );
  }
}

export default connect((state) => {
  return {
    chatList: state.lists.chatList
  };
}, { fetchChat })(ChatList);
