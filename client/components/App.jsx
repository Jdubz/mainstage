import React from 'react';
import axios from 'axios';

class App extends React.Component {
  constructor() {
    super();
    this.state = {};
  }

  render() {
    return (
      <div>
        <div className="BG" />
        <h2>Mainstage Control</h2>
        <div className="container">
          <button
            onClick={() => {
              axios.get('/on/1');
            }}
          >ON</button>
          <button
            onClick={() => {
              axios.get('/on/0');
            }}
          >OFF</button>
        </div>
      </div>
    );
  }
}

export default App;
