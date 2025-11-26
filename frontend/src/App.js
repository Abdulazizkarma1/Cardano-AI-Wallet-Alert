import React, { useState, useEffect } from 'react';
import './App.css';
import RuleForm from './components/RuleForm';
import RulesList from './components/RulesList';
import { getRules, createRule, parseInstruction } from './services/api';

function App() {
  const [rules, setRules] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const fetchRules = async () => {
    try {
      setLoading(true);
      const data = await getRules();
      setRules(data);
      setError(null);
    } catch (err) {
      setError('Failed to fetch rules');
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchRules();
  }, []);

  const handleCreateRule = async (ruleData) => {
    try {
      setLoading(true);
      await createRule(ruleData);
      await fetchRules();
      setError(null);
    } catch (err) {
      setError('Failed to create rule');
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  const handleParseInstruction = async (instruction) => {
    try {
      setLoading(true);
      const result = await parseInstruction(instruction);
      return result;
    } catch (err) {
      setError('Failed to parse instruction');
      console.error(err);
      throw err;
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1>Cardano AI Wallet Alerts</h1>
        <p className="subtitle">Prototype - Natural Language Wallet Monitoring</p>
      </header>

      <main className="App-main">
        {error && <div className="error-message">{error}</div>}

        <RuleForm
          onSubmit={handleCreateRule}
          onParse={handleParseInstruction}
          loading={loading}
        />

        <RulesList rules={rules} loading={loading} onRefresh={fetchRules} />
      </main>
    </div>
  );
}

export default App;


