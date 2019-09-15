import React from 'react'

import './App.css'


class App extends React.Component {
  constructor(props){
    super(props)
    this.state = {
      file: null
    }
    this.handleChange = this.handleChange.bind(this)
  }
  handleChange(event) {
    this.setState({
      file: URL.createObjectURL(event.target.files[0])
    })
  }
  render() {
    return (
      <div>
        <p>Testing here</p>
        <input type="file" onChange={this.handleChange}/>
        <img src={this.state.file}/>

      </div>
    );
  }
}

export default App
