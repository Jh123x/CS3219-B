import React, { Component } from 'react';
import axios from 'axios';
import Todo from './components/todos';

const url = "http://127.0.0.1:8000/todo"

class App extends Component {
  constructor(props) {
    super(props)
    this.state = {
      todos: [],
      updated: [],
      newTask: "",
    }
    this.submitNewTodo = this.submitNewTodo.bind(this)
    this.updateTodo = this.updateTodo.bind(this)
    this.updateNewTask = this.updateNewTask.bind(this)
    this.deleteTodo = this.deleteTodo.bind(this)
    this.todoUpdate = this.todoUpdate.bind(this)
  }

  todoUpdate = () => {
    fetch(url, { method: 'GET' })
      .then(res => res.json())
      .then(data => {
        this.setState({ todos: data })
      })
      .catch(console.log)
  }

  componentDidMount() {
    this.todoUpdate()
  }

  submitNewTodo(_) {
    const formData = new FormData();
    formData.append('description', this.state.newTask)
    const config = {
      headers: {
        "content-type": 'multipart/form-data'
      }
    }
    axios.post(url, formData, config)
  }

  updateTodo(event) {
    console.log(event.target.id);
    const id = event.target.id.split('-')[1]
    axios.put(url + "/" + id)
    this.setState({ todos: this.state })
    window.location.reload()
  }

  updateNewTask = (event) => this.setState({ newTask: event.target.value })

  deleteTodo(event) {
    console.log("Item deleted: " + event.target.id)
    const id = event.target.id.split('-')[1]
    axios.delete(url + "/" + id)
    window.location.reload()
  }

  render() {
    return (
      <div className="container">
        <center><h1>Todo List</h1></center>
        <form onChange={this.updateTodo}>
          <Todo todos={this.state.todos} deleteCallback={this.deleteTodo} updateCallback={this.updateTodo} onChange={this.todoUpdate} />
        </form>
        <hr />
        <div className="container">
          <form className="mb-3" onSubmit={this.submitNewTodo}>
            <label htmlFor="todoTitle" className="form-label">Task Title</label>
            <input
              type="text"
              className="form-control"
              id="todoTitle"
              placeholder="Very interesting title here"
              onChange={this.updateNewTask}
            />
            <br />
            <input type="submit" value="Submit" className="btn btn-primary" />
          </form>
        </div>
      </div>
    );
  }
}

export default App;
