import axios from 'axios';

const API_BASE_URL = process.env.REACT_APP_API_URL || 'http://localhost:8000';

const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

export const getRules = async () => {
  const response = await api.get('/rules');
  return response.data;
};

export const getRule = async (id) => {
  const response = await api.get(`/rules/${id}`);
  return response.data;
};

export const createRule = async (ruleData) => {
  const response = await api.post('/rules', ruleData);
  return response.data;
};

export const deleteRule = async (id) => {
  await api.delete(`/rules/${id}`);
};

export const parseInstruction = async (instruction) => {
  const response = await api.post('/parse', { instruction });
  return response.data;
};


