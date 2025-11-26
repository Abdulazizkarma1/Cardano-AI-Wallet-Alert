import React, { useState } from 'react';

const RuleForm = ({ onSubmit, onParse, loading }) => {
  const [formData, setFormData] = useState({
    wallet_address: '',
    condition: '',
    timeframe: '',
    notification_channel: 'email'
  });
  const [useNaturalLanguage, setUseNaturalLanguage] = useState(false);
  const [naturalLanguage, setNaturalLanguage] = useState('');
  const [parsePreview, setParsePreview] = useState(null);

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setFormData(prev => ({
      ...prev,
      [name]: value
    }));
  };

  const handleParse = async () => {
    if (!naturalLanguage.trim()) {
      alert('Please enter a natural language instruction');
      return;
    }

    try {
      const result = await onParse(naturalLanguage);
      setParsePreview(JSON.stringify(result, null, 2));
      
      // Auto-fill form with parsed data
      if (result.parsed_rule) {
        setFormData(prev => ({
          ...prev,
          wallet_address: result.parsed_rule.wallet || prev.wallet_address,
          condition: result.parsed_rule.condition || prev.condition,
          timeframe: result.parsed_rule.timeframe || prev.timeframe
        }));
      }
    } catch (err) {
      alert('Failed to parse instruction');
    }
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    
    if (!formData.wallet_address || !formData.condition) {
      alert('Please fill in wallet address and condition');
      return;
    }

    onSubmit(formData);
    
    // Reset form
    setFormData({
      wallet_address: '',
      condition: '',
      timeframe: '',
      notification_channel: 'email'
    });
    setNaturalLanguage('');
    setParsePreview(null);
  };

  return (
    <div className="card">
      <h2>Create Alert Rule</h2>
      
      <div style={{ marginBottom: '20px' }}>
        <label>
          <input
            type="checkbox"
            checked={useNaturalLanguage}
            onChange={(e) => setUseNaturalLanguage(e.target.checked)}
            style={{ marginRight: '8px' }}
          />
          Use Natural Language Input
        </label>
      </div>

      {useNaturalLanguage && (
        <div className="form-group">
          <label>Natural Language Instruction</label>
          <textarea
            value={naturalLanguage}
            onChange={(e) => setNaturalLanguage(e.target.value)}
            placeholder="e.g., Alert me when wallet addr_test1... receives more than 100 ADA in the next hour"
          />
          <button
            type="button"
            className="btn btn-secondary"
            onClick={handleParse}
            disabled={loading}
            style={{ marginTop: '10px' }}
          >
            Parse Instruction
          </button>
          {parsePreview && (
            <div className="parse-preview">
              <strong>Parsed Result:</strong>
              <pre>{parsePreview}</pre>
            </div>
          )}
        </div>
      )}

      <form onSubmit={handleSubmit}>
        <div className="form-group">
          <label>Wallet Address *</label>
          <input
            type="text"
            name="wallet_address"
            value={formData.wallet_address}
            onChange={handleInputChange}
            placeholder="addr_test1..."
            required
          />
        </div>

        <div className="form-group">
          <label>Condition *</label>
          <input
            type="text"
            name="condition"
            value={formData.condition}
            onChange={handleInputChange}
            placeholder="e.g., receive > 100 ADA"
            required
          />
        </div>

        <div className="form-group">
          <label>Timeframe</label>
          <input
            type="text"
            name="timeframe"
            value={formData.timeframe}
            onChange={handleInputChange}
            placeholder="e.g., 1h, 24h, 7d"
          />
        </div>

        <div className="form-group">
          <label>Notification Channel</label>
          <select
            name="notification_channel"
            value={formData.notification_channel}
            onChange={handleInputChange}
          >
            <option value="email">Email</option>
            <option value="sms">SMS</option>
            <option value="push">Push Notification</option>
            <option value="webhook">Webhook</option>
          </select>
        </div>

        <div className="button-group">
          <button type="submit" className="btn btn-primary" disabled={loading}>
            {loading ? 'Creating...' : 'Create Rule'}
          </button>
        </div>
      </form>
    </div>
  );
};

export default RuleForm;


