import * as React from 'react';
import { GoogleButton } from './GoogleButton';
import { Socket } from './Socket';

export default function Login() {
  const [accounts, setAccounts] = React.useState([]);

  function updateUsers(data) {
    setAccounts(data.allUsers);
  }

  function getNewUsers() {
    React.useEffect(() => {
      Socket.on('users updated', updateUsers);
      return () => {
        Socket.off('users updated', updateUsers);
      };
    });
  }

  getNewUsers();

  return (
    <div>
      <h1>Log in with OAuth!</h1>
      <GoogleButton />
    </div>

  );
}
