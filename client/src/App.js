import React, { useState } from "react";
const chatScoket = new WebSocket("ws://127.0.0.1:8000/ws/home");
const App = () => {
  const [message, setMessage] = useState("");

  chatScoket.onmessage = (event) => {
    const data = JSON.parse(event.data);
    setMessage((prevMessages) => [...prevMessages, data.message]);
  };
  return (
    <div>
      <div>{message}</div>
    </div>
  );
};

export default App;
