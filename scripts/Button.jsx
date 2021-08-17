import * as React from 'react';
import { Socket } from './Socket';

export default function Button() {
  const [user, setUser] = React.useState('');
  const [pfp, setPfp] = React.useState('');

  function handleSubmit(event) {
    const newMessage = document.getElementById('message_input');
    Socket.emit('new message input', {
      user,
      pfp,
      message: newMessage.value,
    });

    newMessage.value = '';

    event.preventDefault();
  }
  function updateUser(data) {
    setUser(data.username);
    setPfp(data.pfp);
  }
  function getNewUser() {
    React.useEffect(() => {
      Socket.on('user received', updateUser);
      return () => {
        Socket.off('user received', updateUser);
      };
    });
  }

  getNewUser();

  return (
    <form onSubmit={handleSubmit}>
      <input id="message_input" placeholder="Enter a message" />
      <button type="submit">Send!</button>
    </form>
  );
}
