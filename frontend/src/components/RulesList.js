import React from 'react';

const RulesList = ({ rules, loading, onRefresh }) => {
  if (loading && rules.length === 0) {
    return (
      <div className="card">
        <h2>Active Rules</h2>
        <div className="loading">Loading rules...</div>
      </div>
    );
  }

  return (
    <div className="card">
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '20px' }}>
        <h2>Active Rules</h2>
        <button className="btn btn-secondary" onClick={onRefresh} disabled={loading}>
          Refresh
        </button>
      </div>

      {rules.length === 0 ? (
        <div className="empty-state">
          <p>No rules created yet. Create your first alert rule above!</p>
        </div>
      ) : (
        <div className="rules-list">
          {rules.map((rule) => (
            <div key={rule.id} className="rule-item">
              <h3>Rule: {rule.id?.substring(0, 8)}...</h3>
              <p><strong>Wallet:</strong> {rule.wallet_address}</p>
              <p><strong>Condition:</strong> {rule.condition}</p>
              {rule.timeframe && (
                <p><strong>Timeframe:</strong> {rule.timeframe}</p>
              )}
              <div className="rule-meta">
                <span><strong>Channel:</strong> {rule.notification_channel}</span>
                <span><strong>Status:</strong> {rule.active ? 'Active' : 'Inactive'}</span>
                {rule.created_at && (
                  <span><strong>Created:</strong> {new Date(rule.created_at).toLocaleString()}</span>
                )}
              </div>
            </div>
          ))}
        </div>
      )}
    </div>
  );
};

export default RulesList;


