import * as React from 'react';
import ReactDOM from 'react-dom';
import GoogleLogin from 'react-google-login';
import { Socket } from './Socket';
import { Content } from './Content';

const responseGoogle = (response) => {
  const { name } = response.profileObj;
  const { email } = response.profileObj;
  const pfp = response.profileObj.imageUrl;
  Socket.emit('new google user', {
    name, email, pfp,
  });
  return ReactDOM.render(<Content />, document.getElementById('content'));
};

export default function GoogleButton() {
  return (
    <GoogleLogin
      clientId="778126205197-otgo1t4j6baunn67e82kgqj1k7ffhcq3.apps.googleusercontent.com"
      buttonText="Login"
      onSuccess={responseGoogle}
      onFailure={responseGoogle}
      cookiePolicy="single_host_origin"
    />
  );
}
