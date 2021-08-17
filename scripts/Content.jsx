import * as React from 'react';
import { Button } from './Button';
import { Socket } from './Socket';

export default function Content() {
  const [messages, setMessages] = React.useState([]);
  const [users, setUsers] = React.useState([]);
  const [pfp, setPfp] = React.useState([]);
  const [links, setLinks] = React.useState([]);
  const [images, setImages] = React.useState([]);
  const [current, setCurrent] = React.useState(0);

  function updateMessages(data) {
    setCurrent(data.currentUsers);
    setMessages(data.allMessages);
    setUsers(data.allUsers);
    setPfp(data.allPfp);
    setLinks(data.allLinks);
    setImages(data.allImages);
    const messageBody = document.querySelector('#chatBody');
    messageBody.scrollTop = messageBody.scrollHeight - messageBody.clientHeight;
  }

  function getNewMessages() {
    React.useEffect(() => {
      Socket.on('messages received', updateMessages);
      return () => {
        Socket.off('messages received', updateMessages);
      };
    });
  }

  getNewMessages();

  return (
    <div>
      <div className="header">
        <h1><span>Shuo chat!</span></h1>
      </div>
      <div className="onlinecount">
        <h2>
          Currently
          { current }
          {' '}
          users online!
        </h2>
      </div>
      <div className="chatbox" id="chatBody">
        <ol id="chatList">
          {
                    messages.map((message, index) => (users[index] === 'zs-bot' ? (
                      <li key={index}>
                        <strong>
                          <img src="static/zsbot.jpg" id="botpic" alt="bot avatar" />
                          { users[index] }
                          :
                          { message }
                        </strong>
                      </li>
                    ) : (
                      <li id="chatlist" key={index}>
                        <img src={pfp[index]} id="pfp" alt="profile" />
                        { users[index] }
                        :
                        { message }
                        {' '}
                        <a href={links[index]}>{ links[index] }</a>
                        <img src={images[index]} alt="linked" />
                      </li>
                    )))
                    }
        </ol>
      </div>
      <Button />
    </div>

  );
}
