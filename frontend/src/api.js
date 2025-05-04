import axios from 'axios';

const BASE_URL = 'http://localhost:5000'; 
const API = axios.create({ baseURL: BASE_URL });


API.interceptors.request.use((req) => {
  const token = localStorage.getItem('token');
  if (token) {
    req.headers.Authorization = `Bearer ${token}`;
  }
  return req;
});


export const register = async (formData) => {
  const res = await API.post('/register', formData);
  return res.data;
};


export const login = async (formData) => {
  const res = await API.post('/login', formData);
  return res.data;
};


export const gettasks = async () => {
  const res = await API.get('/tasks');
  return res.data;
};


export const createtask = async (taskData) => {
  const res = await API.post('/tasks', taskData);
  return res.data;
};
