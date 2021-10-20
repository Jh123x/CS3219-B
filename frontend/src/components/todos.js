import React from 'react'


const Todo = ({ todos, deleteCallback, updateCallback }) => {
    return (
        <div className="container">
            <ul className="list-group">
                {todos.map((todo) => {
                    return (
                        <li className="list-group-item" id={"item-" + todo.id} key={todo.id}>
                            <div className="text-right inline row">
                                <div className="col-md-6">
                                    <input
                                        className="form-check-input me-1"
                                        type="checkbox"
                                        id={"input-" + todo.id}
                                        aria-label="..."
                                        checked={todo.is_completed}
                                        onChange={() => updateCallback}
                                    />
                                    {todo.description}
                                </div>

                                <div className="col-md-6">
                                    <input type="button" className="btn btn-danger" value="delete" id={"btn-" + todo.id} onClick={deleteCallback} />
                                </div>
                            </div>
                        </li>
                    )
                })}
            </ul>
        </div>
    )
}

export default Todo