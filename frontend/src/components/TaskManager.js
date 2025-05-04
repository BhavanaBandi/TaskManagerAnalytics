import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';

function TaskManager() {
  const [tasks, setTasks] = useState([]);
  const [newTask, setNewTask] = useState({ title: '', description: '', priority: 'Low', due_date: '' });
  const navigate = useNavigate();

  const token = localStorage.getItem('token');
  const api = axios.create({
    baseURL: 'http://localhost:5000',
    headers: { Authorization: `Bearer ${token}` }
  });

  useEffect(() => {
    api.get('/tasks')
      .then(res => setTasks(res.data))
      .catch(() => navigate('/login'));
  }, []);

  const handleCreate = async (e) => {
    e.preventDefault();
    try {
      await api.post('/tasks', newTask);
      const res = await api.get('/tasks');
      setTasks(res.data);
      setNewTask({ title: '', description: '', priority: 'Low', due_date: '' });
    } catch {
      alert('Failed to create task');
    }
  };

  return (
    <div className="container">
      <h2>Your Tasks</h2>
      <form onSubmit={handleCreate}>
        <input placeholder="Title" value={newTask.title} onChange={e => setNewTask({ ...newTask, title: e.target.value })} required />
        <input placeholder="Description" value={newTask.description} onChange={e => setNewTask({ ...newTask, description: e.target.value })} />
        <input type="date" value={newTask.due_date} onChange={e => setNewTask({ ...newTask, due_date: e.target.value })} />
        <select value={newTask.priority} onChange={e => setNewTask({ ...newTask, priority: e.target.value })}>
          <option>Low</option>
          <option>Medium</option>
          <option>High</option>
        </select>
        <button type="submit">Add Task</button>
      </form>
      <ul>
        {tasks.map(task => (
          <li key={task._id}>
            <strong>{task.title}</strong> - {task.description} ({task.priority})
          </li>
        ))}
      </ul>
    </div>
  );
}

export default TaskManager;
